## 🚀 AI-Powered Tax Assistant

This is a **Streamlit-based AI agent** that extracts salary details from an uploaded salary slip (image), calculates tax liabilities under both the **Old and New Tax Regimes**, and provides a **recommendation** on the better option. The app also generates an **AI-powered explanation** using **Google's Gemini AI**.
## 🌍 Live Demo  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Click here to view the app](https://taxassista-3y3bud5hget7o2eebv6udr.streamlit.app/) 

## ⚡ Features
✅ Extracts text from a salary slip image using **EasyOCR**.  
✅ Parses salary components such as **Basic Salary, HRA, Allowances, and Deductions**.  
✅ Calculates tax liability under both **Old and New Tax Regimes** (FY 2025-26).  
✅ Provides a recommendation on the **better tax regime**.  
🧠 Generates an **AI-powered explanation** using **Google Gemini AI**.  

> 🔹 **Note:** This tool supports salary slips in **JPG, JPEG, and PNG** formats only.  

# 📌 Installations 


## Prerequisites

Make sure you have Python 3.8+ installed on your system.

Install Dependencies

Run the following command to install the required packages:
```bash
pip install streamlit google-generativeai easyocr pillow torch torchvision
```
## Usage

**Step 1:** Obtain a Google Gemini API Key

&nbsp;&nbsp;&nbsp;&nbsp;Replace the API key in the script with your own Gemini API key:
```bash

API_KEY_GEMINI = "your-gemini-api-key-here"
```
&nbsp;&nbsp;&nbsp;&nbsp;You can obtain the API key from Google AI Studio.

**Step 2:** Run the Streamlit App

&nbsp;&nbsp;&nbsp;&nbsp;Use the following command to start the app:
```terminal
streamlit run your_script.py
```
**Step 3:** Upload Salary Slip

&nbsp;&nbsp;&nbsp;&nbsp;Upload a salary slip in JPG, JPEG, or PNG format.



# Project Structure

## 📂 Tax-ai-agent
```bash
│── your_script.py   # Main Streamlit app script
│── README.md        # Project documentation
│── requirements.txt # List of dependencies
```
# Troubleshooting

1. EasyOCR Model Download Issue

If EasyOCR fails to download models, manually create the required directory:
```bash
mkdir easyocr_models
```
2. Streamlit App Not Running

Ensure you have installed all dependencies correctly. Try running:
```bash
pip install --upgrade streamlit google-generativeai easyocr pillow torch torchvision
```
# Impact
The AI-powered tax recommendation system significantly reduced the time employees spent on tax-related inquiries and filing processes. By providing personalized insights and recommendations, it empowered employees to make informed financial decisions, ultimately leading to better tax compliance and optimization.
## Final Outcome

| File Upload | Explaination |
|-------------|-------------|
| ![Screenshot2](images/Screenshot%202025-02-25%20203359.png) | ![Screenshot1](images/Screenshot%202025-02-25%20203409.png) |





## Future Enhancements

Support for PDF salary slips.

More accurate tax deductions and exemptions.

Improved parsing for salary components.

# License

This project is open-source and free to use.

Developed by Nunna Naga Yaswitha 🚀
