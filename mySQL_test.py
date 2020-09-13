import mysql.connector

mydb = mysql.connector.connect(
  host="10.129.1.10",
  user="djo",
  passwd="Z#Tk!K7GG1#zmQ2UvX@oIz",
  database="nzta_sh94_aws_data"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM nzta_aoc1_site_10")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)