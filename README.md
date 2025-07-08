# Entertainment--Music-NLP-Project

# 🎬 Movie & 🎵 Music Recommendation System + 📖 AI Story Generator

This is a web-based application that provides movie and music recommendations based on selected genres and also includes an AI-powered storytelling chatbot using Google Gemini.

## 🌟 Features

- 🎥 **Movie Recommendation** – Recommends top-rated movies by genre using the MovieLens dataset.
- 🎵 **Music Recommendation** – Recommends music lyrics/songs using the Spotify Millsong dataset based on mood/genre.
- 🤖 **AI Story Generator** – Generates creative stories using the Gemini Pro LLM based on user prompts.
- 🖥️ Interactive web interface with a modern, responsive design using HTML, CSS, and jQuery.

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (jQuery)
- **Backend:** Flask, Python, Pandas
- **AI Integration:** Google Generative AI (Gemini API)
- **Datasets:**
  - `movies.dat`, `ratings.dat`, `users.dat` – [MovieLens 1M Dataset](https://grouplens.org/datasets/movielens/)
  - `spotify_millsongdata.csv` – Spotify lyrics dataset

## 📂 Project Structure


├── app.py # Flask backend with API routes
├── templates/
│ └── index.html # Frontend UI
├── music/
│ └── spotify_millsongdata.csv
├── ml-1m/
│ ├── movies.dat
│ ├── ratings.dat
│ └── users.dat
├── requirements.txt # Python dependencies
└── README.md # Project description


## 📦 Installation & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recommendation-story-app.git
cd recommendation-story-app

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. Install Dependencies
pip install -r requirements.txt

4. Add Your Gemini API Key
Open app.py and replace the API key line:
genai.configure(api_key="YOUR_GEMINI_API_KEY")

5. Run the Flask App
python app.py
Visit http://127.0.0.1:5000 in your browser.

How It Works
Movie Recommendation: Filters movies by genre and ranks them using average user ratings.

Music Recommendation: Matches lyrics containing genre-related keywords.

AI Story: Sends user prompts to the Gemini LLM and displays generated text.

📌 Future Enhancements
🎯 Add user-based collaborative filtering

🎼 Integrate real-time Spotify playback

🌐 Deploy on Render or Heroku

🤝 Credits
MovieLens Dataset – GroupLens

Spotify Millsong Dataset – Kaggle

Google Generative AI API (Gemini)

📄 License
This project is open-source under the MIT License.

---

✅ You can paste this into a `README.md` file in your project folder and push it to GitHub. Let me know if you want me to create the file again for download when the system is stable.
