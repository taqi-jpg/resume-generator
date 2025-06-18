function updateResume() {
  document.getElementById("previewName").innerText = document.getElementById("fullName").value || "Your Name";
  document.getElementById("previewEmail").innerText = document.getElementById("email").value || "your@email.com";
  document.getElementById("previewPhone").innerText = document.getElementById("phone").value || "+91-XXXXXXXXXX";
  
  const skillsInput = document.getElementById("skills").value;
  const skillsList = document.getElementById("previewSkills");
  skillsList.innerHTML = "";
  if (skillsInput.trim() !== "") {
    const skillsArray = skillsInput.split(",");
    skillsArray.forEach(skill => {
      const li = document.createElement("li");
      li.textContent = skill.trim();
      skillsList.appendChild(li);
    });
  }

  document.getElementById("previewExperience").innerText = document.getElementById("experience").value;
  document.getElementById("previewEducation").innerText = document.getElementById("education").value;
}

function downloadResume() {
  const element = document.getElementById("resumePreview");
  html2pdf().from(element).save("My_Resume.pdf");
}
