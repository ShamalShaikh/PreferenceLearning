import nltk
from nltk import word_tokenize
import os

print(nltk.__path__)

# Ensure the nltk_data path is explicitly set
nltk.data.path.append('/Users/shamalshaikh/nltk_data')

# Download the 'punkt' tokenizer if not already downloaded
try:
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    print("Punkt tokenizer loaded successfully!")
except LookupError:
    print("Punkt tokenizer not found. Downloading...")
    nltk.download('punkt', download_dir='/Users/shamalshaikh/nltk_data')


# Define a simple mapping from natural language phrases to LTL formulas
phrase_to_ltl = {
    "eventually": "F",
    "always": "G",
    "next": "X",
    "until": "U",
    "and": "&&",
    "or": "||",
    "not": "!",
}

def nl_to_ltl(natural_language):
    tokens = word_tokenize(natural_language.lower())
    ltl_formula = ""
    
    for token in tokens:
        ltl_formula += phrase_to_ltl.get(token, token.upper()) + " "

    return ltl_formula.strip()
    
    # i = 0

    # while i < len(tokens):
    #     token = tokens[i]

    #     if token in phrase_to_ltl:
    #         ltl_formula += f"{phrase_to_ltl[token]} "
    #     elif token == "(" or token == ")":
    #         ltl_formula += f"{token} "
    #     else:
    #         # Assume any other token is a proposition or variable
    #         ltl_formula += f"{token.upper()} "
    #     i += 1

    # return ltl_formula.strip()

# Example usage
if __name__ == "__main__":
    natural_language_input = "eventually A and always B"
    ltl_output = nl_to_ltl(natural_language_input)
    print(f"Natural Language Input: {natural_language_input}")
    print(f"LTL Output: {ltl_output}")
