
# Word Similarity Analysis with spaCy

This repository contains Python code for analyzing word similarity using spaCy's pre-trained models. In this README, we will walk through the code and discuss interesting observations and differences between models.

## Code Overview

The code provided in this repository demonstrates how to use spaCy to calculate similarity scores between words and sentences. Here's a brief overview of what each section of the code does:

### Word Similarity Analysis

In this section of the code, we load spaCy's medium-sized English language model (`en_core_web_md`) and calculate similarity scores between the words "cat," "monkey," and "banana." We then print out these similarity scores.

### Token Similarity Analysis

This part of the code tokenizes a given sentence into words and calculates similarity scores between all pairs of tokens in the sentence. The results are printed to the console.

### Sentence Similarity Analysis

Here, we compare the similarity of a reference sentence ("Why is my cat on the car") with a list of other sentences. We calculate similarity scores for each sentence and print the results.

## Interesting Observations

Here are the code observations:

- The similarities between 'cat,' 'monkey,' and 'banana' reveal that the model understands some semantic relationships.
- 'cat' and 'monkey' have a lower similarity compared to 'cat' and 'banana,' indicating that the model captures that 'cat' and 'monkey' are less related than 'cat' and 'banana.'
- 'banana' and 'monkey' have a higher similarity, likely due to the association that monkeys often eat bananas.

## Differences between Models

The code also highlights differences between spaCy's 'en_core_web_md' and 'en_core_web_sm' models:

- The similarity scores are generally lower in 'en_core_web_sm,' indicating that the simpler model might have less nuanced semantic understanding.
- Some nuanced relationships captured by 'en_core_web_md' might not be well-represented in 'en_core_web_sm.'
- While 'en_core_web_md' might capture more subtle relationships like 'banana' and 'monkey' due to eating habits, 'en_core_web_sm' might not capture such relationships as effectively.

## Getting Started

To run this code locally and explore word and sentence similarity using spaCy, follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have Python and spaCy installed. You can install spaCy and the 'en_core_web_md' model using the following command:
   ```
   pip install spacy
   python -m spacy download en_core_web_md
   ```

3. Run the code provided in this repository to analyze word and sentence similarity.

Feel free to modify the code and experiment with your own words and sentences.

---

**Note**: This README provides an overview of the code and its functionality. For a more detailed explanation and usage, please refer to the code comments and documentation within the code files.

```

You can create a new README.md file in your GitHub repository and paste this content into it. Make sure to replace the existing README.md file if you have one. This README provides a clear explanation of the code and its purpose, making it easier for others to understand and use your repository.



# Movie Recommendation with spaCy

This repository contains a Python script for recommending movies based on user-provided descriptions. In this README, we will walk through the code and explain how to use it to get movie recommendations.

## Code Overview

The code provided in this repository uses spaCy's pre-trained model ('en_core_web_md') to recommend movies based on user-provided descriptions. Here's a brief overview of how the code works:

1. It loads the spaCy language model ('en_core_web_md').

2. Reads movie descriptions from the 'movies.txt' file.

3. Defines a function `recommend_movie(user_description)` that takes a user's description as input and returns the most similar movie from the dataset.

4. Inside the `recommend_movie` function, it processes the user's input description and then compares it to each movie description in the dataset.

5. It keeps track of the highest similarity score and updates the most similar movie.

6. Finally, it returns the title of the most similar movie as a recommendation.

## Getting Started

To run this movie recommendation script locally and get personalized movie recommendations, follow these steps:

1. Clone this repository to your local machine.

2. Ensure you have Python and spaCy installed. You can install spaCy and the 'en_core_web_md' model using the following command:
   ```
   pip install spacy
   python -m spacy download en_core_web_md
   ```

3. Create a 'movies.txt' file and populate it with movie descriptions. Each description should be on a separate line, formatted as follows:
   ```
   Movie Title - Movie Description
   ```
   Example:
   ```
   Avengers: Endgame - After the devastating events of Avengers: Infinity War, the universe is in ruins...
   ```

4. Run the script and provide a user description as input to receive a movie recommendation. For example:
   ```
   python movie_recommendation.py "A group of friends embark on an epic adventure..."

5. The script will return the title of the recommended movie.

Feel free to customize the 'movies.txt' file with your own movie descriptions for a personalized movie recommendation experience.

## Example Usage

Here's an example of how to use the script:

```python
user_input = "Will he save their world or destroy it? When the Hulk becomes too dangerous..."

recommended_movie = recommend_movie(user_input)
print("Recommended Movie:", recommended_movie)
```

---

**Note**: This README provides an overview of the code and its functionality. For more details and usage instructions, please feel free to get in touch with me in this platform.

```

You can create a new README.md file in your GitHub repository for the movie recommendation script and paste this content into it. This README will help users understand how to use your script and get movie recommendations based on their descriptions.
