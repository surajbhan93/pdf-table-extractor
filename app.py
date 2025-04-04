from flask import Flask, request, render_template, jsonify, send_from_directory
import os
import pandas as pd
import uuid
from smart_pdf_table_parser import extract_tables_from_pdf

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    file_id = str(uuid.uuid4())
    filename = f"{file_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    tables = extract_tables_from_pdf(file_path)
    if not tables:
        return jsonify({"error": "No tables found in PDF"}), 200

    output_excel_path = os.path.join(OUTPUT_FOLDER, f"{file_id}_tables.xlsx")
    with pd.ExcelWriter(output_excel_path) as writer:
        for page_num, df in tables:
            df.to_excel(writer, sheet_name=f"Page_{page_num}", index=False)

    return jsonify({
        "message": "Tables extracted and saved.",
        "download_link": f"/download/{os.path.basename(output_excel_path)}"
    })

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
