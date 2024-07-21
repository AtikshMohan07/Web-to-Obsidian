import html2text as ht
import os
import sys
from pathlib import Path

text_maker = ht.HTML2Text()

def convertor(input_file, output_file): 
    try:
        with open(input_file, 'r', encoding='UTF-8') as f:
            htmlpage = f.read()
        text = text_maker.handle(htmlpage)
        with open(output_file, 'w', encoding='UTF-8') as f:
            f.write(text)
        print(f"Conversion successful. Markdown saved to {output_file}.")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convertor(input_file, output_file)
