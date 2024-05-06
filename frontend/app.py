import streamlit as st
import requests
import time

# Define the navigation links
nav_links = {
    "Home": "/",
    "About": "/about",
    "Contact": "/contact"
}

# Render the navbar
st.sidebar.title("Navigation")
for title, link in nav_links.items():
    st.sidebar.markdown(f"[{title}]({link})")


# Streamlit app title
st.title("GeoPolitics AI Agent")

st.header("Enter Regions")
regions = []
region_index = 0
while True:
    if region_index == 0:
        region = st.text_input(f"Regions:", key=f"region_{region_index}")
    else:
        region = st.text_input(f"Region {region_index + 1}:", key=f"region_{region_index}")
    if region:
        regions.append(region)
        region_index += 1
    else:
        break

# Input fields for subjects and regions
st.header("Enter Subjects")
subjects = []
subject_index = 0
while True:
    if subject_index == 0:
        subject = st.text_input(f"Subjects:", key=f"subject_{subject_index}")
    else:
        subject = st.text_input(f"Subject {subject_index + 1}:", key=f"subject_{subject_index}")
    if subject:
        subjects.append(subject)
        subject_index += 1
    else:
        break

# Button to trigger API request
if st.button("Submit"):
    # Placeholder for output
    output_placeholder = st.empty()
    # Display loading spinner
    spinner = st.spinner("Waiting for output...")
    
    # API endpoint for POST request
    post_api_url = "http://localhost:8080/api/crew"
    
    # Input data
    data = {
        "subjects": subjects,
        "regions": regions
    }
    
    # POST request to send input data
    post_response = requests.post(post_api_url, json=data)
    
    if post_response.status_code == 200:
        job_id = post_response.json().get("job_id")
        st.success(f"Request sent successfully.")
        
        # Polling loop to check job status
        while True:
            # GET request to check job status
            get_api_url = f"http://localhost:8080/api/crew/{job_id}"
            time.sleep(10)
            get_response = requests.get(get_api_url)
            #print(f"This is the response: {get_response.json()}")
            if get_response.status_code == 200:
                job_status = get_response.json().get("status")

                if job_status == "COMPLETE":
                    # Update placeholder with output data
                    output_placeholder.write("Output:")
                    output_placeholder.markdown(get_response.json()["result"])
                    # Remove loading spinner
                    spinner = None
                    break  # Break the polling loop
                elif job_status == "ERROR":
                    st.error("Job encountered an error.")
                    # Remove loading spinner
                    spinner = None
                    break  # Break the polling loop on error
                else:
                    continue  # Continue polling if job is not complete
    else:
        st.error("Failed to send request to the API.")
