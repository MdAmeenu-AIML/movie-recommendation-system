import pandas as pd

# Load dataset
df = pd.read_csv("tmdb_5000_movies.csv")

# Keep useful columns
df = df[["title", "overview"]]

# Remove missing values
df = df.dropna()

# User input
movie = input("Enter a movie name: ")

# Find movie
result = df[df["title"].str.lower() == movie.lower()]

if not result.empty:

    print("\nMovie Found!")
    print("\nOverview:\n")

    print(result.iloc[0]["overview"])

else:
    print("Movie not found")
