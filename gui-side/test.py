#test-file# WORKING CODE!
import pyodbc 
print(pyodbc.drivers())  
cnxn = pyodbc.connect(DRIVER='{ODBC Driver 18 for SQL Server}',
                      Server='',
                      Database='',
                      Port='',
                      UID='',
                      PWD='*',
                      TrustServerCertificate='yes')

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.Tokens") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()
