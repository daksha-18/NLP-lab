# Simple Top-Down Parser

grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N': [['cat'], ['dog']],
    'V': [['chased'], ['saw']]
}

def parse(symbol, words):
    if not words:
        return []

    if symbol not in grammar:
        return [[words[1:]]] if words[0] == symbol else []

    results = []
    for rule in grammar[symbol]:
        remainders = [words]
        for sym in rule:
            new_remainders = []
            for rem in remainders:
                parsed = parse(sym, rem)
                for p in parsed:
                    new_remainders.append(p)
            remainders = new_remainders
        results.extend(remainders)
    return results


sentence = "the cat chased the dog".split()
print("Sentence Parsed Successfully:", [] in parse('S', sentence))
