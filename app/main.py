# # app/main.py

# from flask import Flask, request, jsonify
# from recommender import recommend_assessments 

# app = Flask(__name__)
# from flask import render_template

# # Add this route below your other routes
# @app.route("/web")
# def frontend():
#     return render_template("index.html")
# @app.route("/", methods=["GET"])
# def home():
#     return "🧠 SHL Assessment Recommendation API is running!"

# @app.route("/recommend", methods=["POST"])
# def recommend():
#     # Get query from form data or JSON body
#     query = request.form.get("query") or (request.json and request.json.get("query"))

#     if not query:
#         return jsonify({"error": "No query provided"}), 400

#     try:
#         # Get recommendations from the recommender
#         recommendations_df = recommend_assessments(query)

#         # Convert DataFrame to list of dicts for JSON response
#         recommendations = recommendations_df.to_dict(orient="records")

#         return jsonify({
#             "query": query,
#             "recommendations": recommendations
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
# app/main.py

from flask import Flask, request, jsonify, render_template
from recommender import recommend_assessments 
import os
app = Flask(__name__, template_folder="templates")


@app.route("/web")
def frontend():
    return render_template("index.html")

@app.route("/", methods=["GET"])
def home():
    return "🧠 SHL Assessment Recommendation API is running!"

@app.route("/recommend", methods=["POST"])
def recommend():
    query = request.form.get("query") or (request.json and request.json.get("query"))

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        recommendations_df = recommend_assessments(query)
        recommendations = recommendations_df.to_dict(orient="records")
        return jsonify({
            "query": query,
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
import requests

response = requests.post("https://shl-recommender-pefm.onrender.com/recommend", json={"query": "problem solving"})
print(response.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
