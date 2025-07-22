import csv
import time

# Create a list of movie titles, ratings, and genres
movies = [
    ["Crazy Rich Asians", 6.9, "Comedy, Romance"],
    ["Mean Girls", 7.1, "Comedy, Romance"],
    ["My Neighbor Totoro", 8.1, "Fantasy, Adventure"],
    ["Pitch Perfect", 7.1, "Comedy"],
    ["The Greatest Showman", 7.5, "Musical, Thriller"]
]

def instructions1():
    print("\nWelcome to the Movie Data Explorer!")
    print("\nLoading personal movie list...")
    time.sleep(3)
    print("\nPersonal Movie List:")
    print_movies_list()
    print("\nMenu:")
    print("a - Modify ratings in the list")
    print("b - Access rating analysis")
    while True:
        command = input("\nEnter a letter: ")
        if command == "a":
            modify_ratings()
            print("\nNew List:")
            print_movies_list()
            break
        elif command == "b":
            rating_analysis()
            break
        else:
            print("Invalid input.")

def instructions2():
    print("\nLoading action movie list analysis...")
    time.sleep(10)
    action_movies = load_movies("action.csv")
    action_movie_ratings = [movie[1] for movie in action_movies]
    print("\nAverage Rating:", calculate_average_rating(action_movie_ratings))
    print("Highest Rated:", find_highest_rated(action_movies))

# Access elements in the list
def print_movies_list():
    for movie in movies:
        print("\nTitle:", movie[0])
        print("Rating:", movie[1])
        print("Genre:", movie[2])

# Modify elements in the list
def modify_ratings():
    index = int(input("\nEnter the index of the movie you want to update the rating for: "))
    rating = int(input("Enter the new rating: "))
    movies[index][1] = rating

def rating_analysis():
    print("\nLoading rating analysis...\n")
    time.sleep(3)
    for movie in movies:
        rating = movie[1]
        # Write a conditional statement that checks a movie’s rating and prints a message
        if rating >= 8:
            print(str(movie[0]) + " (" + str(movie[1]) + "): Great movie!")
        elif rating >= 5:
            print(str(movie[0]) + " (" + str(movie[1]) + "): Okay movie.")
        else:
            print(str(movie[0]) + " (" + str(movie[1]) + "): Not worth watching.")
    movie_ratings = [movie[1] for movie in movies]
    print("\nAverage Rating:", calculate_average_rating(movie_ratings))
    print("Highest Rated:", find_highest_rated(movies))

def calculate_average_rating(ratings):
    total = 0
    # Use a loop to calculate the sum of ratings in the list
    for rating in ratings:
        try:
            rating = float(rating)
        except:
            continue
        total += rating
    average_rating = total / len(ratings)
    return average_rating

def find_highest_rated(movies):
    highest_rated = movies[0]
    # Find the highest-rated movie using a loop
    for movie in movies:
        if movie[1] > highest_rated[1]:
            highest_rated = movie
    return highest_rated

def filter_by_genre(movies, target_genre):
    filtered_movies = []
    # Create a loop that filters your movies by genre and stores those movies in a new list
    for movie in movies:
        genre_string = movie[2]
        genre_list = genre_string.split(",")
        for genre in genre_list:
            genre = genre.strip()
            if genre.lower() == target_genre.lower():
                filtered_movies.append(movie)
                break
    return filtered_movies

def load_movies(filename):
    action = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            title = row[1]
            rating = row[6]
            genre = row[5]
            action.append([title, rating, genre])
    return action

def save_analysis(results, filename):
    with open(filename, "w") as file:
        for movie in results:
            file.write(str(movie))

def genre_analysis():
    print("\nLoading genre analysis...")
    time.sleep(10)
    comedy_movies = filter_by_genre(movies, "Comedy")
    print("\nComedy Movies (personal movie list):", comedy_movies)
    action_movies = load_movies("action.csv")
    fantasy_movies = filter_by_genre(action_movies, "Fantasy")
    print("Number of Fantasy Movies (action movie list):", len(fantasy_movies))

def save_filtered_movies():
    print("\nSaving filtered movies...")
    time.sleep(5)
    action_movies = load_movies("action.csv")
    fantasy_movies = filter_by_genre(action_movies, "Fantasy")
    save_analysis(fantasy_movies, "fantasy_movies.txt")
    print("Successfully saved filtered movies.")

instructions1()
instructions2()
genre_analysis()
save_filtered_movies()