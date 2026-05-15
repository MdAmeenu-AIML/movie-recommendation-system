# 🎬 Movie Recommendation System

An AI-powered Movie Recommendation System built using Python, Machine Learning, NLP, and Streamlit.  
This project recommends similar movies based on movie descriptions using cosine similarity and text vectorization techniques.

---

## 🚀 Live Demo

[Open Web App](https://movie-recommendation-system-dyc6h8za9hnyhytyzvzpej.streamlit.app/)

---

## 📌 Features

- Recommends similar movies instantly
- Uses Natural Language Processing (NLP)
- Real-world TMDB movie dataset
- Machine Learning recommendation engine
- Cosine similarity algorithm
- Interactive Streamlit web app
- Modern dark-themed UI

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- NLP (Natural Language Processing)

---

## 📂 Project Structure

```txt
movie-recommendation-system/
│
├── app.py
├── model.py
├── tmdb_5000_movies.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset used:

TMDB 5000 Movie Dataset from Kaggle.

The dataset contains:
- Movie titles
- Movie overviews
- Genres
- Metadata

---

## 🤖 Machine Learning Workflow

1. Load movie dataset
2. Clean and preprocess text data
3. Convert movie overviews into vectors using CountVectorizer
4. Calculate cosine similarity between movies
5. Recommend similar movies based on similarity scores
6. Display recommendations using Streamlit

---

## 🧠 AI Concepts Used

- Recommendation Systems
- NLP (Natural Language Processing)
- CountVectorizer
- Cosine Similarity
- Content-Based Filtering

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/MdAmeenu-AIML/movie-recommendation-system.git
```

### Open Project Folder

```bash
cd movie-recommendation-system
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎥 Example Recommendations

### Input

```txt
Avatar
```

### Recommended Movies

```txt
Aliens
Guardians of the Galaxy
Star Trek
John Carter
```

---

## 📈 Project Versions

| Version | Features |
|---|---|
| V1 | Hardcoded recommendations |
| V2 | CSV dataset integration |
| V3 | Real TMDB dataset |
| V4 | Cosine similarity engine |
| V5 | Streamlit web app |
| V6 | Online deployment |

---

## 📚 Learning Outcomes

This project helped learn:

- Recommendation Systems
- NLP basics
- Text vectorization
- Cosine similarity
- Real-world dataset handling
- Streamlit deployment
- Machine Learning workflow

---

## 👨‍💻 Author

Mohammed Ameen ul Aman

AI & ML Beginner Projects 🚀
