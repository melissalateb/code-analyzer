from parser_1 import tokenize
from parser_1 import parse
from analyzer import scoring

def evaluate_code(code):
    tokens = list(tokenize(code))
    ast = parse(tokens)
    total_score, scores = scoring(code)
    print(f"Total Score: {total_score}/10")
    for criteria, score in scores.items():
        print(f"{criteria}: {score}/10")

if __name__ == "__main__":
    with open("test.js", "r") as file:
        code = file.read()
        evaluate_code(code)
