import psycopg2
import random as rnd

#connect to the data base
con = psycopg2.connect(
    		host = "127.0.0.1",
    		database = "prueba",
    		user = "postgres",
    		password = "1234",
    		port = 5432)
#cursor
cur = con.cursor()

con.autocommit = True

#execute query
#cur.execute("select user, name from usuario")
#cur.execute("insert into usuario (user, pwd) values (%s, %s)", ('u', 'c'))
#
#cur.execute("CREATE TABLE users(usr varchar(50) PRIMARY KEY, pwd varchar(16), score integer)")
#cur.execute("INSERT INTO users(usr, pwd) VALUES(%s, %s)", ('u', 'c'))

print("Register now!")
user = input('Type the new usr: ')
pswd = input('Type the new pwd: ')
sc = rnd.randint(0,100)

try:
	cur.execute("INSERT INTO users(usr, pwd, score) VALUES(%s, %s, %s)", (user, pswd, sc))
	#Table info
	print("====================================================")
	cur.execute("SELECT usr, pwd ,score FROM users")

	rows = cur.fetchall()
	for r in rows:
		print (f"User: {r[0]} Pwd:{r[1]} Score: {r[2]}")
	print("====================================================")
except:
	print("##### UPS!!!  User already exists :(  #####")


#commit
#cur.commit()

#close cursor
cur.close()

#close the connection
con.close()
