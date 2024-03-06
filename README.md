# CloserLook
This is a Streamlit application that analyzes legal documents, contracts and terms of services, (PDF, DOCX, or DOC) and provides insights into potential risks, ambiguities, and advantages for the person agreeing to the document. The app uses OpenAI's GPT-3.5-turbo model to analyze the text and generate the analysis results.

## Features
- Upload legal documents (PDF, DOCX, or DOC)
- Analyze the text and identify potential risks, ambiguities, and advantages
- Display the analysis results in a user-friendly card-like format
- Provide a summary of the document
- Show detailed information for each identified risk, ambiguity, or advantage

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
- Python 3.x
- streamlit
- PyPDF2
- openai
- python-docx (for DOCX and DOC support)
  
### Installation
- Clone the repository:
`git clone https://github.com/your-username/legal-document-analyzer.git`

- Navigate to the project directory:
cd `legal-document-analyzer`

- Install the required packages:
`pip install -r requirements.txt`

- Set up your OpenAI API key:
Obtain an API key from the OpenAI website (https://beta.openai.com/signup/).
In the app.py file, replace '' with your actual API key.

- Run the Streamlit app:
`streamlit run app.py`

The app will now be accessible at http://localhost:8501/.

## Usage
- Upload a legal document (PDF, DOCX, or DOC) using the file uploader.
- Click the "Start Analysis" button to initiate the analysis process.
- The app will display the analysis results in cards, categorized as Risks, Ambiguities, and Advantages.
- Expand the "Show Details" section to view detailed information for each identified risk, ambiguity, or advantage.
- A summary of the document will also be provided.
  
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Streamlit for the awesome framework
- PyPDF2 for PDF text extraction
- python-docx for DOCX and DOC text extraction
- OpenAI for the powerful language model
