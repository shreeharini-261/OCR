
import cv2

def preprocess_image(image_path, output_path):
  
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    
    image = cv2.GaussianBlur(image, (5, 5), 0)
    
 
    cv2.imwrite(output_path, image)
    print(f"Preprocessed image saved at: {output_path}")
