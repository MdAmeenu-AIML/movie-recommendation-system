import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
movie = input("Enter a movie name: ")

# Find movie index
movie_index = df[df["title"].str.lower() == movie.lower()].index

if len(movie_index) > 0:

    index = movie_index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[index]))

    # Sort movies
    sorted_movies = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Movies:\n")

    # Show top 5 recommendations
    for movie in sorted_movies[1:6]:

        movie_title = df.iloc[movie[0]]["title"]

        print(movie_title)

else:
    print("Movie not found")
