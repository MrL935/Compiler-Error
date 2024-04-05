import nltk
import string
from nltk.chat.util import Chat, reflections
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Necessary NLTK resources 
#nltk.download('punkt')


# Defines stopwords and punctuation for pre-processing
stopWords = set(stopwords.words('english') + list(string.punctuation))


# Preprocessing and word tokenization
def preProcessing(text):
    tokens = word_tokenize(text.lower()) # Breaks text into individual words    
    filteredWords = [token for token in tokens if token not in stopWords]
    return ' '.join(filteredWords)

training_data = [
    ("What is your name?", "I'm Azi, your virtual assistant."),
    ("Company policies", "Here are the company policies."),
    ("How much PTO time do I have left?", ""),
    ("How are you?", "I'm doing fine, thanks for asking!"),
    ("Clock in", "Please provide first name, followed by your last name."),
    ("What is the process for submitting a leave request?", "You can submit a leave request through the company portal. Here's the link: [link to leave request portal]. You'll need to enter your details, leave type, and desired dates. Once submitted, your manager will review and approve your request."),
    ("What are my bhealth insurance options?",
      "You can find a detailed breakdown of your helaht insurance options on the following link: [link to benefits page]."
     ),
]


def extract_features(sentence):
    words = word_tokenize(sentence.lower())
    # Replace with your feature extraction logic based on NLTK or other methods
    features = {}
    vocabulary = set(  # Replace with your vocabulary if you have a predefined list
      ["what", "is", "your", "name", "company", "policies", "PTO", "time", "clock",
       "in", "submit", "leave", "request", "portal", "health", "insurance", "options"]
    )
    # ... (extract features from the sentence)
    for word in set(words):
        features[word] = (word in words)
    return features



def get_chatbot_response(user_input):
    preprocessed_user_input = preProcessing(user_input)
    if greetings_check(preprocessed_user_input):
        return "Hi there"
    
    # Feature extraction (replace with your logic)
    features = extract_features(preprocessed_user_input)  # Replace with feature extraction function
    classifier = NaiveBayesClassifier()
  # Classify user input using the trained classifier
    try:
        response = classifier.classify(features)
    except Exception as e:
        print(f"Error during classification: {e}")
        return "Sorry, I am having some trouble understanding you. Can you rephrase your question?"

  # Check classifier confidence (optional)
    if classifier.classify_prob(features)[response] < 0.7:
        return "Sorry, I don't understand. Can you rephrase that?"
    else:
    # Return answer from training data based on classification
        return training_data[response][1]
    


def greetings_check(message):
    greetings = ["hello", "hi", "hey", "good morning", "good evening", "good afternoon", "howdy", "what's up"]

    import re
    greeting_pattern = r"\b(hi|hello|hey|good(morning|afternoon|evening)\b( |,)?\w+\b"
    match = re.search(greeting_pattern, message, re.IGNORECASE)
    return match is not None
