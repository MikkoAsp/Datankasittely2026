import pandas as pd

def load_data(filepath):
    df = pd.read_csv("data/books.csv")
    return df

def get_unique_genres(df):
    uniqueList = df["genre"].unique().tolist()
    return uniqueList 

def find_books_by_author(df, author_name):
    filteredByAuthor = df[df['author'] == author_name]
    return filteredByAuthor 

def get_highest_rating(df):
    highestRating = df["rating"].max()
    return highestRating

if __name__ == "__main__":
    df = load_data('data/books.csv')

    print("\n--- Task 1 ---\n")
    print(df)
    
    print("\n--- Task 2 ---\n")
    print(get_unique_genres(df))

    print("\n--- Task 3 ---\n")
    print(find_books_by_author(df, "George Orwell"))

    print("\n--- Task 4 ---\n")
    print(get_highest_rating(df))