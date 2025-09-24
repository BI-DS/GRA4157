import os
from math import sqrt

outfile = open("outfile.txt", "w")

x = [i for i in range(1, 11)]

outfile.write("x sqrt(x)\n")

for xi in x:
    outfile.write(f"{xi:.2f} {sqrt(xi):.2f}\n")
    # outfile.write('%.2f %.2f\n'%(xi, sqrt(xi)))

outfile.close()
