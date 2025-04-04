import pdfplumber
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def cluster_x0_positions(words, n_clusters=None):
    x0s = np.array([w['x0'] for w in words]).reshape(-1, 1)
    if n_clusters is None:
        n_clusters = min(len(x0s), 10)
    kmeans = KMeans(n_clusters=n_clusters, n_init='auto').fit(x0s)
    centers = sorted([c[0] for c in kmeans.cluster_centers_])
    return centers


def extract_table_by_position(page, y_tolerance=3):
    words = page.extract_words(x_tolerance=1, y_tolerance=1, keep_blank_chars=True)
    if not words:
        return []

    words.sort(key=lambda w: (round(w['top'] / y_tolerance), w['x0']))
    x_centers = cluster_x0_positions(words)
    x_boundaries = [-float('inf')] + [(x_centers[i] + x_centers[i + 1]) / 2 for i in range(len(x_centers) - 1)] + [float('inf')]

    rows = []
    current_row_y = None
    current_row = [[] for _ in range(len(x_boundaries) - 1)]

    for word in words:
        word_y = round(word['top'] / y_tolerance)
        if current_row_y is None:
            current_row_y = word_y

        if word_y != current_row_y:
            rows.append([' '.join(cell).strip() for cell in current_row])
            current_row = [[] for _ in range(len(x_boundaries) - 1)]
            current_row_y = word_y

        for i in range(len(x_boundaries) - 1):
            if x_boundaries[i] <= word['x0'] < x_boundaries[i + 1]:
                current_row[i].append(word['text'])
                break

    if any(current_row):
        rows.append([' '.join(cell).strip() for cell in current_row])

    return rows


def extract_tables_from_pdf(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            rows = extract_table_by_position(page)
            if not rows or len(rows) < 2:
                continue
            df = pd.DataFrame(rows)
            df.columns = df.iloc[0]
            df = df[1:].reset_index(drop=True)
            df.columns = [f"Column_{i}" if pd.isna(col) or col is None else str(col) for i, col in enumerate(df.columns)]
            df.fillna("", inplace=True)
            tables.append((page_number, df))
    return tables
