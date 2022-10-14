from IPython import embed
import numpy as np
import pandas as pd
import pylab as plt

"""
Note to all: 
There are many ways to solve these exercises. If you managed to do what the exercise asked you to do 
you will most likely get full score on the exercise, no matter how you solved the task. 
"""

def a1():
    l = [1, 2, -5, 3, 12, 20, 45, 13, -10, 21]
    m = l[0]
    for i in l: 
        if i>m:
            m = i
    print('1A:\n', m)
    return m


def b1():
    l = [1, 2, -5, 3, 12, 20, 45, 13, -10, 21]
    print("\n\n1B:\n", l[1:3]+l[4:6])
    print(l[3]+l[6])
    print(2*l[8])
    print(2*l[8:])
    
    

def c1():
    d = {'Oslo':2.5, 'London':12.3, 'Paris':11.0, 9.0: 'Berlin'}
    c = {}
    for item in d:
        if type(item) != str:   # Check if key is not string
            c[d[item]] = item   # Swap order in new dict
        else:
            c[item] = d[item]   # Else use original dict
    print("\n\n1C:\n", c)
    
    
def a2(filename):
    infile = open(filename)
    rows = []                           # Store all rows in this list
    infile.readline()
    infile.readline()
    for line in infile:
        values = line.split()           
        rows.append(values[-3:])        # Floats are not strictly asked for so we just add strings
    
    row1, row2, row3 = rows
    infile.close()
    print("\n\n2A:\n", row1, row2, row3)
    return row1, row2, row3
   
  
def b2(filename):
    infile = open(filename)
    col1,col2,col3 = [],[],[]           
    infile.readline()
    infile.readline()
    for line in infile:
        values = line.split()
        col3.append(values[-1])         # Only three lists, so still OK to code explicitly (without loop)
        col2.append(values[-2])
        col1.append(values[-3])
    infile.close()
    print("\n\n2B:\n", col1, col2, col3)
    return col1, col2, col3



def c2(rows):
    outfile = open('out.csv','w')
    outfile.write('a,b,c\n')
    for row in rows:
        for i in range(len(row)):
            if i == 0:
                outfile.write('%s'%row[i])
            else:
                outfile.write(',%s'%row[i])
        outfile.write('\n')
    outfile.close()
    print("\n\n2C:\n See out.csv")   
   

def a3():
    print("\n\n3A:\n If-statement is ambiguous on array")
    

def b3():
    def f(x):
        if x > 0:
            return x
        else:
            return -x

    f = np.vectorize(f)         # alternatively inside f use np.append(-x[x < 0], x[x>0])
    x = np.linspace(-2,2,11)
    print("\n\n3B (array call):\n", f(x))                 # now array calls should work
    


def c3(t,p):
    dt = t[1:] - t[:-1]    # Compute time difference t_{i+1} - t{i} for i in range(len(t)-1)
    dp = p[1:] - p[:-1]    # Compure price difference p_{i+1} - p{i} for i in range(len(p)-1) 
    
    dpdt = dp/dt           # Compute derivative
    plt.plot(t[1:], dpdt)  # dpdt has one item less than t. Therefore t[1:] is used. (alternatively t[:-1])
    plt.xlabel('time [s]')
    plt.ylabel('Price change/s')
    plt.show()
    print("\n\n3C:\n See plot 1")
    
   

def a4(infile):

    df = pd.read_csv(infile, delimiter=',')
    
    a = df['a']
    b = df['b']
    c = df['c']
    plt.plot(a,b)       # Can alternatively use pandas built-in plotting
    plt.show()
    print("\n\n4A:\n See plot 2")

def b4():
    url = "https://en.wikipedia.org/wiki/List_of_Norway_international_footballers"
    df = pd.read_html(url)
    players = df[1]             # Extract correct DataFrame, (the second table if counting from 1). 
    
    goals = players.sort_values(('Goals', 'Goals'), ascending=False)    # OK if you forgot the Multi-index
    n = 10                                                              # Also possible to use goals.columns to index
    print("\n\n4B:\n", goals.head(n)['Player']['Player'])                            # OK if you forgot the Multi-index
    
    # alternative solution (there are plenty)
    #for i in range(n):
    #    print(goals.iloc[i]['Player']['Player'])                        
    return goals
    


def c4(goals):                                      # This task has multiple solutions! 
                                                    # Here we assume that "goals" is the DataFrame sorted by goals scored with the highest goal scorers first
    team = [[0], [0,0,0,0], [0,0,0,0], [0,0]]                     # I store the team names in a list
    pos = {'GK': 0, 'DF': 1, 'FB': 1, 'MF': 2, 'HB': 2, 'FW': 3}  # I have a mapping to determine where in the team-list players should be
    n = len(goals)
    for i in range(n):
        player = goals.iloc[i]                                    # Find the Series for the player
        p = player['Pos.']['Pos.'].split()[0]                     # Find position of player. Here i chose the first position ([0]) if the player has multiple positions. 
        idx = pos[p]                                              # Index from pos dictionary
        if 0 in team[idx]:                                        # If there is still an idle spot in the players position
            count = team[idx].count(0)                            # Find out which sub-position to play (midfield right, midfield left etc). Arbitrary
            team[idx][count-1] = player['Player']['Player']       # Put name in team

                                                                  # If no idle spot in position, keep going.
                                                                  # Could have checked if team was filled up and break if it was
    print("\n\n4C:\n", team)
    
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
a4('out.csv')

c4(b4())
        

    
    
    
    
    
    
    

