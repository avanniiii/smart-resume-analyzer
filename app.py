import streamlit as st
from utils import extract_text_from_pdf, clean_text, calculate_similarity, find_missing_skills

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

# Custom Styling
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: grey;
    margin-bottom: 30px;
}
.score-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
    text-align: center;
}
.keyword-box {
    background-color: #ffe6e6;
    padding: 8px 12px;
    margin: 5px;
    border-radius: 20px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">💼 Smart Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your resume and compare it with the job description</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📝 Paste Job Description Here")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    similarity_score = calculate_similarity(resume_clean, job_clean)
    missing_skills = find_missing_skills(resume_clean, job_clean)

    st.markdown("## 📊 Match Score")

    st.markdown(f"""
    <div class="score-box">
        <h2>{similarity_score}% Match</h2>
    </div>
    """, unsafe_allow_html=True)

    st.progress(similarity_score / 100)

    if similarity_score > 75:
        st.success("🔥 Excellent Match! You're strongly aligned with this job.")
    elif similarity_score > 50:
        st.info("👍 Good Match. Consider improving some areas.")
    else:
        st.warning("⚠️ Low Match. Try tailoring your resume more.")

    st.markdown("## ❌ Missing Keywords")

    if missing_skills:
        for word in missing_skills:
            st.markdown(f'<span class="keyword-box">{word}</span>', unsafe_allow_html=True)
    else:
        st.success("🎉 No major keywords missing!")