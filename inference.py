from fastapi import FastAPI, UploadFile, File
from preprocessing.preprocessing_infer import Preprocessor
from embedding.embedding_infer import Embedder
from model.model_infer import H2OPredictor
import os
import json
import shutil
from pathlib import Path

app = FastAPI()

# Khởi tạo model
preprocessor = Preprocessor()
embedder = Embedder(model_name="SBERT")
predictor = H2OPredictor(model_path="./model/StackedEnsemble_BestOfFamily_1_AutoML_3_20250227_84704", threshold=0.2)

UPLOAD_DIR = "uploaded_html"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict/")
async def predict(files: list[UploadFile] = File(...)):
    file_paths = []
    
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_paths.append(file_path)
    
    # Tiền xử lý
    descriptions, file_paths = preprocessor.process_files(file_paths)
    embeddings = embedder.encode(descriptions)
    results = predictor.predict(embeddings, file_paths)
    
    return results