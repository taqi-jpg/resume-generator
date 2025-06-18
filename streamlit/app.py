import pdfkit
import tempfile
import streamlit as st

st.set_page_config(page_title="Resume Generator", layout="centered")

st.title("📝 Real-Time Resume Generator")

st.markdown("Fill the form to generate your resume preview:")

# Input fields
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
skills = st.text_input("Skills (comma-separated)")
experience = st.text_area("Experience")
education = st.text_area("Education")

# Real-time preview
st.subheader("📄 Resume Preview")
st.markdown(f"### {name or 'Your Name'}")
st.markdown(f"📧 {email or 'your@email.com'}")
st.markdown(f"📞 {phone or '+91-XXXXXXXXXX'}")
st.markdown("---")

if skills:
    st.markdown("**Skills**")
    skill_list = [f"- {skill.strip()}" for skill in skills.split(",")]
    st.markdown("\n".join(skill_list))

if experience:
    st.markdown("**Experience**")
    st.markdown(experience)

if education:
    st.markdown("**Education**")
    st.markdown(education)

if st.button("📄 Download Resume as PDF"):
    # Create HTML content for PDF
    html_content = f"""
    <h1>{name}</h1>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Phone:</strong> {phone}</p>
    <hr>
    <h2>Skills</h2>
    <ul>
        {''.join([f"<li>{s.strip()}</li>" for s in skills.split(',')])}
    </ul>
    <h2>Experience</h2>
    <p>{experience}</p>
    <h2>Education</h2>
    <p>{education}</p>
    """

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        pdfkit.from_string(html_content, f.name)
        with open(f.name, "rb") as file:
            btn = st.download_button(
                label="📥 Click to Download PDF",
                data=file,
                file_name="resume.pdf",
                mime="application/pdf"
            )

