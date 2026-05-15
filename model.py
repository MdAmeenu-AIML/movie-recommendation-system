movies = {
    "Batman": [
        "Batman Begins",
        "The Dark Knight",
        "Man of Steel"
    ],

    "Iron Man": [
        "Avengers",
        "Doctor Strange",
        "Spider-Man"
    ],

    "Titanic": [
        "Avatar",
        "The Notebook",
        "Romeo + Juliet"
    ]
}

movie = input("Enter a movie name: ")

if movie in movies:
    print("Recommended Movies:")

    for recommendation in movies[movie]:
        print("-", recommendation)

else:
    print("Movie not found")