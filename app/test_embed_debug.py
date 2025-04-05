import pandas as pd
import pickle
import cohere
import os

# API Key
api_key = "4tJO50mMzwVSWor7obvxGQi7XQXPOv8EK0ZGnb4K"

try:
    co = cohere.Client(api_key)
except Exception as e:
    print("❌ Failed to initialize Cohere client:", e)
    exit()

file_path = "app/assessments.csv"

if not os.path.exists(file_path):
    print("❌ assessments.csv file not found.")
    exit()

df = pd.read_csv(file_path)

if df.empty:
    print("❌ assessments.csv is empty.")
    exit()

if "description" not in df.columns:
    print("❌ 'description' column not found in assessments.csv.")
    exit()

print("📄 Loaded CSV with", len(df), "rows")

try:
    texts = df["description"].tolist()
    response = co.embed(texts=texts, model="embed-english-v3.0", input_type="classification")

    embeddings = response.embeddings
    df["embedding"] = embeddings
except Exception as e:
    print("❌ Embedding generation failed:", e)
    exit()

output_path = "app/embeddings.pkl"

try:
    with open(output_path, "wb") as f:
        pickle.dump(df, f)
    print("✅ Embeddings saved to", output_path)
except Exception as e:
    print("❌ Failed to save embeddings.pkl:", e)
