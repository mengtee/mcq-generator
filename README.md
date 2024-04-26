# MCQ Generator using LangChain and OpenSource LLM

## Overview

This project aims to leverage open-source language model (LLM) capabilities to generate question and answer pairs for educational purposes. It utilizes Streamlit, a popular Python library for creating web applications, to provide an interactive user interface for generating and exploring these Q&A pairs.

## Features

- Generate question and answer pairs using open-source LLM models.
- Customize the subject, tone, and number of Q&A pairs generated.
- Explore the generated Q&A pairs in an interactive web application powered by Streamlit.

## Technologies Used

- Python
- Streamlit
- Open-source LLM models (llama-3)

## Getting Started

To run the Streamlit app locally:

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

4. Access the Streamlit app in your web browser at [http://localhost:8501](http://localhost:8501).

## Usage

1. Upon launching the Streamlit app, you will be presented with options to customize the generation of Q&A pairs, including the subject, tone, and number of pairs.
2. Once you've selected your preferences, click on the "Generate Q&A Pairs" button.
3. The app will utilize the specified LLM model to generate the Q&A pairs based on your inputs.
4. Explore the generated Q&A pairs displayed on the app interface. You can scroll through the pairs or download them for offline use.

## Limitations

- The project may encounter limitations related to context length when using LLM models, which could affect the quality and completeness of the generated Q&A pairs. Strategies such as chunking or summarization may be employed to address these limitations.

## Deployment on AWS EC2

1. Launch an EC2 instance on AWS and ensure it has the necessary permissions to access your repository.
2. SSH into your EC2 instance: ssh -i <key-file.pem> ec2-user@
3. Clone your repository onto the EC2 instance: git clone <repository-url>
4. Navigate to the project directory: cd <project-directory>
5. Install the required dependencies: pip install -r requirements.txt
6. Run the Streamlit app in a detached screen session to keep it running even after logout: streamlit run app.py
