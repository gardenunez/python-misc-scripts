#!/usr/bin/python
"Proof connection at SQLAlchemy level, on top of pyodbc."

import urllib
from sqlalchemy import create_engine


engine = create_engine('mssql+pyodbc:///?odbc_connect=' +
    urllib.quote_plus('DRIVER=FreeTDS;SERVER=localhost;PORT=1433;DATABASE=DbName;UID=user;PWD=password;TDS_Version=8.0;')
)
connection = engine.connect()
result = connection.execute('select top 5 * from users')
for row in result:
    print row['User_ID'], row['User_Name'], row['Age']
connection.close()