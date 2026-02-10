# Subject-Verb Agreement Checker using CFG

def check_agreement(sentence):
    words = sentence.split()

    singular_nouns = ['cat', 'dog', 'boy']
    plural_nouns = ['cats', 'dogs', 'boys']
    singular_verbs = ['is', 'runs']
    plural_verbs = ['are', 'run']

    subject = words[1]
    verb = words[2]

    if subject in singular_nouns and verb in singular_verbs:
        return "Agreement Correct"
    elif subject in plural_nouns and verb in plural_verbs:
        return "Agreement Correct"
    else:
        return "Agreement Incorrect"


sentence = "The boys run"
print(check_agreement(sentence))
