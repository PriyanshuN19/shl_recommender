
# 🧠 SHL Assessment Recommendation Engine

This is a simple AI-powered recommendation system that helps you find the most relevant SHL assessments based on a natural language query. Built for the SHL AI Research Intern assignment.

---

## 🔧 Features

- Scrapes SHL assessment catalog and saves data
- Generates semantic embeddings using **Gemini Pro**
- Finds top relevant assessments using **cosine similarity**
- Web interface powered by **Flask**
- Clean, responsive UI with HTML/CSS

---

## 🗂️ Project Structure

```
SHL-Assessment-Recommender/
│
├── app/
│   ├── scraper.py          # Scrapes SHL site
│   ├── recommender.py      # Generates embeddings + recommendation logic
│   ├── assessments.csv     # Scraped data (auto-generated)
│   └── embeddings.pkl      # Gemini-based embeddings (auto-generated)
│
├── templates/
│   └── index.html          # Web UI
│
├── main.py                 # Flask server
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 How to Run

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Set your Gemini API key (replace with your key in `recommender.py`):**

```python
GOOGLE_API_KEY = "your-api-key-here"
```

3. **Scrape and generate embeddings:**

```bash
python app/recommender.py
```

4. **Run the Flask app:**

```bash
python main.py
```

5. **Go to browser:**

```
http://127.0.0.1:5000
```

---

## 📌 Example Query

> I need an assessment for evaluating leadership and numerical skills.

✅ Returns top matching SHL assessments with their scores and descriptions.

---

## 🛠️ Tech Stack

- Python 3.10+
- Flask
- BeautifulSoup
- Pandas / NumPy / Scikit-learn
- Gemini Pro (Google Generative AI)

---

## 📬 Contact

Built with ❤️ by Priyanshu Nailwal for SHL Internship Assignment.

