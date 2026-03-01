import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Clean text
def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    return text

# Calculate similarity
def calculate_similarity(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectors)[0][1]
    return round(similarity * 100, 2)

# Find missing skills
def find_missing_skills(resume_text, job_description):
    resume_words = set(resume_text.split())
    job_words = set(job_description.split())
    missing = job_words - resume_words
    return list(missing)[:15]