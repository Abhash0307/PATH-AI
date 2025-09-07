# PATH-AI

PathAI 🎯
AI-Powered Career Coach and Job Discovery Platform

📽️ Demo Video
Watch the full demo here: YouTube Demo

🚀 Overview
PathAI is an intelligent web-based platform that:

Analyzes resumes using NLP (spaCy) to recommend the most suitable job roles.
Offers personalized feedback for improvement.
Generates mock interview questions in real-time using Gemini AI.
Facilitates job discovery with curated listings via RapidAPI.
Includes a live AI Career Coach for instant guidance.
🔑 Features
✅ Resume Parsing & Analysis — Processes 500+ resumes with 85% accuracy in job-role matching.
🧠 AI Career Coach — Provides real-time, personalized career advice using Gemini API.
🎤 Mock Interviews — Generates 10+ tailored interview questions with a live proctoring setup.
🔎 Job Discovery — Fetches and filters 100+ job listings based on skills, location, and job type.
📋 Resume Feedback — Offers targeted suggestions to improve CVs.
🛠️ Tech Stack
Category	Technologies
Frontend	Streamlit
Backend	Flask
AI & NLP	Gemini API, spaCy
APIs	RapidAPI (job listings, career tips)
Database	Firebase
Deployment	Streamlit Cloud / Localhost
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/pathai.git cd pathai 2. Install Dependencies bash Copy Edit pip install -r requirements.txt 3. Add Environment Variables Create a .env file and include:

env Copy Edit GEMINI_API_KEY=your_key FIREBASE_CREDENTIALS=your_credentials.json RAPIDAPI_KEY=your_key 4. Run the App

streamlit run app/main.py 🧠 Built With Google Gemini API

spaCy

RapidAPI

Streamlit

Flask

Firebase

🤝 Contributing Contributions are welcome! If you find a bug or want to suggest a feature:

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature-name)

Open a pull request

