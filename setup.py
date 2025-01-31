from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='mithun sarkar',
    author_email='mithunsarkar1307@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)