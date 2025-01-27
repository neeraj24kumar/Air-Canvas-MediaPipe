import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# Initialize variables
points = {0: [deque(maxlen=1024)], 1: [deque(maxlen=1024)], 2: [deque(maxlen=1024)], 3: [deque(maxlen=1024)]}
indices = {0: 0, 1: 0, 2: 0, 3: 0}
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]  # Blue, Green, Red, Yellow
colorIndex = 0
paintWindow = np.ones((471, 636, 3), dtype=np.uint8) * 255
kernel = np.ones((5, 5), np.uint8)

# Define toolbar buttons
buttons = [
    ("CLEAR", (40, 1, 140, 65), (200, 200, 200)),  # Light gray
    ("BLUE", (160, 1, 255, 65), (255, 0, 0)),     # Blue
    ("GREEN", (275, 1, 370, 65), (0, 255, 0)),    # Green
    ("RED", (390, 1, 485, 65), (0, 0, 255)),      # Red
    ("YELLOW", (505, 1, 600, 65), (0, 255, 255))  # Yellow
]

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# Initialize Mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert frame to RGB
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)

    # Create a copy of the frame for the toolbar
    toolbar_frame = frame.copy()

    # Draw toolbar buttons on the toolbar frame
    for label, (x1, y1, x2, y2), color in buttons:
        cv2.rectangle(toolbar_frame, (x1, y1), (x2, y2), color, -1)  # Filled rectangle
        cv2.putText(toolbar_frame, label, (x1 + 15, 40), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            landmarks = [(int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])) for lm in handlms.landmark]
            mpDraw.draw_landmarks(toolbar_frame, handlms, mpHands.HAND_CONNECTIONS)

            # Extract finger landmarks
            fore_finger, thumb = landmarks[8], landmarks[4]
            cv2.circle(toolbar_frame, fore_finger, 5, (0, 255, 0), -1)  # Draw fingertip

            # Handle gestures
            if thumb[1] - fore_finger[1] < 30:  # Close gesture
                for key in points:
                    points[key].append(deque(maxlen=1024))
                    indices[key] += 1
            elif fore_finger[1] <= 65:  # Toolbar area
                for i, (_, (x1, _, x2, _), _) in enumerate(buttons):
                    if x1 <= fore_finger[0] <= x2:
                        if i == 0:  # Clear button
                            points = {k: [deque(maxlen=1024)] for k in points}
                            indices = {k: 0 for k in indices}
                            paintWindow[67:, :, :] = 255
                        else:  # Color selection
                            colorIndex = i - 1
            else:
                points[colorIndex][indices[colorIndex]].appendleft(fore_finger)

    # Draw points on canvas
    for idx, color in enumerate(colors):
        for point in points[idx]:
            for k in range(1, len(point)):
                if point[k - 1] and point[k]:
                    cv2.line(paintWindow, point[k - 1], point[k], color, 2)

    # Show the windows
    cv2.imshow("Paint", paintWindow)
    cv2.imshow("Frame", toolbar_frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == 27:  # Escape key
        break

cap.release()
cv2.destroyAllWindows()
