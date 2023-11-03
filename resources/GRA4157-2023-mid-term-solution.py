import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1a)
def a1_reverse_list(input_list=[1, 2, 3]):
    reversed_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list


# 1b)
def b1_list_to_dict(tuple_list=[("a", 1),("b", 2),("c", 3)]):
    result_dict = {}
    for tup in tuple_list:
        result_dict[tup[0]] = tup[1]
    return result_dict


# 1c)
def c1_max_value_key(input_dict={"a": 1, "b": 2, "c": 3}):
    if not input_dict:
        return None

    max_value = max(input_dict.values())
    for key, value in input_dict.items():
        if value == max_value:
            return key


# 1d)
def d1():
    list_of_values = [1, 2, -5, 3, 12, 20, 45, 13, -10, 21]
    print(list_of_values[1:3] + list_of_values[4:6])
    print(list_of_values[-1] + list_of_values[6])
    print(list_of_values[8] * 2)
    print(list_of_values[4::2])

# 2a)
def a2(path):
    rows = []
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            row = []
            values = line.strip().split(",")
            for value in values:
                try:
                    num = float(value)
                    row.append(num)
                except ValueError:
                    continue
            rows.append(row)
    return rows

# 2b)
def b2(path):
    columns = [[] for _ in range(4)]
    with open(path) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            values = line.strip().split(",")
            for value in values:
                try:
                    num = float(value)
                    columns[i].append(num)
                except ValueError:
                    continue
    return columns

# 2c)
def c2(path, output="out.csv"):
    rows = a2(path)
    with open(path, 'r') as infile:
        header = infile.readline().strip()
    with open(output, 'w') as outfile:
        outfile.write(header + '\n')
        for row in rows:
            outfile.write(','.join(str(v * 10) for v in row if v is not None) + '\n')


# 3a)
def a3():
    matrix_a = np.array([[2, 5, 1],
                        [11, 6, 8],
                        [3, 34, 5]])

    matrix_b = np.array([[2, 9, 7],
                        [4, 6, 5],
                        [-6, 27, 5]])
    return matrix_a, matrix_b


def b3():
    
    matrix_a, matrix_b = a3()

    # Perform element-wise addition and subtraction
    result_addition = matrix_a + matrix_b
    result_subtraction = matrix_a - matrix_b

    # Print the results
    print("Element-wise Addition:\n", result_addition)
    print("Element-wise Subtraction:\n", result_subtraction)


def c3():
    def f(a, b):
        print(a, b)
        if a == b:
            return a - b
        return a + b

    matrix_a, matrix_b = a3()
    
    try:
        print(f(matrix_a, matrix_b))
    except Exception as e:
        print(e)
        
    f = np.vectorize(f)
    
    return f(matrix_a, matrix_b)

# 4a)
def a4():
    url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    movies = pd.read_html(url)[0]
    return movies

# 4b)
def b4():

    movies = a4()
    movies = movies.sort_values('Worldwide gross', ascending=False)
    movies = movies.drop_duplicates(subset='Year')
    movies = movies.sort_values('Year', ascending=False)

    return movies

# 4c)
def c4():

    def remove_non_numeric(df, column_name):
        df[column_name] = df[column_name].apply(lambda x: x.split("$")[1].replace(",", ""))
        df[column_name] = df[column_name].astype(int)
        return df
    
    movies = b4()

    movies = remove_non_numeric(movies, "Worldwide gross")
    movies.sort_values("Year", ascending=False, inplace=True)
    
    movies.plot(x="Year", y="Worldwide gross", kind="scatter")
    plt.show()

a1_reverse_list()
b1_list_to_dict()
c1_max_value_key()
d1()
a2("file.txt")
b2("file.txt")
c2("file.txt")
b3()
c3()
a4()
b4()
c4()
