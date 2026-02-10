# Simple Earley Parser Implementation

def earley_parser(words):
    grammar = {
        'S': [('NP', 'VP')],
        'NP': [('Det', 'N')],
        'VP': [('V', 'NP')],
        'Det': [('the',), ('a',)],
        'N': [('cat',), ('dog',)],
        'V': [('chased',), ('saw',)]
    }

    chart = [set() for _ in range(len(words) + 1)]
    chart[0].add(('S', (), grammar['S'][0], 0))

    for i in range(len(words) + 1):
        for state in list(chart[i]):
            lhs, seen, unseen, origin = state

            if unseen:
                next_sym = unseen[0]
                if next_sym in grammar:
                    for prod in grammar[next_sym]:
                        chart[i].add((next_sym, (), prod, i))
                elif i < len(words) and next_sym == words[i]:
                    chart[i + 1].add((lhs, seen + (next_sym,), unseen[1:], origin))
            else:
                for st in chart[origin]:
                    if st[2] and st[2][0] == lhs:
                        chart[i].add((st[0], st[1] + (lhs,), st[2][1:], st[3]))

    return any(state[0] == 'S' and not state[2] and state[3] == 0 for state in chart[len(words)])


sentence = "the cat chased the dog".split()
print("Earley Parse Result:", earley_parser(sentence))
