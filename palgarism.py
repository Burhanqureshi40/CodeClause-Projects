import difflib

def calculate_similarity(text1, text2):
    # Convert the texts to lowercase
    text1 = text1.lower()
    text2 = text2.lower()

    # Split the texts into individual words
    words1 = text1.split()
    words2 = text2.split()

    # Calculate the similarity using the SequenceMatcher class from difflib
    matcher = difflib.SequenceMatcher(None, words1, words2)
    similarity = matcher.ratio() * 100

    return similarity

# Example usage
text1 = "This is a sample text to check plagiarism."
text2 = "This is another text for plagiarism checking."

similarity_percentage = calculate_similarity(text1, text2)
print(f"Similarity: {similarity_percentage}%")
