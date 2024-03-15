# parser.py
import re


def tokenize(code):
    print(code)
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r'='),            # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*\/]'),     # Arithmetic operators
        ('DOT',      r'\.'),           # Dot operator
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'SKIP':
            continue
        # elif kind == 'MISMATCH':
        #     raise RuntimeError(f'{value}: unexpected character')
        yield {'type': kind, 'value': value}

def parse(tokens):
    print(tokens)
    """Parses tokens into a simple AST. Each node in the AST is a dict."""
    ast = []
    for token in tokens:
        # Example: simple parsing logic to create an AST node for each token
        ast.append({'type': 'Node', 'token': token})
    return ast
