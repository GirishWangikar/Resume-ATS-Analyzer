# ATS Resume Analyzer

The ATS Resume Analyzer is an interactive Gradio-based application designed to help users optimize their resumes for Applicant Tracking Systems (ATS). This tool allows users to upload a resume and a job description, and then provides a detailed analysis of the match between the two. Additionally, it offers a content rephrasing feature to help improve resume content according to ATS standards.

## Features

- **Resume Analysis**: Upload a PDF or DOCX resume and a job description to get a detailed analysis of how well the resume matches the job description.
- **Keyword Matching**: Identifies missing keywords and provides a match percentage based on the job description.
- **Content Rephrasing**: Rephrase resume content to optimize it for ATS, ensuring it includes quantifiable measures and improvements.
- **Customizable Parameters**: Adjust the temperature and max tokens to fine-tune the AI's responses.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7+
- Gradio
- Groq API key
- PyPDF2
- python-docx

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GirishWangikar/Resume-ATS-Analyzer
    cd ats-resume-analyzer
    ```

2. Install the required packages:
    ```bash
    pip install gradio groq PyPDF2 python-docx
    ```

3. Set up your API key as an environment variable:
    ```bash
    export API_KEY='your_api_key_here'
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to the URL provided in the console output.

3. **Resume Analyzer**:
    - Upload your resume (PDF or DOCX) and paste the job description into the provided fields.
    - Click "Analyze Resume" to get detailed feedback on your resume, including match percentage, missing keywords, and improvement suggestions.

4. **Content Rephraser**:
    - Enter the text you want to rephrase in the "Text to Rephrase" field.
    - Click "Rephrase" to receive a rephrased version optimized for ATS.

## Customization

- **Temperature**: Adjust the randomness of the AI's responses (0 for more deterministic, 1 for more creative).
- **Max Tokens**: Set the maximum length of the AI's responses.

## Contact

Created by Girish Wangikar

Check out more on [LinkedIn](https://www.linkedin.com/in/girish-wangikar/) | [Portfolio](https://girishwangikar.github.io/Girish_Wangikar_Portfolio.github.io/)
