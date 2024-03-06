import streamlit as st
import PyPDF2
import openai
import json


OPEN_API_KEY = ''
openai.api_key = OPEN_API_KEY

# Set the page configuration
st.set_page_config(page_title="Closer Look", page_icon="upscaled.jpg")

# Define CSS style for the card
st.markdown(
    """
    <style>
    .card {
        padding: 5px;
        background-color: #2F2F2F;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        margin-bottom: 20px;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .card-content {
        padding: 10px;
        color: white;
    }
    .title-risk {
        background: linear-gradient(to right, #ff0000 30%, transparent 50%);
        padding: 10px 5px;
        border-radius: 5px;
    }

    .title-advantage {
        background: linear-gradient(to right, #28A745 30%, transparent 50%);
        padding: 10px 5px;
        border-radius: 5px;
    }

    .title-ambiguity {
        background: linear-gradient(to right, #FFA500 30%, transparent 50%);
        padding: 10px 5px;
        border-radius: 5px;
    }

    .popup {
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        z-index: 999;
    }
    """,
    unsafe_allow_html=True
)


# Define the main function for the app
def main():
    st.title("Legal Document Analyzer")
    upload_page()


# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to call OpenAI API for summarization
def call_openai_api(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust the model as needed
            messages=[{"role": "system", "content": prompt}],
            max_tokens=1000,  # Adjust the maximum tokens as needed
        )
        return completion.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "An error occurred while summarizing the text."

# Define the upload page
def upload_page():

    st.subheader("Upload Your Legal Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf","docx","doc"])

    if uploaded_file is not None:
        # Assuming you have a function to extract text from PDF
        extracted_text = extract_text_from_pdf(uploaded_file)

        st.success("File successfully uploaded!")
        st.write("Now click the button below to start analysis.")
        if st.button("Start Analysis"):
            # Assuming you have a function to analyze text using OpenAI API
            
            analysis_results_str = call_openai_api('Given below is a legal document. I want you to find the sentences which are risk for me, ambiguous and sentences which are advantageous to the person who agrees to it. Give me the output in json format with the sentences and the reason under the key names called Risks, Ambiguities and Advantages. Make the sentences you get as keys inside its respective heading and their reason as its value. This is the document:'+ extracted_text)
            
            # Find the index of the first '{' and last '}'
            start_index = analysis_results_str.find('{')
            end_index = analysis_results_str.rfind('}')

            analysis_results_str = analysis_results_str[start_index:end_index+1]
            analysis_results = json.loads(analysis_results_str)

            display_analysis_results(analysis_results)

            summary = call_openai_api('summarize this:'+ extracted_text)
            st.header("Summary:")
            st.write(summary)

# Function to create pop-up window
def show_popup(title, sentences_and_reasons):
    with st.expander(title):
        for sentence, reason in sentences_and_reasons.items():
            st.write(f"- **{sentence}:** {reason}")
        st.button("Close")

# Function to create a card-like component
def create_card(title, content):
    # Determine the appropriate CSS class based on the title name
    if "risks" in title.lower():
        title_class = "title-risk"
    elif "advantages" in title.lower():
        title_class = "title-advantage"
    elif "ambiguities" in title.lower():
        title_class = "title-ambiguity"
    else:
        title_class = "title-default"

    if content:
    # Generate HTML code for the card
        st.markdown(
            f'<div class="card {title_class}"><div class="card-content"><h3>{title}</h3>' +
            ''.join([f'<p>{key}</p>' for key in content.keys()]) +
            '</div></div>',
            unsafe_allow_html=True
        )
        
        # Create an expander for showing details
        with st.expander("Show Details", expanded=False):  # Set expanded to False to initially collapse the expander
            for sentence, reason in content.items():
                st.write(f"- **{sentence}:** {reason}")

# Function to display analysis results
def display_analysis_results(results):
    st.header("Analysis Results")
    # Create card components
    for title, content in results.items():
        create_card(title, content)


# Define the main function to run the app
if __name__ == "__main__":
    main()
