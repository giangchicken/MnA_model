import h2o
from h2o.frame import H2OFrame
from tqdm import tqdm
import numpy as np

class H2OPredictor:
    """
    Class H2OPredictor:
        - Dự đoán M&A bằng mô hình H2O:
        - Load mô hình đã huấn luyện.
        - Dự đoán xác suất M&A.
        - Lọc kết quả theo ngưỡng.
    
        Args:
        - model_path: Storage model path
        - threshold: Set separate threshold for class

        Return:
        - Output:  statified articles along with probability

    """
    def __init__(self, model_path, threshold=0.2):
        self.model_path = model_path
        self.threshold = threshold
        h2o.init()
        self.model = h2o.load_model(model_path)
    
    def predict(self, embeddings, file_names):
        embed_array = np.array(embeddings)
        feature_cols = [f"feat_{i}" for i in range(embed_array.shape[1])]
        X_h2o = H2OFrame(embed_array)
        X_h2o.columns = feature_cols
        predictions = self.model.predict(X_h2o).as_data_frame(use_multi_thread=True)
        predicted_probs = predictions["p1"].values  # Xác suất M&A
        results = [
            {"file": file, "probability": prob}
            for file, prob in zip(file_names, predicted_probs) if prob >= self.threshold
        ]
        return results