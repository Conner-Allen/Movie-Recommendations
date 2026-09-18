"""
Movie Recommendations List Program
Author: Conner Allen
Version: 1.0

Description:
This program allows users to add movies to a recommendation list,
display the list, and exit the program. It prevents duplicate entries,
formats titles in Title Case, and validates user input.
"""

def display_menu():
    """Displays the main menu options"""
    print("\nPlease choose one of the following options:")
    print("1. Add a movie to the list")
    print("2. Display the movie recommendations")
    print("3. Exit")


def main():
    # Initialize empty list to store movie recommendations
    movie_list = []

    print("Welcome to the Movie Recommendations Program!")

    # Loop until the user chooses to exit
    while True:
        display_menu()

        # INPUT: Get user's menu choice
        choice = input("\nEnter your choice: ")

        # PROCESSING: Handle menu choices
        if choice == "1":
            # INPUT: Get movie name
            movie = input("Enter the name of the movie: ").strip()

            # Convert to Title Case
            movie = movie.title()

            # PROCESSING: Check for duplicates
            if movie in movie_list:
                print(f"'{movie}' is already in the list!")
            else:
                movie_list.append(movie)
                print(f"'{movie}' has been added to the list.")

        elif choice == "2":
            # OUTPUT: Display movie recommendations
            print("\nMovie Recommendations:")

            if len(movie_list) == 0:
                print("No movies in the list yet.")
            else:
                for index, movie in enumerate(movie_list, start=1):
                    print(f"{index}. {movie}")

        elif choice == "3":
            # OUTPUT: Exit message
            print("\nExiting the program. Goodbye!")
            break

        else:
            # INPUT VALIDATION: Handle invalid choices
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
