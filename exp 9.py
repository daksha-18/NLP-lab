# Rule-Based POS Tagging using Regular Expressions

import re

def rule_based_pos_tagger(sentence):
    words = sentence.split()
    tagged_words = []

    for word in words:
        if re.match(r'.*ing$', word):
            tag = 'VBG'   # Verb gerund
        elif re.match(r'.*ed$', word):
            tag = 'VBD'   # Verb past tense
        elif re.match(r'.*ly$', word):
            tag = 'RB'    # Adverb
        elif re.match(r'.*ous$|.*ful$|.*able$', word):
            tag = 'JJ'    # Adjective
        elif re.match(r'.*s$', word):
            tag = 'NNS'   # Plural noun
        else:
            tag = 'NN'    # Default noun

        tagged_words.append((word, tag))

    return tagged_words


sentence = "The boys are playing happily"
print(rule_based_pos_tagger(sentence))
