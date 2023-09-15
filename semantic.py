import spacy

# Load the medium-sized English language model with word vectors
nlp = spacy.load('en_core_web_md')

# Create word objects for the given words
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Print the similarity scores between the words
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)

    print(sentence + " - " + str(similarity))           #convert similarity to a string


                            # Note: Interesting Observations

# The similarities between 'cat,' 'monkey,' and 'banana' reveal that the model understands some semantic relationships:

# - 'cat' and 'monkey' have a lower similarity compared to 'cat' and 'banana,' indicating that the model captures that 'cat' and 'monkey' are less related than 'cat' and 'banana.'
# - 'banana' and 'monkey' have a higher similarity, likely due to the association that monkeys often eat bananas.
# - An additional example: 'apple' and 'banana' might have a similarity due to their common fruit category, although they're not as closely related as 'banana' and 'monkey.'


                            # Note: Differences between Models
# After running the example code with the 'en_core_web_sm' model, I noticed the following differences compared to 'en_core_web_md':

# - The similarity scores are generally lower in 'en_core_web_sm,' indicating that the simpler model might have less nuanced semantic understanding.
# - Some nuanced relationships captured by 'en_core_web_md' might not be well-represented in 'en_core_web_sm.'
# - While 'en_core_web_md' might capture more subtle relationships like 'banana' and 'monkey' due to eating habits, 'en_core_web_sm' might not capture such relationships as effectively.
# - Overall, 'en_core_web_md' seems to offer more accurate and detailed similarity assessments than 'en_core_web_sm.'
