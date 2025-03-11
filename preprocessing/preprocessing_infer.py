import os
import json
import numpy as np
from tqdm import tqdm
from pathlib import Path
from newspaper import fulltext
from sentence_transformers import SentenceTransformer

class Preprocessor:
    """
    Class Preprocessor:
        - Nhận danh sách đường dẫn file HTML.
        - Tiền xử lý và loại bỏ ký tự xuống dòng.
    
    Args:
        - model_path: Đường dẫn mô hình H2O đã huấn luyện.
        - threshold: Ngưỡng dự đoán (probability).
        - embedding_model: Tên mô hình nhúng sử dụng.
    
    Output:
        - Danh sách extracted text
    """

    def __init__(self):
        # self.model_paths = model_paths
        self.type = None

    def read_news(self, html_file):
        """Đọc nội dung bài báo từ file HTML và loại bỏ ký tự xuống dòng."""
        with open(html_file, "r", encoding="utf-8") as file:
            html_content = file.read()
        extracted_text = fulltext(html_content, language="vi")
        return extracted_text.replace("\n", " ").strip() if extracted_text else ""

    def process_files(self, file_paths):
        """Tiền xử lý văn bản và nhúng embedding."""
        descriptions, file_names = [], []

        # Đọc và làm sạch nội dung
        for file_path in file_paths:
            extracted_text = self.read_news(file_path)
            if extracted_text:
                descriptions.append(extracted_text)
                file_names.append(file_path)

        return descriptions, file_names