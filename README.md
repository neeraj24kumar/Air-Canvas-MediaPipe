# Air-Canvas-MediaPipe
Created a virtual drawing interface that tracks finger movements to allow users to draw or write digitally. Assessed user engagement and the interface's applicability for creative or educational purposes.

The objective of this project is to develop a gesture-based painting application that allows users to create digital art or use it as a board using hand movements captured by a webcam. By leveraging computer vision techniques, specifically MediaPipe for hand tracking, the application enables users to draw on a virtual canvas by pointing and moving their fingers. Users can select colors and clear the canvas using intuitive gestures, enhancing the interactive experience without the need for traditional input devices like a mouse or stylus.

### System Components and Technologies Used:
- OpenCV: A library for computer vision tasks, used for video capture and image processing.
- NumPy: A library for numerical operations, utilized for creating and manipulating the paint canvas.
- MediaPipe: A framework for building multimodal machine learning applications, specifically used for hand tracking.
- Deque: A collection from the collections module used to store points for drawing lines on the canvas.
- Webcam: Captures live video feed of the user's hand gestures.


### Working:
1.	Initialization: Set up variables, colors, and toolbar buttons.
2.	Webcam Capture: Start capturing video frames from the webcam.
3.	Hand Detection: Process each frame to detect hand landmarks using MediaPipe.
4.	Toolbar Interaction: Draw toolbar buttons and check if the user's finger interacts with them (for color selection or clearing).
5.	Gesture Recognition: Recognize gestures for drawing (moving forefinger) and selecting options (thumb and forefinger proximity).
6.	Drawing on Canvas: Render lines on a virtual canvas based on finger movements.
7.	Display Output: Show both the drawing canvas and the frame with detected landmarks in real-time.
8.	Exit Condition: Allow the user to exit the application by pressing the escape key.

### Results: - 
Initially, after running the program, two windows will pop up, namely Paint and Frame. Paint refers to the canvas where all the outcomes will be seen. Frame refers to the window where all the actions are performed.

![image](https://github.com/user-attachments/assets/9013cf0f-7243-4881-8613-ad8be77c4269)
Figure 1: Initial window (Paint/ Canvas, Frame)

Hand landmarks detection: here all the points of the single hand are detected, and the green point on the index fingertip is the active point from where it is used as a brush or stylus. Rest all the red points are non-active in the below figure; nothing is drawn because the index finger and thumb are close to each other, which acts as a cap or lock where the green is inactive. points. Currently, in the below figure, nothing is drawn because the index finger and thumb are close to each other, which acts as a cap or lock where the pen is inactive.

![image](https://github.com/user-attachments/assets/cdf0d852-2122-415a-af01-1cc327ebe71a)
Figure 2: Hand landmark detection





Drawing different shapes in the paint window using available colors

![image](https://github.com/user-attachments/assets/7a0665b2-a786-4f88-bae9-7c55dbfcf7bc)
Figure 3: Drawing Shapes

Writing ‘MSCIT 224’ using the index finger i.e. the tip of the stylus

![image](https://github.com/user-attachments/assets/ea20a823-e731-43cc-9681-4cca0bed3f7e)
Figure 4: Writing MSCIT 224

The program functions as expected and demonstrates the true potential of computer vision by utilizing the MediaPipe and OpenCV libraries, which provide the necessary support for creating a gesture-recognized air canvas.

