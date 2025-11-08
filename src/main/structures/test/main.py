# vulnerable/python_vuln.py
# INTENTIONAL: demonstrates insecure use of eval() for CodeQL testing only.
def handle_request(query_param):
    # Simulate taking an untrusted value and evaluating it — insecure!
    # DO NOT use eval() on untrusted input in real code.
    result = eval(query_param)
    return result

if __name__ == "__main__":
    # Example: run as `python vulnerable/python_vuln.py "1+2"`
    import sys
    if len(sys.argv) > 1:
        print(handle_request(sys.argv[1]))
