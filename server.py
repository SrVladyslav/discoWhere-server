import psycopg2
import random as rnd

#connect to the data base
con = psycopg2.connect(
    		host = "ec2-23-23-182-18.compute-1.amazonaws.com",#127.0.0.1",
    		database = "dennd4iuajacnp",
    		user = "qakosmistdhlbr",
    		password = "2c06eed80820c1b17e4e780409a94f670403dac2040ee7624349d04d09131850",
    		port = 5432)
#cursor
cur = con.cursor()

con.autocommit = True

#execute query
#cur.execute("select user, name from usuario")
#cur.execute("insert into usuario (user, pwd) values (%s, %s)", ('u', 'c'))
#
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
