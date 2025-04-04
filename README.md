# pdf-table-extractor
Develop a tool to detect and extract tables from system-generated PDFs without using Tabula, Camelot, or converting the PDF into images. The extracted tables should then be stored in an Excel sheet. The tables may have borders, no borders, and irregular shapes.

![Screenshot 2025-04-04 162745](https://github.com/user-attachments/assets/19c5ac6e-99d1-476d-a819-1acf4b6f148b)
![Screenshot 2025-04-04 162758](https://github.com/user-attachments/assets/93b6b892-18f1-466a-a98b-d4e3a423b046)

## 🚀 Features

- ✅ Detects and extracts **tables** from PDFs (bordered or borderless)
- ✅ Supports **irregular layouts** and complex table structures
- ✅ **No dependency on Tabula, Camelot, or image conversion**
- ✅ Export extracted tables to **Excel (`.xlsx`)**
- ✅ Simple and intuitive **web interface**

## 🛠️ Tech Stack

| Technology      | Use Case                                |
|------------------|------------------------------------------|
| **Python**        | Backend & core logic                     |
| **Flask**         | Lightweight web framework                |
| **OpenCV**        | Table detection via image processing     |
| **Pandas**        | Data manipulation and Excel export       |
| **HTML/CSS**      | Web interface                            |
| **Jinja2**        | Template rendering                       |
| **Werkzeug**      | Secure file uploads                      |

---

## 📁 Project Structure
pdf-table-extractor/ ├── app.py # Flask app ├── smart_pdf_table_parser.py # Core table extraction logic ├── templates/ │ └── index.html # Frontend UI ├── static/ │ └── style.css # (Optional) CSS styling ├── uploads/ # Uploaded PDF files ├── outputs/ # Temporary output images/data ├── sample_pdfs/ │ └── example.pdf # Sample PDF for testing ├── output_excels/ │ └── example.xlsx # Extracted Excel output ├── README.md # Project documentation ├── requirements.txt # Python dependencies └── demo.mp4 # Demo video of the tool

📝 Requirements
Python 3.7+

Flask

OpenCV

Pandas

NumPy

(Optional) openpyxl / xlsxwriter for Excel output

All dependencies are listed in requirements.txt.
