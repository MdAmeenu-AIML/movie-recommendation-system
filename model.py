import pandas as pd

# Load dataset
df = pd.read_csv("movies.csv")

# User input
movie = input("Enter a movie name: ")

# Find movie
result = df[df["movie"].str.lower() == movie.lower()]

if not result.empty:

    print("\nRecommended Movies:")

    print("-", result.iloc[0]["recommendation1"])
    print("-", result.iloc[0]["recommendation2"])
    print("-", result.iloc[0]["recommendation3"])

else:
    print("Movie not found")
