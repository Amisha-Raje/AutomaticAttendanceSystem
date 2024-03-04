import cv2
import time

# Create an object to hold reference to camera video capturing
vidcap = cv2.VideoCapture(0)

# Check if connection with camera is successful
if vidcap.isOpened():
    start_time = time.time()  # Get the start time
    
    # Loop until 1 minute has passed
    while time.time() - start_time < 60:
        ret, frame = vidcap.read()  # Capture a frame from live video

        # Check whether frame is successfully captured
        if ret:
            cv2.imshow("Frame", frame)  # Show captured frame
            
            # Press 'q' to break out of the loop
            if cv2.waitKey(1) & 0xFF == ord('x'):
                break
        # Print error if frame capturing was unsuccessful
        else:
            print("Error: Failed to capture frame")
            break

    # Release the camera
    vidcap.release()
    cv2.destroyAllWindows()

# Print error if the connection with camera is unsuccessful
else:
    print("Cannot open camera")
