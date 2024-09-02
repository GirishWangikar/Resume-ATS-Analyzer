import gradio as gr
import os
from groq import Groq
from PyPDF2 import PdfReader
from docx import Document

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

CSS = """
.duplicate-button { 
    margin: auto !important; 
    color: white !important; 
    background: black !important; 
    border-radius: 100vh !important;
}
h3, p, h1 { 
    text-align: center; 
    color: white;
}
footer { 
    text-align: center; 
    padding: 10px; 
    width: 100%; 
    background-color: rgba(240, 240, 240, 0.8); 
    z-index: 1000; 
    position: relative; 
    margin-top: 10px; 
    color: black;
}
"""

FOOTER_TEXT = """
<footer>
    <p>If you enjoyed the functionality of the app, please leave a like!<br>
    Check out more on <a href="https://www.linkedin.com/in/girish-wangikar/" target="_blank">LinkedIn</a> | 
    <a href="https://girishwangikar.github.io/Girish_Wangikar_Portfolio.github.io/" target="_blank">Portfolio</a></p>
</footer>
"""

TITLE = "<h1>📄 ATS Resume Analyzer 📄</h1>"
PLACEHOLDER = "Chat with AI about your resume and job descriptions..."

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def generate_response(message: str, system_prompt: str, temperature: float = 0.5, max_tokens: int = 512):
    conversation = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8B-Instant",
        messages=conversation,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=False
    )

    return response.choices[0].message.content

def analyze_resume(resume_text, job_description):
    prompt = f"""
    Please analyze the following resume in the context of the job description provided. Strictly check every single line in the job description and analyze the resume for exact matches. Maintain high ATS standards and give scores only to the correct matches. Focus on missing hard skills and soft skills. Provide the following details:
    1. The match percentage of the resume to the job description.
    2. A list of accurate missing keywords.
    3. Final thoughts on the resume's overall match with the job description in 3 lines.
    4. Recommendations on how to add the missing keywords and improve the resume in 3-4 points with examples.
    Job Description: {job_description}
    Resume: {resume_text}
    """
    return generate_response(prompt, "You are an expert ATS resume analyzer.")

def rephrase_text(text):
    prompt = f"""
    Please rephrase the following text according to ATS standards, including quantifiable measures and improvements where possible. Maintain precise and concise points which will pass ATS screening:
    Original Text: {text}
    """
    return generate_response(prompt, "You are an expert in rephrasing content for ATS optimization.")

def clear_conversation():
    return [], None

with gr.Blocks(css=CSS, theme="Nymbo/Nymbo_Theme") as demo:
    gr.HTML(TITLE)

    with gr.Tab("Resume Analyzer"):
        with gr.Row():
            with gr.Column():
                job_description = gr.Textbox(label="Job Description", lines=5)
                resume_file = gr.File(label="Upload Resume (PDF or DOCX)")
            with gr.Column():
                resume_content = gr.Textbox(label="Parsed Resume Content", lines=10)
        analyze_btn = gr.Button("Analyze Resume")
        output = gr.Markdown()

    with gr.Tab("Content Rephraser"):
        text_to_rephrase = gr.Textbox(label="Text to Rephrase", lines=5)
        rephrase_btn = gr.Button("Rephrase")
        rephrased_output = gr.Markdown()

    with gr.Accordion("⚙️ Parameters", open=False):
        temperature = gr.Slider(
            minimum=0, maximum=1, step=0.1, value=0.5, label="Temperature",
        )
        max_tokens = gr.Slider(
            minimum=50, maximum=1024, step=1, value=512, label="Max tokens",
        )

    def process_resume(file):
        if file is not None:
            file_type = file.name.split('.')[-1].lower()
            if file_type == 'pdf':
                return extract_text_from_pdf(file.name)
            elif file_type == 'docx':
                return extract_text_from_docx(file.name)
        return ""

    resume_file.upload(process_resume, resume_file, resume_content)

    analyze_btn.click(
        analyze_resume,
        inputs=[resume_content, job_description],
        outputs=[output]
    )

    rephrase_btn.click(
        rephrase_text,
        inputs=[text_to_rephrase],
        outputs=[rephrased_output]
    )

    gr.HTML(FOOTER_TEXT)

if __name__ == "__main__":
    demo.launch()
