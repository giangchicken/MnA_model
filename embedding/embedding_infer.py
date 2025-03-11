from sentence_transformers import SentenceTransformer

class Embedder:
    """
    Class Embedder
        - Nhúng văn bản từ mô hình đã chọn:
        - Hỗ trợ SBERT và Bi-Encoder.
        - Encode danh sách văn bản.

    Args:
        - model_name: Choose model to embed
    
    Output:
        - Embedding vector
    """
    MODELS = {
        "SBERT": SentenceTransformer("keepitreal/vietnamese-sbert"),
        "Bi-Encoder": SentenceTransformer("bkai-foundation-models/vietnamese-bi-encoder"),
    }
    
    def __init__(self, model_name="SBERT"):
        if model_name not in self.MODELS:
            raise ValueError(f"Embedding model {model_name} không được hỗ trợ!")
        self.encoder = self.MODELS[model_name]
    
    def encode(self, texts):
        return self.encoder.encode(texts)