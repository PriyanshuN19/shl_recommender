# app/prepare_data.py

import pandas as pd
import cohere
import numpy as np
import pickle
import os
from dotenv import load_dotenv

load_dotenv()
print("Loaded API Key:", os.getenv("4tJO50mMzwVSWor7obvxGQi7XQXPOv8EK0ZGnb4K"))

# Correct: Load from environment variable by name
COHERE_API_KEY = os.getenv("COHERE_API_KEY")


if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Set COHERE_API_KEY in your .env file or environment variables.")

# Load dataset
df = pd.read_csv("app/sample_shl_dataset.csv")  # Make sure this path is correct

# Combine roles and assessments into a single text for embedding
texts = (df["Role"] + ": " + df["Recommended_Assessments"]).tolist()

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Generate embeddings
response = co.embed(texts=texts, model="embed-english-v3.0", input_type="search_document")


# Store embeddings in a new column
df["embeddings"] = response.embeddings

# Save the dataframe with embeddings to a pickle file
with open("app/data.pkl", "wb") as f:
    pickle.dump(df, f)

print("✅ Data preparation completed. Embeddings saved to app/data.pkl")
