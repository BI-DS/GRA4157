import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="This is a simple example.")

# Add arguments
parser.add_argument("name", help="Your name")
parser.add_argument("-a", "--age", help="Your age", type=int, default=0)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
