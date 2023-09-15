import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_md')

# Read movie descriptions from the file
with open('movies.txt', 'r', encoding='utf-8') as file:
    movie_descriptions = [line.strip() for line in file]

def recommend_movie(user_description):
    # Process user's input description
    user_doc = nlp(user_description)

    # Initialize variables to track highest similarity
    max_similarity = 0
    most_similar_movie = None

    # Compare user's description with each movie description
    for movie_description in movie_descriptions:
        movie_doc = nlp(movie_description)
        similarity = user_doc.similarity(movie_doc)

        # Update the most similar movie if similarity is higher
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_description.split(' - ')[0]  # Extract movie title

    return most_similar_movie

# Example usage
user_input = "Will he save their world or destroy it? When the Hulk becomes too dangerous..."

recommended_movie = recommend_movie(user_input)
print("Recommended Movie:", recommended_movie)
