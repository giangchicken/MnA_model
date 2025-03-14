# 1️⃣ Sử dụng Python 3.10 trên Debian Slim (tốt hơn Alpine cho PyTorch)
FROM python:3.10-slim

# 2️⃣ Cài đặt các gói hệ thống cần thiết
RUN apt update && apt install -y \
    bash curl unzip openjdk-17-jre \
    gcc g++ build-essential libstdc++6 libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 3️⃣ Thiết lập JAVA_HOME cho Java (cần cho H2O)
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# 4️⃣ Thiết lập thư mục làm việc
WORKDIR /app

# 5️⃣ Cài đặt thư viện Python
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt

# 6️⃣ Sao chép mã nguồn FastAPI vào container
COPY inference.py ./
COPY preprocessing ./preprocessing
COPY embedding ./embedding
COPY model ./model

# 7️⃣ Mở cổng API và chạy Uvicorn
EXPOSE 8000
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
