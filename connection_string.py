import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
@app.route("/login")
def login():

  username = request.values.get('username')
  password = request.values.get('password')

  # Prepare database connection
  db = pymysql.connect("localhost")
  cursor = db.cursor()

  # Execute the vulnerable SQL query concatenating user-provided input.
  cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))

  # If the query returns any matching record, consider the current user logged in.
  record = cursor.fetchone()
  if record:
    session['logged_user'] = username

  # disconnect from server
  db.close()
