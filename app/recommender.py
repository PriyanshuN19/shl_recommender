import numpy as np
import pickle
import cohere
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

# Load API key
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Set COHERE_API_KEY in .env")

# Load embeddings
with open("app/data.pkl", "rb") as f:
    df = pickle.load(f)

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

def recommend_assessments(query: str, top_n: int = 3):
    """Returns top N recommended assessments based on input query."""
    
    # Embed the query
    response = co.embed(texts=[query], model="embed-english-v3.0", input_type="search_query")
    query_embedding = np.array(response.embeddings)

    # Convert stored embeddings to array
    stored_embeddings = np.vstack(df["embeddings"].values)

    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, stored_embeddings)[0]

    # Get top-N indices
    top_indices = np.argsort(similarities)[::-1][:top_n]

    # Fetch results
    results = df.iloc[top_indices][["Role", "Recommended_Assessments"]].copy()
    results["Similarity"] = similarities[top_indices]

    return results
