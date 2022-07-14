import pypyodbc as pyodbc

cnxn = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};"
                  "SERVER=localhost;"
                  "DATABASE=test;"
                  "UID=YYY;"
                  "PWD=XXX;"
                  "TrustServerCertificate=no;"
                  "Connection Timeout=60")
