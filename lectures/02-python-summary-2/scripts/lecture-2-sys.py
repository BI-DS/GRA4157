import sys
name = sys.argv[1]
if len(sys.argv)>2:
    age = sys.argv[2]
print(f"Hello {name}")
if len(sys.argv)>2:
    print(f"You are {age} years old")