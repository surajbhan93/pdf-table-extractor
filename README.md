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
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{fancyvrb}

\begin{document}

\section*{Project Directory Structure}

\begin{Verbatim}
pdf-table-extractor/
├── app.py
├── smart_pdf_table_parser.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (if any)
├── uploads/
├── outputs/
├── sample_pdfs/
│   └── example.pdf
├── output_excels/
│   └── example.xlsx
├── README.md
├── requirements.txt
└── demo.mp4
\end{Verbatim}

\end{document}


📝 Requirements
Python 3.7+

Flask

OpenCV

Pandas

NumPy

(Optional) openpyxl / xlsxwriter for Excel output

All dependencies are listed in requirements.txt.
