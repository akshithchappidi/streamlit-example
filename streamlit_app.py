import streamlit as st

# Create a sidebar with links to the different sections of the portal.
sidebar = st.sidebar()
sidebar.title("Placement Portal")
sidebar.link("Student Section")
sidebar.link("Placement Section")
sidebar.link("Company Section")

# Create a main content area.
main_content = st.container()
main_content.title("Student Section")

# Add a form for students to register for placement.
registration_form = main_content.form("Registration Form")
registration_form.text("Name")
registration_form.text("Email")
registration_form.text("Phone Number")
registration_form.text("Resume")
registration_form.submit()

# Add a list of job openings.
job_openings = main_content.container()
job_openings.title("Job Openings")
for job_opening in job_openings:
    job_openings.text(job_opening["title"])
    job_openings.text(job_opening["description"])
    job_openings.link("Apply Now") 
