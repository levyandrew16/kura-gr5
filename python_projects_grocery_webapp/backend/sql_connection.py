import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    #__cnx = mysql.connector.connect(user='root', password='prr001', database='grocery_store')
    __cnx = mysql.connector.connect(host='grocerystore.csobnuvwajav.us-east-2.rds.amazonaws.com', port= 3306, user='admin', password='grocery2021', database='grocery_store')
  return __cnx

