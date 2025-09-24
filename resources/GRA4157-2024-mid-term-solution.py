import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1a)
def sort_list(m=[5, 3, -10, 30, 110, -7, 45, 11, 12, -15]):
    sorted_list = []
    while len(m) > 0:
        max_val = m[0]
        max_val_index = 0
        for i in range(len(m)):  # or enumerate
            number = m[i]
            if number > max_val:
                max_val = number
                max_val_index = i
        sorted_list.append(m.pop(max_val_index))

    return sorted_list


# 1b)
def output_calls(m=[5, 3, -10, 30, 110, -7, 45, 11, 12, -15]):
    print(m[2:3] + m[3:6])
    print(m[2] + m[4])
    print(2 * m[8])
    print(2 * m[7:])


# 1c)
def make_nested_dict(
    temps={
        "Oslo": 2.5,
        "London": 12.3,
        "Paris": 11.0,
        "Berlin": 9.0,
        "Los Angeles": 19.5,
        "Cairo": 22.5,
    },
    rainfall={"Oslo": 0.0, "London": 2.2, "Paris": 5.5, "Berlin": 0},
):

    nested_dict = {}
    for city in temps.keys():
        if city in rainfall.keys():
            temperature = temps[city]
            rain = rainfall[city]
            nested_dict[city] = {"temperature": temperature, "rainfall": rain}
    return nested_dict


# 2a)
def read_file(filename="mid-term-data.txt"):
    R = []
    with open(filename, "r") as infile:
        for i in range(3):
            infile.readline()
        for line in infile:
            numbers = line.split()  # optional to convert to numeric
            R.append(numbers)
    row1, row2, row3, row4 = R
    return row1, row2, row3, row4


# 2b)
def read_and_reverse(filename="mid-term-data.txt"):
    rows = read_file(filename=filename)
    result = []
    for row in rows[::-1]:
        result += row

    # could also do result = rows[3] + rows[2] + ...
    return result


# 2c)
def write_file(out_filename="out.csv"):
    rows = read_file()
    with open(out_filename, "w") as outfile:
        outfile.write("a,b,c")
        for row in rows[::-1]:
            outfile.write("\n")
            outfile.write(",".join(row))


# 3a)
def create_y(x=[0.1 * i for i in range(101)]):
    def f(x):
        return 5 * x + 2

    x = np.array(x)
    y = f(x)
    return y


# 3b)
def clean_curve():
    data = {
        0.00: 0.0,
        10.00: 20.0,
        30.00: 20.0,
        40.00: 20.0,
        41.33: 20.0,
        45.00: 21.5,
        50.00: 25.0,
        55.00: 100.0,
        56.00: 100.0,
        57.00: 100.0,
        60.00: 105.0,
        4000.00: 105.0,
    }
    s = pd.Series(data)
    eq1 = s.values[2:] == s.values[1:-1]
    eq2 = s.values[1:-1] == s.values[:-2]
    inner_indices = list(eq1 * eq2)
    drop_idx = [False] + inner_indices + [False]  # keep first and last number
    index_to_drop = s.index[drop_idx]
    s = s.drop(index_to_drop)
    return s


# 4a)
def read_series(filename="city_bike_data.csv"):
    df = pd.read_csv(filename)
    st0, t0, st1, t1 = [df.iloc[:, i] for i in range(4)]
    return st0, t0, st1, t1


# 4b)
def fix_dtypes(filename="city_bike_data.csv"):
    df = pd.read_csv(filename)
    df = df.dropna()  # may skip this step based on the exam text
    df["Start time"] = pd.to_datetime(df["Start time"])
    df["End time"] = pd.to_datetime(df["End time"])
    df["End station"] = df["End station"].astype(int)
    return df


# 4c)
def create_new_column():
    df = fix_dtypes()
    df["trip_duration"] = df["End time"] - df["Start time"]
    return df


# 4d)
# Here I compute the top 10 longest trips.
# Also accepted to sort other ways
def compute_top10():
    df = create_new_column()
    quantiles = df.quantile(0.9)
    duration_limit = quantiles["trip_duration"]
    df = df[df["trip_duration"] > duration_limit]
    # if you want to sort the df: df.sort_values(by="trip_duration")
    return df["trip_duration"].mean()


# 1a)
sorted_list = sort_list()
print("\nSorted list:\n", sorted_list)

# 1b)
output_calls()

# 1c)
nested_dict = make_nested_dict()
print("\nNested dict:\n", nested_dict)

# 2a)
row1, row2, row3, row4 = read_file()
print("\nRows from file:\n", row1, row2, row3, row4)

# 2b)
reversed_rows = read_and_reverse()
print("\nReversed rows:\n", reversed_rows)

# 2c)
write_file()

# 3a)
y_values = create_y()
print("\nY values:\n", y_values)

# 3b)
cleaned_series = clean_curve()
print("\nCleaned series:\n", cleaned_series)

# 4a)
start_station_0, start_time_0, start_station_1, end_time_1 = read_series()
print(
    "\nStart and end station times:\n",
    start_station_0,
    start_time_0,
    start_station_1,
    end_time_1,
)

# 4b)
fixed_df = fix_dtypes()
print("\nFixed DataFrame dtypes:\n", fixed_df)

# 4c)
df_with_new_column = create_new_column()
print("\nDataFrame with new column:\n", df_with_new_column)

# 4d)
top10_mean_duration = compute_top10()
print("\nTop 10 longest trip duration mean:\n", top10_mean_duration)
from IPython import embed

embed()
