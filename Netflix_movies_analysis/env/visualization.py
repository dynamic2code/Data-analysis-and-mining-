import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('env/netflix_titles.csv')

def basic_Visualization():
    """
    shows the general information about the dataset
    """
    # Display the first few rows of the DataFrame
    print(df.head())

    # Get summary statistics of the DataFrame
    print(df.describe())

    # Check the column names
    print(df.columns)

def  movie_categorization():
    """
    gives insight of how movies have been produced and tries to find any patten
    """

    #how many movies have been produced in each year

    # Convert 'release_year' column to numeric type 
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    # Group the data by 'release_year' and count the number of occurrences
    movies_per_year = df['release_year'].value_counts()
    # Sort the result by year
    movies_per_year = movies_per_year.sort_index()
    # Print the number of movies produced in each year
    print(movies_per_year)

    #what genre there is and their numbers

    # Get the unique types
    unique_types = df["type"].unique()

    # Count the number of shows for each type
    type_counts = {}
    for type in unique_types:
        type_counts[type] = df[df["type"] == type].shape[0]

    # Print the results
    print(type_counts)

    #getting categories 
    # Split the listed_in column into a list of categories
    categories = df["listed_in"].str.split(", ")

    # Flatten the list of lists
    categories = [category for sublist in categories for category in sublist]

    # Get the unique categories
    unique_categories = set(categories)

    # Print the results
    print(unique_categories)



# basic_Visualization()
movie_categorization()


