# Transformation-Based POS Tagging

def transformation_based_tagger(sentence):
    words = sentence.split()

    # Initial tagging (default NN)
    tags = ['NN' for _ in words]

    # Transformation rules
    for i, word in enumerate(words):
        if word.endswith('ing'):
            tags[i] = 'VBG'
        if word.endswith('ed'):
            tags[i] = 'VBD'
        if word.lower() in ['is', 'are', 'was', 'were']:
            tags[i] = 'VB'

    return list(zip(words, tags))


sentence = "He is playing cricket"
print(transformation_based_tagger(sentence))
