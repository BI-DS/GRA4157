from IPython import embed
import numpy as np
import pandas as pd
import pylab as plt

# ---------------------
# Exercise 1
# ---------------------

# Exercise 1a: Find the maximum number in the list
def a1():
    l = [1, 2, -5, 3, 12, 20, 45, 13, -10, 21]
    m = l[0]
    for i in l: 
        if i > m:
            m = i
    print("1A:", m)
    return m

# Exercise 1b: Perform specific list manipulations
def b1():
    l = [1, 2, -5, 3, 12, 20, 45, 13, -10, 21]
    print("1B:", l[1:3] + l[4:6])
    print(l[3] + l[6])
    print(2 * l[8])

# Exercise 1c: Dictionary manipulations
def c1():
    d = {"Oslo": 2.5, "London": 12.3, "Paris": 11.0, 9.0: "Berlin"}
    c = {}
    for item in d:
        if type(item) != str:
            c[d[item]] = item
        else:
            c[item] = d[item]
    print("1C:", c)

# ---------------------
# Exercise 2
# ---------------------

# Exercise 2a: Read rows from a file
def a2(filename):
    with open(filename) as infile:
        infile.readline()
        infile.readline()
        rows = [line.split()[-3:] for line in infile]
    print("2A:", rows[0], rows[1], rows[2])
    return rows

# Exercise 2b: Read columns from a file
def b2(filename):
    with open(filename) as infile:
        infile.readline()
        infile.readline()
        col1, col2, col3 = zip(*[line.split()[-3:] for line in infile])
    print("2B:", col1, col2, col3)
    return col1, col2, col3

# Exercise 2c: Write rows to a CSV file
def c2(rows):
    with open("out.csv", "w") as outfile:
        outfile.write("a,b,c\n")
        for row in rows:
            outfile.write(",".join(row) + "\n")
    print("2C: See out.csv")

# ---------------------
# Exercise 3
# ---------------------

# Exercise 3a: Comment on array ambiguity in if-statement
def a3():
    print("3A: If-statement is ambiguous on array")

# Exercise 3b: Apply function to NumPy array
def b3():
    f = np.vectorize(lambda x: x if x > 0 else -x)
    x = np.linspace(-2, 2, 11)
    print("3B (array call):", f(x))

# Exercise 3c: Plot the rate of change
def c3(t, p):
    dt = np.diff(t)
    dp = np.diff(p)
    dpdt = dp / dt
    plt.plot(t[1:], dpdt)
    plt.xlabel("time [s]")
    plt.ylabel("Price change/s")
    plt.show()
    print("3C: See plot 1")

# ---------------------
# Exercise 4
# ---------------------

# Exercise 4a: Plot CSV data using pandas
def a4(infile):
    df = pd.read_csv(infile, delimiter=",")
    df.plot(x='a', y='b')
    plt.show()
    print("4A: See plot 2")

# Exercise 4b: Extract and sort data from a Wikipedia table
def b4():
    url = "https://en.wikipedia.org/wiki/List_of_Norway_international_footballers"
    df = pd.read_html(url)[1]
    sorted_goals = df.sort_values(("Goals", "Goals"), ascending=False)
    print("4B:", sorted_goals.head(10))
    return sorted_goals

# Exercise 4c: Create a dream team based on goals
def c4(goals):                                      # This task has multiple solutions! 
                                                    # Here we assume that "goals" is the DataFrame sorted by goals scored with the highest goal scorers first
    team = [[0], [0,0,0,0], [0,0,0,0], [0,0]]                     # I store the team names in a list
    pos = {"GK": 0, "DF": 1, "FB": 1, "MF": 2, "HB": 2, "FW": 3}  # I have a mapping to determine where in the team-list players should be
    n = len(goals)
    for i in range(n):
        player = goals.iloc[i]                                    # Find the Series for the player
        p = player["Pos."]["Pos."].split()[0]                     # Find position of player. Here i chose the first position ([0]) if the player has multiple positions. 
        idx = pos[p]                                              # Index from pos dictionary
        if 0 in team[idx]:                                        # If there is still an idle spot in the players position
            count = team[idx].count(0)                            # Find out which sub-position to play (midfield right, midfield left etc). Arbitrary
            team[idx][count-1] = player["Player"]["Player"]       # Put name in team

                                                                  # If no idle spot in position, keep going.
                                                                  # Could have checked if team was filled up and break if it was
    print("4C:", team)
    
a1()
b1()
c1()
rows = a2("../lectures/02-python-summary2/example_data2.txt")
b2("../lectures/02-python-summary2/example_data2.txt")
c2(rows)
a3()
b3()

t = np.linspace(0,5,6)
p = t**2                # arbitrary sample data
c3(t,p)
a4("out.csv")

c4(b4())