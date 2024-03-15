import re

def evaluate_indentation(code):
    """Evaluate code indentation."""
    return 10 if all(line.startswith('    ') or line == '' for line in code.split('\n')[1:]) else 0

def evaluate_camel_case(code):
    """Evaluate camelCase usage."""
    camel_case_pattern = re.compile(r'\b[a-z]+([A-Z][a-z]+)*\b')
    return 10 if camel_case_pattern.findall(code) else 0

# Add more detailed scoring functions here...

def scoring(code):
    """Score the code based on various criteria."""
    scores = {
        'indentation': evaluate_indentation(code),
        'camelCase': evaluate_camel_case(code),
        # Add other evaluations here...
    }
    total_score = sum(scores.values()) / len(scores)
    return total_score, scores
