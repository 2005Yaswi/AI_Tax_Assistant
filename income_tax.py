import streamlit as st
import google.generativeai as genai
import easyocr
import re
import os
from PIL import Image


from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY_GEMINI = os.getenv("API_KEY_GEMINI")
# Set up Google Gemini

  # Replace with your Gemini API key
genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

genai.configure(api_key=API_KEY_GEMINI)

try:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
  # Remove "models/"
  # Ensure correct model path
except Exception as e:
    st.error(f"Error initializing Gemini model: {e}")
    st.stop()

# Create a directory for EasyOCR models
os.makedirs("easyocr_models", exist_ok=True)

# Initialize EasyOCR with a custom model storage directory
reader = easyocr.Reader(['en'], model_storage_directory="easyocr_models")

# Function to extract text using EasyOCR
def extract_text_from_image(image_path):
    result = reader.readtext(image_path)
    extracted_text = " ".join([text[1] for text in result])  # Combine all detected text
    return extracted_text

# Function to clean and parse salary components
def parse_salary_data(text):
    salary_data = {
        "basic_salary": 0,
        "hra": 0,
        "allowances": 0,
        "deductions": 0,
    }

    # Improved regex patterns to match salary components
    basic_match = re.search(r"(Basic|Basic Wage)[\s:<]*₹?(\d+,?\d*)", text, re.IGNORECASE)
    hra_match = re.search(r"(HRA|House Rent Allowance)[\s:<]*₹?(\d+,?\d*)", text, re.IGNORECASE)
    allowances_match = re.search(r"(Conveyance Allowance|Total Allowances)[\s:<]*₹?(\d+,?\d*)", text, re.IGNORECASE)
    deductions_match = re.search(r"(Total Deductions|Deduccions Total)[\s:<]*₹?(\d+,?\d*)", text, re.IGNORECASE)

    if basic_match:
        salary_data["basic_salary"] = int(basic_match.group(2).replace(",", ""))
    if hra_match:
        salary_data["hra"] = int(hra_match.group(2).replace(",", ""))
    if allowances_match:
        salary_data["allowances"] = int(allowances_match.group(2).replace(",", ""))
    if deductions_match:
        salary_data["deductions"] = int(deductions_match.group(2).replace(",", ""))

    return salary_data

# Tax calculation function for the Old Regime (FY 2025-26)
def calculate_tax_old_regime(income, deductions=0):
    taxable_income = (income - deductions) * 12
    if taxable_income <= 250000:
        return 0
    elif 250001 <= taxable_income <= 500000:
        return (taxable_income - 250000) * 0.05
    elif 500001 <= taxable_income <= 1000000:
        return 12500 + (taxable_income - 500000) * 0.2
    else:
        return 112500 + (taxable_income - 1000000) * 0.3

# Tax calculation function for the New Regime (FY 2025-26)
def calculate_tax_new_regime(income):
    if income <= 1200000:
        return 0
    elif 1200001 <= income <= 2000000:
        return (income - 1200000) * 0.15
    elif 2000001 <= income <= 2400000:
        return 1200000 + (income - 2000000) * 0.2
    else:
        return 300000 + (income - 2400000) * 0.3

# Streamlit app
st.title("AI-Powered Tax Assistant")
st.write("Upload your salary slip and let the AI calculate your tax liability under both regimes!")

# Upload salary slip
uploaded_file = st.file_uploader("Upload Salary Slip (Image)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    # Save the uploaded file temporarily
    with open("temp_file.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text using EasyOCR
    extracted_text = extract_text_from_image("temp_file.png")

    # Parse salary data
    salary_data = parse_salary_data(extracted_text)
    st.write("Parsed Salary Data:", salary_data)

    # Calculate income
    income = salary_data["basic_salary"] + salary_data["hra"] + salary_data["allowances"]
    deductions = salary_data["deductions"]

    # Calculate tax under both regimes
    tax_old_regime = calculate_tax_old_regime(income, deductions)
    tax_new_regime = calculate_tax_new_regime(income * 12)

    # Display results
    st.write("Tax Liability:")
    st.write(f"Old Regime: ₹{tax_old_regime}")
    st.write(f"New Regime: ₹{tax_new_regime}")

    # Compare and suggest the better option
    if tax_old_regime < tax_new_regime:
        st.write("**Recommendation:** The Old Tax Regime is better for you.")
    else:
        st.write("**Recommendation:** The New Tax Regime is better for you.")

    # Generate explanation using Gemini
    input_text = f"""
    The user has the following salary details:
    - Basic Salary: ₹{salary_data['basic_salary']}
    - HRA: ₹{salary_data['hra']}
    - Allowances: ₹{salary_data['allowances']}
    - Deductions: ₹{salary_data['deductions']}

    The calculated tax under the Old Regime is ₹{tax_old_regime}, and under the New Regime is ₹{tax_new_regime}. Explain the tax calculation and recommend the better option.
    """

    response = model.generate_content(input_text)
    st.write("**Explanation:**")
    st.write(response.text)


    try:
        response = model.generate_content(input_text)
        st.write("**Explanation:**")
        st.write(response.text)
    except Exception as e:
        st.error(f"Error generating explanation: {e}")

