import pandas as pd
import sqlite3

con = sqlite3.connect('site.db')

df = pd.read_csv('~/Documents/ucietyAPP/application/SocietyDatabase.csv')
df.to_sql('~/Documents/ucietyAPP/application/SocietyDatabase.csv', con)

print (df)