import os

def main():
    x = os.getenv("X")
    if not x:
        raise ValueError("Environment variable 'X' is not set.")
    output = f"Hello, {x}!"
    print(output)

if __name__ == "__main__":
    main()