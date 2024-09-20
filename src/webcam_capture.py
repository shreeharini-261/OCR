# src/webcam_capture.py
import cv2

def capture_image_from_webcam(output_path='../data/temp_frame.jpg'):
    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam")
        return False

    print("Press 'Space' to capture image, 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Display the live video
        cv2.imshow("Webcam", frame)

        # Wait for the space bar to capture an image
        key = cv2.waitKey(1)
        if key == 32:  # Space bar
            # Save the captured frame as an image file
            cv2.imwrite(output_path, frame)
            print(f"Captured image saved at: {output_path}")
            break
        elif key == ord('q'):
            # Quit the webcam
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    return True
