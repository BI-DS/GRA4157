import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from IPython import embed



# 1a) Lists and Dictionaries

def count_positive(xs=[4, -2, 15, 0, 8, 23, -7, 9, 5, -3]):
    count = 0
    for num in xs:
        if num > 0:
            count += 1
    return count


# 1b)
def output_slices(nums=[4, -2, 15, 0, 8, 23, -7, 9, 5, -3]):
    print(nums[2:5])          # [15, 0, 8]
    print(nums[-4] + nums[1]) # -7 + (-2) = -9
    print(nums[::3])          # [4, 0, -7, -3]
    print(nums[::-2])         # [-3, 9, 23, 0, -2]


# 1c)
def top_students(d={"Alice": 87, "Bob": 92, "Carla": 75, "David": 92, "Eva": 68}):
    max_grade = max(d.values())
    top = []
    for name, grade in d.items():
        if grade == max_grade:
            top.append(name)
    return top


# 1d)
def growth(
    pop_2020={"Norway": 5.4, "Sweden": 10.3, "Denmark": 5.8, "Iceland": 0.36},
    pop_2025={"Norway": 5.6, "Sweden": 10.6, "Denmark": 6.0, "Finland": 5.6},
):
    growth_dict = {}
    for country in pop_2020.keys():
        if country in pop_2025.keys():
            growth_dict[country] = pop_2025[country] - pop_2020[country]
    return growth_dict



# 2) Reading and Writing Files


def read_matrix(filename="data.txt"):
    """Read numeric rows into a list of lists of integers."""
    matrix = []
    with open(filename, "r") as infile:
        for i in range(3):
            infile.readline()
        for line in infile:
            numbers = line.strip().split()
            matrix.append([int(number) for number in numbers])
    return matrix


def sum_rows(mat=[[3, 4, 5], [6, 7, 8], [9, 10, 11]]):
    sums = []
    for row in mat:
        row_sum = 0
        for val in row:
            row_sum += val
        sums.append(row_sum)
    return sums


def write_sums_to_csv(mat=[[3, 4, 5], [6, 7, 8], [9, 10, 11]], filename="sums.csv"):
    """Write row sums to a CSV file."""
    sums = sum_rows(mat)
    with open(filename, "w") as f:
        f.write("row,sum\n")
        for i, s in enumerate(sums, start=1):
            f.write(f"{i},{s}\n")



# 3) Vectorized Computations and Pandas


def add_theoretical_power(data):
    rho = 1000
    g = 9.81
    eta = 0.9
    data["p_theoretical"] = rho * g * data["flow_rate"] * data["head"] * eta / 1000
    return data


def compute_efficiency_periods(data):
    data["efficiency"] = data["power_output"] / data["p_theoretical"]

    # assume timestamps are evenly spaced, e.g., every 10s
    below = data["efficiency"] < 0.85
    runs = below != below.shift() # This is where a new consecutive run of efficiency below or above 85 starts
    runs[runs.index[-1] + pd.Timedelta(10, "seconds")] = True  # Add this so we include the "last run". Assume evenly spacing. 
    starts = runs[runs]           # This is only the recordings of a start of a new consecutive period.
    len_of_runs = pd.Series(starts.index[1:] - starts.index[:-1], index = starts.index[:-1]) # length of each period. 
    below_eff_30_sec = (len_of_runs >= pd.Timedelta(seconds=30)) & below[len_of_runs.index] # length over 30 and below is true
    ineff_runs = len_of_runs[below_eff_30_sec] # start time and duration is ok

    return ineff_runs


def remove_redundant_rows(df):
    x = np.arange(len(df))
    y = df["power_output"].values
    # slope between consecutive points
    slopes = np.diff(y) / np.diff(x)
    # A middle point is redundant if slope[i] == slope[i-1]
    keep = np.ones(len(df), dtype=bool)
    keep[1:-1] = slopes[1:] != slopes[:-1]
    return df[keep]


# ============================================================
# 4) Web Scraping and Pandas
# ============================================================

def fetch_html(url="https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"):
    """Fetch HTML with requests."""
    headers = {"User-Agent": "PythonRequests"}
    response = requests.get(url, headers=headers)
    return response.text


def convert_value(val):
    if isinstance(val, str):
        val = val.strip().replace('\u2212', '-') # fix minus sign (not needed in exam...)
        if val.endswith('%'):
            return float(val.strip('%').replace(',', '')) / 100
        elif val.replace(',', '').replace('.', '').replace('-', '').isdigit():
            try:
                return int(val.replace(',', ''))
            except ValueError:
                return float(val.replace(',', ''))
        else:
            try:
                return float(val.replace(',', ''))
            except ValueError:
                return val
    return val

def parse_population_table(html):
    """Parse first table using BeautifulSoup."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    data_list = {}
    for row in rows[2:]:
        cells = [td.get_text(strip=True) for td in row.find_all("td")]
        cells = [convert_value(cell) for cell in cells]
        try:
            name = [td.get_text(strip=True) for td in row.find_all("th")][0]
        except:
            name = cells[0]
        data_list[name] = cells[:]
    return data_list


def clean_population_dataframe(data_list):
    """Convert list of dicts to cleaned DataFrame."""
    df = pd.DataFrame(data_list).transpose()
    # Try to coerce numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df.columns = ["pop24", "pop20", "pct_change", "abs_change", "seats", "pct_seats", "pop_per_vote", "pop_per_seat", "pct_us", "ec"]
    return df


def analyze_population(df):
    """Answer population-related questions."""
    pop_col = df["pop24"]
    largest_entry = pop_col.idxmax()
    print("Largest population entry:\n", largest_entry)

    # US totals if available
    total_2020 = df["pop20"].sum()
    total_2024 = df["pop24"].sum()

    print("\nUS population 2020:", total_2020)
    print("US population 2024:", total_2024)

    # Entries with <1% population
    total_pop = pop_col.sum()
    small_entries = df[pop_col < 0.01 * total_pop]
    combined = small_entries["pop24"].sum()
    print("\nCombined <1% entries:", combined)


# ============================================================
# Demo / Testing section
# ============================================================

if __name__ == "__main__":
    print("\n=== Exercise 1 ===")
    print("Positive count:", count_positive())
    output_slices()
    print("Top students:", top_students())
    print("Population growth:", growth())

    print("\n=== Exercise 2 ===")
    # Example matrix manually since data.txt not available
    matrix = read_matrix()
    print("Matrix:", matrix)
    print("Row sums:", sum_rows(matrix))
    write_sums_to_csv(matrix)

    print("\n=== Exercise 3 ===")
    data = pd.read_csv("hydro_data.csv", index_col=0)
    data.index = pd.to_datetime(data.index, format="%M:%S")
    data = add_theoretical_power(data)
    print("\nWith theoretical power:\n", data)
    print("\nLow-efficiency intervals:\n", compute_efficiency_periods(data))
    print("\nWithout redundant rows:\n", remove_redundant_rows(data))

    print("\n=== Exercise 4 ===")
    html = fetch_html()
    data_list = parse_population_table(html)
    keys = list(data_list.keys())[:52]
    valid_data = {key: data_list[key] for key in keys}
    df_pop = clean_population_dataframe(valid_data)
    analyze_population(df_pop)
    embed()