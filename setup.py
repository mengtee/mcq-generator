# Installing local package in a local environment

from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="meng kiat",
    author_email="mengtee1127@gmail.com",
    install_requires=["openai", "langchain","streamlit", "python-dotenv",'PyPDF2'],
    package=find_packages()
)