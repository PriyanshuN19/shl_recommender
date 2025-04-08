# 🧠 SHL Assessment Recommendation Engine

An AI-powered system to recommend the most relevant SHL assessments based on your job role or query — built as part of the SHL AI Research Intern assignment.

---

## ✨ Features

- 🔍 Scrapes SHL's public catalog of assessments
- 🧠 Uses **Cohere Embeddings** 
- 📈 Computes **semantic similarity** with cosine distance
- 🖥️ Clean, modern **dark-themed web UI** with HTML/CSS
- 🔁 JSON API endpoint for integration with other apps

---

Here's the updated **📁 Folder Structure** section of your `README.md` based on your latest screenshot:

---

```markdown
## 🗂️ Folder Structure

```
SHL-Assessment-Recommender/
│
├── app/
│   ├── templates/                 # HTML templates (index.html)
│   ├── __pycache__/              # Python cache
│   ├── test_api.py               # Endpoint testing
│   ├── prepare_data.py           # Data prep script
│   ├── test_embed_debug.py       # Debugging embedding output
│   ├── data.pkl                  # Additional serialized data
│   ├── recommender.py            # Core logic: embeddings & search
│   ├── sample_shl_data.csv       # Sample input data
│   ├── debug_pickle.py           # Debug script
│   ├── embeddings.pkl            # Generated embeddings
│   ├── assessments.csv           # Scraped assessment data
│   └── scraper.py                # SHL scraper
│   └── main.py                   # Flask Server
        entry
├── requirements.txt              # Dependencies
├── runtime.txt                   # Python runtime version
├── Procfile                      # For deployment on Render/Heroku
├── .runtime                      # (optional runtime config)
└── README.md                     # Project documentation
```

## 🚀 Getting Started

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Add your Cohere API key to `recommender.py`:**

```python
COHERE_API_KEY = "your-cohere-api-key"
```

3. **Scrape data and generate embeddings:**

```bash
python app/recommender.py
```

4. **Run the Flask server:**

```bash
python main.py
```

5. **Access your app:**

```
http://127.0.0.1:5000/web
```

---

## 🌐 Live Demo & Endpoints

- 🔗 **Web UI:** https://shl-recommender-pefm.onrender.com/web  
- 📡 **API Endpoint:**  
  `POST https://shl-recommender-pefm.onrender.com/recommend`  
  Send JSON body like:
  
```json
{
  "query": "problem solving"
}
```

- 💻 **GitHub Repo:**  
  https://github.com/PriyanshuN19/shl_recommender

---

## 🧪 Example Query

> `"Looking for someone skilled in system design and creative thinking"`

✅ Returns:
- System Design Assessment  
- Creativity & Innovation Assessment  
- Visual Reasoning Test  

---

## 🛠️ Tech Stack

- Python 3.11.9
- Flask
- Cohere Embeddings (NLP)
- BeautifulSoup4
- Pandas, NumPy, Scikit-learn
- HTML5 + CSS3 (Dark Theme)

---

## 🙋‍♂️ Author

Made with ❤️ by **Priyanshu Nailwal**  
For SHL AI Research Intern Assignment – 2025

---

