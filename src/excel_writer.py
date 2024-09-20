# src/excel_writer.py
import pandas as pd
import os

def write_to_excel(text_list, output_path):
    # Create a DataFrame with the recognized text
    df = pd.DataFrame(text_list, columns=['Recognized Text'])
    
    # Check if the Excel file already exists
    if os.path.exists(output_path):
        # If it exists, append to it
        existing_df = pd.read_excel(output_path)
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.to_excel(output_path, index=False)
    else:
        # Save a new Excel file
        df.to_excel(output_path, index=False)
    
    print(f"Output written to Excel at: {output_path}")
