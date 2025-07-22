books = [
    ["The Hobbit", "J.R.R. Tolkien", "Fantasy"],
    ["1984", "George Orwell", "Dystopian, Science Fiction"],
    ["To Kill a Mockingbird", "Harper Lee", "Fiction, Drama"],
    ["The Fellowship of the Ring", "J.R.R. Tolkien", "Fantasy, Adventure"],
    ["Brave New World", "Aldous Huxley", "Dystopian, Science Fiction"],
    ["Pride and Prejudice", "Jane Austen", "Romance, Classic Literature"],
]

# Define a function to filter books by genre
def filter_books_by_genre(target_genre):
    matching_books = []  # Create an empty list to store results

    # Loop through each book in the list
    for book in books:
        genre_string = book[2]  # The genre field (may contain multiple genres)

        # TODO: Split genre_string by comma into a list of genres
        genre_list = genre_string.split(",")
        # TODO: Loop through each genre in the list
        for genre in genre_list:
            # TODO: Strip spaces and compare it (lowercase) with target_genre (also lowercase)
            genre = genre.strip()
            if genre.lower() == target_genre.lower():
            # TODO: If there's a match, add the book to matching_books and break
                matching_books.append(book)
                break

    return matching_books


# Example usage
results = filter_books_by_genre("Science Fiction")

# Print the matching books
for book in results:
    print(f"{book[0]} by {book[1]} — {book[2]}")