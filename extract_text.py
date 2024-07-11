import os
from docx import Document

def read_docx(file_path):
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return ""

def save_text_to_file(text, output_file):
    try:
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        print(f"Successfully wrote to {output_file}")
    except Exception as e:
        print(f"Failed to write to {output_file}: {e}")

input_directory = './documents/'  
output_file = 'train_data.txt'


try:
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("")
    print(f"Cleared the content of {output_file}")
except Exception as e:
    print(f"Failed to clear {output_file}: {e}")

for filename in os.listdir(input_directory):
    if filename.endswith('.docx'):
        file_path = os.path.join(input_directory, filename)
        print(f"Processing file: {file_path}")  
        text = read_docx(file_path)
        if text.strip():  
            print(f"Extracted text from {filename}: {text[:100]}...")  
            save_text_to_file(text, output_file)
        else:
            print(f"No text extracted from {filename}")
