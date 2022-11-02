import csv
import sqlite3
import sys

conn = sqlite3.connect('bone_quotes.db')
cursor = conn.cursor()

rfile = open(sys.argv[1])

contents = csv.reader(rfile)

insert_records = "INSERT INTO quotes (name, quote, year, semester, submitter, context, notes, said_by_bone) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"

cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM quotes"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

conn.commit()
conn.close()
