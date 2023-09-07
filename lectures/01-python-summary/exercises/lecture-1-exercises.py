

# 2.7 a)
def generate_coordinates(a, b, n):
    """Generate n+1 equally spaced coordinates between a and b using for loop."""
    h = (b - a) / n
    coords = []
    for i in range(n + 1):
        xi = a + i * h
        coords.append(xi)
    return coords

# 2.7 b)
def generate_coordinates_comprehension(a, b, n):
    """Generate n+1 equally spaced coordinates between a and b using list comprehension."""
    h = (b - a) / n
    return [a + i * h for i in range(n + 1)]

# 2.8 a)
def print_table(v0, g, n):
    """Prints a table of t and y(t) values using for loop."""
    for i in range(n + 1):
        t = 2 * v0 / g * i / n
        y = v0 * t - 0.5 * g * t ** 2
        print(f"{t:.2f}\t{y:.2f}")

# 2.8 b)
def print_table_while(v0, g, n):
    """Prints a table of t and y(t) values using while loop."""
    i = 0
    while True:
        t = 2 * v0 / g * i / n
        y = v0 * t - 0.5 * g * t ** 2
        print(f"{t:.2f}\t{y:.2f}")
        if i == n:
            break
        i += 1

# 2.9 a)
def store_in_lists(v0, g, n):
    """Stores t and y(t) in two lists and prints a table."""
    t_values = []
    y_values = []
    for i in range(n + 1):
        t = 2 * v0 / g * i / n
        y = v0 * t - 0.5 * g * t ** 2
        t_values.append(t)
        y_values.append(y)
        
    for t, y in zip(t_values, y_values):
        print(f"{t:.2f}\t{y:.2f}")
