import os 
import json
import pandas as pd
import traceback

# from langchain.chat_models import ChatOpenAI
from langchain_together import Together
from src.mcqgenerator.utils import TokenUsageTracker

# Load the environment file (containing the api keys)
from dotenv import load_dotenv

load_dotenv() 

KEY = os.getenv("TOGETHER_API_KEY")

token_tracker = TokenUsageTracker()
callbacks = [token_tracker]

llm = Together(
    model="NousResearch/Nous-Capybara-7B-V1p9",
    temperature=0.7,
    top_k=1,
    together_api_key= KEY,
)

from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

# Code for testing out 
# input_ = """You are a teacher with a deep knowledge of machine learning and AI. \
# You provide succinct and accurate answers. Answer the following question: 

# What is a large language model?"""
# print(llm.invoke(input_))

TEMPLATE = """
Text: {text}
You are an expert MCQ maker, Given the above text, it is your job to \
create a quiz pf {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}"""

# Creating prompt template
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number","subject", "tone", "response_json"],
    template= TEMPLATE
)

# Chain for creating the quiz
quiz_chain=LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key='quiz', verbose=True)

TEMPLATE2 ="""
You are an expert english grammarian and writer. Given a multiple choice quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis
if the quiz is not at par with the cognitive and analytical abilities of the students, \
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the students
Quiz_MCQs:
{quiz}

Check from an expert English writer of the above quiz:
"""
# Evaluation chain
quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)

review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# Combining two chain together
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"], output_variables=["quiz","review"], verbose=True)

file_path = "/Users/Development/mcq-generator/data.txt"

with open(file_path, 'r') as file:
    TEXT = file.read()

print(TEXT)

