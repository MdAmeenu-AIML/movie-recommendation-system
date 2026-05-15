import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: #FF4B4B;
    font-size: 50px;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    padding: 10px;
}

.stButton > button {
    width: 100%;
    background-color: #FF4B4B;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stButton > button:hover {
    background-color: #ff1e1e;
    color: white;
}

.movie-box {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: white;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🎬 Movie Recommendation System")

st.markdown(
    "<h4 style='text-align:center; color:lightgray;'>AI-powered movie recommendations using Machine Learning</h4>",
    unsafe_allow_html=True
)

# Load dataset
df = pd.read_csv("tmdb_5000_movies.csv")

# Keep useful columns
df = df[["title", "overview"]]

# Remove missing values
df = df.dropna()

# Convert text into vectors
vectorizer = CountVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["overview"])

# Similarity matrix
similarity = cosine_similarity(X)

# User input
movie = st.text_input("🍿 Enter a movie name")

# Recommendation button
if st.button("Recommend Movies"):

    movie_index = df[
        df["title"].str.lower() == movie.lower()
    ].index

    if len(movie_index) > 0:

        index = movie_index[0]

        similarity_scores = list(
            enumerate(similarity[index])
        )

        sorted_movies = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        st.subheader("✨ Recommended Movies")

        for movie in sorted_movies[1:6]:

            movie_title = df.iloc[movie[0]]["title"]

            st.markdown(
                f"<div class='movie-box'>🎥 {movie_title}</div>",
                unsafe_allow_html=True
            )

    else:
        st.error("❌ Movie not found")
