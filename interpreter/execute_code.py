import sys

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    code = sys.stdin.read()
    execute_code(code)