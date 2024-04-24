import os 
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader= PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            return text
        
        except Exception as e:
            return file.read().decode("utf-8")
    else:
        raise Exception(
            "Unsupported file format, only pdf and text file supported."
        )

def get_table_data(quiz_str):
    try:
        quiz_dict= json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options="||".join(
                [
                    f"{option} -> {option_value}" for option, option_value in value["options"].items()
                ]
            )

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        
        return False