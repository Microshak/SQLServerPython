import pyodbc
import pandas


from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('Config.ini')



server=  parser.get('db', 'server')
database = parser.get('db', 'database')
username = parser.get('db', 'username')
password = parser.get('db', 'password')
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
sql = "select top 100 *  from history"
data = pandas.read_sql(sql,conn)

cursor = conn.cursor()


for index, row in data.iterrows():
    print(row.id)
    onnxresults = 3
    cursor.execute('UPDATE history SET results = {}   WHERE id = {}'.format(onnxresults, row.id))

conn.commit()

