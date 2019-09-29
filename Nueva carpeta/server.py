import psycopg2
import random as rnd
import socket
import _thread as t		
import sys

def cliente (c, addr, client):
	print('Peticion entrante de: ', addr) 
	# Devolviendo un mensaje por los jajas. 
	c.sendall(b'Bienvenidos al servidor, pulsa s para salir o info para informacion') 
	vivo = 1
	while vivo == 1:
		try:
			#recibiendo mensajes
			data = (c.recv(1024)).decode()
			if data == 's':
				vivo = 0
			elif data == "info":
				#admin = input("Admin: ")
				admin = "Respondido por el servidor!"# + admin
				c.sendall(bytes(admin,('utf-8')))
				print(f"El cliente <", client,f">pidio la info!")
			else:
				print(f"Cliente <",client ,f">:  " + data)
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
				username1 = data# input('usrame')
				user = data #input('Type the new usr: ')
				pswd = data# input('Type the new pwd: ')
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
		except: 
			vivo = 0
			c.close()
	print(f"===Cliente <" ,client ,f"> se ha desconectado.===")

# creamos el objeto del socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado!")

# declaramos el puerto en el que haremos la conexion
port = 5000				

# ponemos a la escucha al servidor a todas las ips entrantes
# al puerto dado
s.bind(('', port))		 
print("socket a la escucha en el puerto: %s" %(port)) 

# ponemos al socket a escuchar aceptando como maximo 5 usuarios 
s.listen(5)	 
print("socket escuchando...")
print("==========================CONEXIONES=========================")		
clientes = 0
# bucle de escucha que acepta las peticiones
while clientes < 5	: 
	# estableciendo la conexion con el cliente 
	c, addr = s.accept()
	t.start_new_thread(cliente, (c, addr, clientes))	 
	clientes += 1

# cerrando la conexion (IMPORTANTE o SUSPENDEIS) 
c.close()