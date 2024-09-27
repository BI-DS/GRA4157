"""
Create datestamp
"""

from datetime import datetime

with open("datestamp.txt", "w", encoding="utf-8") as file:
    file.write(str(datetime.now()))
