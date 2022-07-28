import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-UL480R1F\SQLEXPRESS;'
                      'Database=BloodbankBD;'
                      'Trusted _connections=yes;')
cursor = conn.cursor()
