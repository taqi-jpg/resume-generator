from xhtml2pdf import pisa
import io
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
    result_html = f"""
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

    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(result_html), dest=pdf_buffer)

    if not pisa_status.err:
        st.download_button(
            label="📥 Click to Download PDF",
            data=pdf_buffer.getvalue(),
            file_name="resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("❌ Error generating PDF")

            

