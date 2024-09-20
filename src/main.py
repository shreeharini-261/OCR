# src/main.py
import os
from preprocess import preprocess_image
from ocr_model import recognize_handwriting
from excel_writer import write_to_excel
from webcam_capture import capture_image_from_webcam

# File paths
webcam_image = '../data/temp_frame.jpg'         # Temporary file for captured frame
preprocessed_image = '../data/preprocessed_handwriting.jpg'
excel_output = '../output/handwriting_output.xlsx'

# Create necessary directories if not exist
os.makedirs('../data', exist_ok=True)
os.makedirs('../output', exist_ok=True)

# Step 1: Capture Image from Webcam
if capture_image_from_webcam(webcam_image):
    # Step 2: Preprocess the Image
    preprocess_image(webcam_image, preprocessed_image)

    # Step 3: Recognize Handwriting
    recognized_text = recognize_handwriting(preprocessed_image)
    print(f"Recognized Text: {recognized_text}")

    # Step 4: Write to Excel
    write_to_excel(recognized_text, excel_output)
else:
    print("Image capture failed. Please try again.")
