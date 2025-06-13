import json
import pytesseract
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

pdf_path = "Delta_Dental_Family_Dental_PPO_2025.pdf"
base_pdf_url = "https://www.coveredca.com/forsmallbusiness/plans/PDFs/2025/Delta_Dental_Family_Dental_PPO_2025.pdf"

# Load PDF and convert to images
reader = PdfReader(pdf_path)
images = convert_from_path(pdf_path, dpi=300)

# Clean headers/footers
def clean_text(text):
    lines = text.split("\n")
    clean_lines = [line for line in lines if not any(x in line for x in [
        "Dentist Handbook January 2025", "Page |", "XGE-CA-ENT", "001-00118", "CoveredCA.com"
    ])]
    return "\n".join(clean_lines).strip()

# Extract text
results = []
for i, page in enumerate(reader.pages):
    page_number = i + 1
    pdf_text = page.extract_text() or ""
    ocr_text = pytesseract.image_to_string(images[i])
    full_text = clean_text(pdf_text + "\n" + ocr_text)

    results.append({
        "page": page_number,
        "content": full_text,
        "URL": f"{base_pdf_url}#page={page_number}"
    })

# Save to JSON
with open("Delta_Dental_PPO_2025_FullText.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Extraction complete: Delta_Dental_PPO_2025_FullText.json")
