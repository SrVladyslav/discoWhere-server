import psycopg2
import random as rnd

#connect to the data base
con = psycopg2.connect(
    		host = "ec2-174-129-227-51.compute-1.amazonaws.com",#127.0.0.1",
    		database = "d1v0tqlhb89str",
    		user = "njsxiqhypfdapi",
    		password = "dfb9dfb53353b301f08e2fdea69a6a2a71312bb048e16f64303233a7ae018b7a",
    		port = 5432)
#cursor
cur = con.cursor()

con.autocommit = True

#execute query
#cur.execute("CREATE TABLE users(usrname varchar(16) PRIMARY KEY, usr varchar(50), pwd varchar(16), karma integer)")
#cur.execute("CREATE TABLE posts(usrname varchar(16) PRIMARY KEY, msg varchar(200))")
#cur.execute("INSERT INTO users(usr, pwd) VALUES(%s, %s)", ('u', 'c'))

print("Register now!")
username1 = input('usrame')
user = input('Type the new usr: ')
pswd = input('Type the new pwd: ')
sc = 0#rnd.randint(0,100)

try:
	cur.execute("INSERT INTO users(usrname, usr, pwd, karma) VALUES(%s, %s, %s, %s)", (username1, user, pswd, sc))
	#Table info
	print("====================================================")
	#cur.execute("SELECT usr, pwd ,score FROM users")
	cur.execute("SELECT usrname , karma FROM users WHERE karma IS NOT NULL")
	rows = cur.fetchall()
	for r in rows:
		print (f"Username: {r[0]} Karma: {r[1]}")
	print("====================================================")
except:
	print("##### UPS!!!  User already exists :(  #####")


#closing cursor
cur.close()
#closing the connection
con.close()
