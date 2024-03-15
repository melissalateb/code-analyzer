# scorer.py
import re

def evaluate_indentation(code):
    # Simplified check for 4 spaces indentation
    return 1 if all(line.startswith('    ') or line == '' for line in code.split('\n')[1:]) else 0

def evaluate_camel_case(code):
    # Check for camelCase in variable names and class names (very simplified version)
    camel_case_pattern = re.compile(r'\b[a-z]+([A-Z][a-z]+)*\b')
    return 1 if camel_case_pattern.findall(code) else 0

def evaluate_unnecessary_imports(code):
    # This requires parsing and is complex to do accurately without a full JS parser
    # Returning a default value for demonstration purposes
    return 1

def evaluate_private_attributes_and_getters_setters(code):
    # Simplified check for _private convention and existence of getters/setters
    if "_private" in code and ("get" in code or "set" in code):
        return 1
    return 0

def evaluate_hardcoded_values(code):
    # Check for hardcoded values (very simplified)
    if re.findall(r'const [A-Z_]+ = ', code):
        return 1
    return 0

def evaluate_code_comments(code):
    # Check for block comments
    return 1 if "/*" in code and "*/" in code else 0

def evaluate_file_length(code):
    # Check if the code has less than 200 lines
    return 1 if len(code.split('\n')) < 200 else 0

def scoring(code):
    scores = {
        'indentation': evaluate_indentation(code),
        'camelCase': evaluate_camel_case(code),
        'unnecessary_imports': evaluate_unnecessary_imports(code),
        'private_attributes_getters_setters': evaluate_private_attributes_and_getters_setters(code),
        'hardcoded_values': evaluate_hardcoded_values(code),
        'code_comments': evaluate_code_comments(code),
        'file_length': evaluate_file_length(code)
    }
    # Calculate total score based on criteria met
    total_score = sum(scores.values()) / len(scores) * 10  # Normalize to score out of 10
    return total_score, scores

def detailed_score_report(code):
    total_score, scores = scoring(code)
    report = f"Total Score: {total_score}/10\n"
    for criteria, score in scores.items():
        report += f"{criteria}: {'Pass' if score else 'Fail'}\n"
    return report
