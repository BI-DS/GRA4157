from datetime import datetime

with open("datestamp.txt", "w") as file:
    file.write(str(datetime.now()))
