# pdf-table-extractor
Develop a tool to detect and extract tables from system-generated PDFs without using Tabula, Camelot, or converting the PDF into images. The extracted tables should then be stored in an Excel sheet. The tables may have borders, no borders, and irregular shapes.

## 🚀 How It Works

1. Upload a system-generated PDF file.
2. The backend (powered by numpy + Pandas) detects tables from PDF pages.
3. It processes tables — even those with irregular or no borders.
4. Extracted table data is structured and exported as `.xlsx`.
5. Download your Excel file — clean and ready!

![Screenshot 2025-04-04 162745](https://github.com/user-attachments/assets/19c5ac6e-99d1-476d-a819-1acf4b6f148b)
![Screenshot 2025-04-04 162758](https://github.com/user-attachments/assets/93b6b892-18f1-466a-a98b-d4e3a423b046)



---

## ⚙️ Libraries Used

| Library      | Description |
|--------------|-------------|
| `pdfplumber` | Extracts tables from PDFs, especially those without needing image conversion |
| `pymupdf`    | Handles PDF layout, structure, and metadata |
| `pandas`     | Used to structure table data into DataFrames |
| `openpyxl`   | For saving extracted data into Excel format |
| `streamlit`  | Creates the interactive web interface |

---



## 🛠️ Setup Instructions

### ✅ Step 1: Create Virtual Environment

```bash
python -m venv venv


 Step 2: Activate Virtual Environment
On Windows (PowerShell):

bash
Copy
Edit
.\venv\Scripts\Activate.ps1
On Command Prompt:

bash
Copy
Edit
.\venv\Scripts\activate.bat
On Linux/Mac:

bash
Copy
Edit
source venv/bin/activate


Step 3: Install Required Libraries
You can install all required libraries at once:

bash
Copy
Edit
pip install pdfplumber pymupdf pandas openpyxl streamlit
Or install one-by-one:

bash
Copy
Edit
pip install pdfplumber
pip install pymupdf
pip install pandas
pip install openpyxl
pip install streamlit

## 🚀 Features

- ✅ Detects and extracts **tables** from PDFs (bordered or borderless)
- ✅ Supports **irregular layouts** and complex table structures
- ✅ **No dependency on Tabula, Camelot, or image conversion**
- ✅ Export extracted tables to **Excel (`.xlsx`)**
- ✅ Simple and intuitive **web interface**

## 🛠️ Tech Stack

🚀 How to Run the App
bash
Copy
Edit
streamlit run app.py


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
<pre> ```text pdf-table-extractor/ ├── app.py ├── smart_pdf_table_parser.py ├── templates/ │ └── index.html ├── static/ │ └── style.css (if any) ├── uploads/ ├── outputs/ ├── sample_pdfs/ │ └── example.pdf ├── output_excels/ │ └── example.xlsx ├── README.md ├── requirements.txt └── demo.mp4 ``` </pre>


---

## 📸 Demo

🎥 Watch the demo here: `demo.mp4`

Or try with the sample file in `sample_pdfs/example.pdf`.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
[git clone https://github.com/your-username/pdf-table-extractor.git](https://github.com/surajbhan93/pdf-table-extractor.git)
cd pdf-table-extractor



📝 Requirements
