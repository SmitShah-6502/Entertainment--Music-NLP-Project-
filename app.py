# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# from flask_cors import CORS  # Allow frontend & backend communication

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# # Load Movie Dataset
# movies_path = "ml-1m/movies.dat"
# ratings_path = "ml-1m/ratings.dat"

# movies = pd.read_csv(movies_path, sep="::", engine="python", names=["MovieID", "Title", "Genres"], encoding="ISO-8859-1")
# ratings = pd.read_csv(ratings_path, sep="::", engine="python", names=["UserID", "MovieID", "Rating", "Timestamp"])

# movies["Year"] = movies["Title"].str.extract(r"\((\d{4})\)").astype(float)
# movies.dropna(inplace=True)
# movies["Year"] = movies["Year"].astype(int)
# movies["Title"] = movies["Title"].str.replace(r"\(\d{4}\)", "", regex=True).str.strip()

# # Load Music Dataset
# music_path = "music/spotify_millsongdata.csv"

# music = pd.read_csv(music_path)

# # Ensure columns exist
# expected_columns = {'artist', 'song', 'link', 'text'}
# if not expected_columns.issubset(music.columns):
#     raise KeyError("Music dataset missing expected columns")

# # Function to recommend movies based on genre
# def recommend_movies_by_genre(genre, top_n=10):
#     genre_movies = movies[movies["Genres"].str.contains(genre, case=False, na=False)]
#     if genre_movies.empty:
#         return []

#     movie_ratings = ratings.groupby("MovieID")["Rating"].mean()
#     genre_movies = genre_movies.merge(movie_ratings, on="MovieID", how="left")
#     genre_movies = genre_movies.sort_values(by="Rating", ascending=False)

#     final_recommendations = genre_movies.head(top_n)[["Title", "Year", "Rating"]]
#     return final_recommendations.to_dict(orient="records")

# # Function to recommend music based on genre
# def recommend_music_by_genre(genre, top_n=10):
#     genre_music = music[music["text"].str.contains(genre, case=False, na=False)]
#     if genre_music.empty:
#         return []

#     return genre_music.head(top_n)[["artist", "song", "link"]].to_dict(orient="records")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/recommend_movies", methods=["POST"])
# def recommend_movies():
#     genre = request.form.get("genre")
#     recommendations = recommend_movies_by_genre(genre)
#     return jsonify(recommendations)

# @app.route("/recommend_music", methods=["POST"])
# def recommend_music():
#     genre = request.form.get("music_genre")
#     recommendations = recommend_music_by_genre(genre)
#     return jsonify(recommendations)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import pandas as pd
import google.generativeai as genai
from flask_cors import CORS  # Allow frontend & backend communication

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load Movie Dataset
movies_path = "ml-1m/movies.dat"
ratings_path = "ml-1m/ratings.dat"

movies = pd.read_csv(movies_path, sep="::", engine="python", names=["MovieID", "Title", "Genres"], encoding="ISO-8859-1")
ratings = pd.read_csv(ratings_path, sep="::", engine="python", names=["UserID", "MovieID", "Rating", "Timestamp"])

movies["Year"] = movies["Title"].str.extract(r"\((\d{4})\)").astype(float)
movies.dropna(inplace=True)
movies["Year"] = movies["Year"].astype(int)
movies["Title"] = movies["Title"].str.replace(r"\(\d{4}\)", "", regex=True).str.strip()

# Load Music Dataset
music_path = "music/spotify_millsongdata.csv"
music = pd.read_csv(music_path)

# Ensure music dataset has expected columns
expected_columns = {'artist', 'song', 'text'}
if not expected_columns.issubset(music.columns):
    raise KeyError("Music dataset missing expected columns")

# Configure Gemini API
genai.configure(api_key="AIzaSyC8Qamg9uhd-jfUtMQ1fbyZ3CXwarfziKA")  
model = genai.GenerativeModel('gemini-1.5-pro')

# Recommend movies based on genre
def recommend_movies_by_genre(genre, top_n=10):
    genre_movies = movies[movies["Genres"].str.contains(genre, case=False, na=False)]
    if genre_movies.empty:
        return []

    movie_ratings = ratings.groupby("MovieID")["Rating"].mean()
    genre_movies = genre_movies.merge(movie_ratings, on="MovieID", how="left")
    genre_movies = genre_movies.sort_values(by="Rating", ascending=False)

    final_recommendations = genre_movies.head(top_n)[["Title", "Year", "Rating"]]
    return final_recommendations.to_dict(orient="records")
# Recommend music based on genre
def recommend_music_by_genre(genre, top_n=10):
    genre_music = music[music["text"].str.contains(genre, case=False, na=False)]
    if genre_music.empty:
        return []

    return genre_music.head(top_n)[["artist", "song"]].to_dict(orient="records")

# AI Storytelling function
def generate_story(prompt):
    try:
        if not prompt or not isinstance(prompt, str) or not prompt.strip():
            return "Error: Story prompt cannot be empty."

        response = model.generate_content(prompt)

        # Ensure response is valid
        if response and hasattr(response, "text") and response.text.strip():
            return response.text.strip()
        else:
            return "Error: No story generated. Try again."

    except Exception as e:
        return f"Error generating story: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend_movies", methods=["POST"])
def recommend_movies():
    genre = request.form.get("genre")
    recommendations = recommend_movies_by_genre(genre)
    return jsonify(recommendations)

@app.route("/recommend_music", methods=["POST"])
def recommend_music():
    genre = request.form.get("music_genre")
    recommendations = recommend_music_by_genre(genre)
    return jsonify(recommendations)

@app.route("/generate_story", methods=["POST"])
def generate_story_api():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()  
    if not prompt:
        return jsonify({"story": "❌ Please enter a story prompt!"})

    story = generate_story(prompt)
    return jsonify({"story": story})

if __name__ == "__main__":
    app.run(debug=True)
