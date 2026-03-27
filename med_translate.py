# BACK-END SOURCE CODE FOR MED-TRANSLATE PROJECT

# Importing the libraries to be used:-
from PyPDF2 import PdfReader
from google import genai

# Writing a function for it:-
def translate_medical_report(api_key, pdf_path):
    # Using try/except method:-
    try:
        reader = PdfReader(pdf_path) # Using the PdfReader module
        full_text = "" # storing all data from pdf into full_text

        for page in reader.pages:
            full_text += page.extract_text()

        if not full_text or full_text.strip() == "":
            return "Error: couldn't excess data from the PDF"
        
        #Using the genai module:-
        client = genai.Client(api_key = api_key)
        prompt = f"translate this medical report into easy and understandable language and advice:\n\n{full_text} also give AI warning"
        response = client.models.generate_content(
            model = 'gemini-3-flash-preview',
            contents = prompt
        )
        return response.text

    # To tackle errors:-
    except FileNotFoundError:
        return "Error:Couldn't locate the PDF"

    except Exception as e:
        return f"Error: {str(e)}" 
    
if __name__ == "__main__":
    api_key = input("Enter the API Key: ")        
    pdf_path = input("Enter the PDF name: ")  
    result = translate_medical_report(api_key, pdf_path)            
    print(result)



    