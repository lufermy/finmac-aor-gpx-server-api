#test-file# WORKING CODE!
import pyodbc 
print(pyodbc.drivers())  
cnxn = pyodbc.connect(DRIVER='{ODBC Driver 18 for SQL Server}',
                      Server='188.165.239.21',
                      Database='AOR',
                      Port='1433',
                      UID='userAOR',
                      PWD='AORAOR01*',
                      TrustServerCertificate='yes')

cursor = cnxn.cursor()
cursor.execute("SELECT * FROM dbo.Tokens") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()