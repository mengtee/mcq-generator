import os 
import PyPDF2
import json
import traceback
from langchain_core.callbacks.base import BaseCallbackHandler

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
    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except Exception as e:
            raise Exception("Error reading text file: {}".format(str(e)))
    else:
        raise Exception(
            "Unsupported file format, only pdf and text file supported."
        )


def get_table_data(quiz_str):
    print("Testing and calling quiz_str")
    print(quiz_str)
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [f"{option}: {option_value}" for option, option_value in value["options"].items()]
            )
            correct_answer = value["correct"]

            quiz_table_data.append({"MCQ": mcq, "Options": options, "Correct Answer": correct_answer})

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return None


class TokenUsageTracker(BaseCallbackHandler):
    def __init__(self):
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_cost = 0

    def on_llm_start(self, serialized, prompts, **kwargs):
        self.prompt_tokens += sum(len(prompt) for prompt in prompts)

    def on_llm_new_token(self, token, **kwargs):
        self.total_tokens += 1
        self.completion_tokens += 1

    def on_llm_end(self, response, **kwargs):
        self.total_cost = response.llm_output["cost"]