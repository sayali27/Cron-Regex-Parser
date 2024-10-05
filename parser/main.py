import sys

from parser.output import output_values
from parser.parser import parse_expression

def main():
    args = sys.argv[1:]
    if len(args) > 1:
        raise ValueError("Sorry, please enter only one expression")
    parsed_expr = parse_expression(args.pop())
    output_values(parsed_expr)

if __name__ == '__main__':
    main()