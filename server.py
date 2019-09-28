import psycopg2
import random as rnd

#connect to the data base
con = psycopg2.connect(
    		host = "ec2-54-75-238-138.eu-west-1.compute.amazonaws.com",#127.0.0.1",
    		database = "dfrtb63stjohc3",
    		user = "sjudskmhldapvz",
    		password = "e7cc00c0a5c24b576e0a386a209cbbdc84fcd627d3cce989667c5acfe57ae91b",
    		port = 5432)
#cursor
cur = con.cursor()

con.autocommit = True

#execute query
#cur.execute("select user, name from usuario")
#cur.execute("insert into usuario (user, pwd) values (%s, %s)", ('u', 'c'))
#
#cur.execute("CREATE TABLE users(usrname varchar(16) PRIMARY KEY, usr varchar(50), pwd varchar(16), score integer)")
#cur.execute("INSERT INTO users(usr, pwd) VALUES(%s, %s)", ('u', 'c'))

print("Register now!")
#username1 = input('usrame')
#user = input('Type the new usr: ')
#pswd = input('Type the new pwd: ')
#sc = rnd.randint(0,100)

try:
	#cur.execute("INSERT INTO users(usrname, usr, pwd, score) VALUES(%s, %s, %s, %s)", (username1, user, pswd, sc))
	#Table info
	print("====================================================")
	#cur.execute("SELECT usr, pwd ,score FROM users")
	cur.execute("SELECT usrname , score FROM users WHERE score IS NOT NULL")
	rows = cur.fetchall()
	for r in rows:
		print (f"Username: {r[0]} Score: {r[1]}")
	print("====================================================")
except:
	print("##### UPS!!!  User already exists :(  #####")


#closing cursor
cur.close()
#closing the connection
con.close()
