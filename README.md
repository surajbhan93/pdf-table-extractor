# pdf-table-extractor
Develop a tool to detect and extract tables from system-generated PDFs without using Tabula, Camelot, or converting the PDF into images. The extracted tables should then be stored in an Excel sheet. The tables may have borders, no borders, and irregular shapes.

## 🔍 Problem Statement
Extracting tables from PDFs is often painful.

Many solutions require converting PDFs to images or use bulky tools like Tabula/Camelot.

Irregular layouts or missing borders make things worse.

## 💡 Our Solution
A smart PDF table extractor built with pdfplumber, pymupdf, and pandas.

Accurately detects and extracts tables from system-generated PDFs (even with irregular shapes or no borders).

Exports the data directly to Excel.

## 🚀 How It Works

1. Upload a system-generated PDF file.
2. The backend (powered by numpy + Pandas) detects tables from PDF pages.
3. It processes tables — even those with irregular or no borders.
4. Extracted table data is structured and exported as `.xlsx`.
5. Download your Excel file — clean and ready!

## Frontend Images
![Screenshot 2025-04-04 162745](https://github.com/user-attachments/assets/19c5ac6e-99d1-476d-a819-1acf4b6f148b)
![Screenshot 2025-04-04 162758](https://github.com/user-attachments/assets/93b6b892-18f1-466a-a98b-d4e3a423b046)
## excel file images data with column separate
![Screenshot 2025-04-04 172712](https://github.com/user-attachments/assets/a9acee43-cc06-4835-af31-ebb19d574636)

![Screenshot 2025-04-04 172725](https://github.com/user-attachments/assets/91c078eb-190c-4db6-a532-2991ab99d517)

---
## 📸 Demo

🎥 **Watch the Demo Video**

👉 [Click to watch on GitHub](https://github.com/user-attachments/assets/e5961cc0-d43e-4038-994a-c46a290bf075)

📁 **Or view on Google Drive:**

🔗 [Watch on Google Drive](https://drive.google.com/file/d/1WEl45yrzX4mkZ1M-IrFPVyvvICZTToFN/view?usp=sharing)

📂 You can also try with the sample file: `sample_pdfs/example.pdf`

## ⚙️ Libraries Used

| Library      | Description |
|--------------|-------------|
| `pdfplumber` | Extracts tables from PDFs, especially those without needing image conversion |
| `pymupdf`    | Handles PDF layout, structure, and metadata |
| `pandas`     | Used to structure table data into DataFrames |
| `openpyxl`   | For saving extracted data into Excel format |
| `streamlit`  | Creates the interactive web interface |


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


## 🛠️ Setup Instructions

### ✅ Step 1: Create Virtual Environment

```bash
python -m venv venv


 Step 2: Activate Virtual Environment
On Windows (PowerShell):

.\venv\Scripts\Activate.ps1

On Command Prompt:

.\venv\Scripts\activate.bat
On Linux/Mac:

source venv/bin/activate


Step 3: Install Required Libraries
You can install all required libraries at once:

pip install pdfplumber pymupdf pandas openpyxl streamlit
Or install one-by-one:

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

streamlit run app.py

---

## 📁 Project Structure
<pre> ```text pdf-table-extractor/ ├── app.py ├── smart_pdf_table_parser.py ├── templates/ │ └── index.html ├── static/ │ └── style.css (if any) ├── uploads/ ├── outputs/ ├── sample_pdfs/ │ └── example.pdf ├── output_excels/ │ └── example.xlsx ├── README.md ├── requirements.txt └── demo.mp4 ``` </pre>

---


## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
[git clone https://github.com/your-username/pdf-table-extractor.git](https://github.com/surajbhan93/pdf-table-extractor.git)

cd pdf-table-extractor



🤝 Contribution
Feel free to fork the repo, open issues, or submit pull requests.

🧠 Author
Made with ❤️ by Suraj Bhan


---

Let me know if you want this converted to PDF or LaTeX as well.
