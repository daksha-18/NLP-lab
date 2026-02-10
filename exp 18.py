import re

def parse_fopc(expression):
    pattern = r"(\w+)\(([\w,]+)\)"
    match = re.match(pattern, expression)

    if match:
        predicate = match.group(1)
        arguments = match.group(2).split(",")
        return predicate, arguments
    else:
        return "Invalid Expression"

expr = "Likes(John,Mary)"
print(parse_fopc(expr))
