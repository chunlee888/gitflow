import sys

def main():
    if len(sys.argv) < 2:
        raise ValueError("Input from script1 is required as an argument.")
    input_text = sys.argv[1]
    output = f"Processed: {input_text}"
    print(output)

if __name__ == "__main__":
    main()