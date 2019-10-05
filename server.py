import socket
import _thread as t		
import sys
import psycopg2
import random as rnd
import json
import os

CONFIG_FN = "config.json"
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILE)


def cliente (c, addr, client, db_cfg):
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
			elif data == "register":
				#connecting to the data base
				con = psycopg2.connect(
				    		host = db_cfg["host"],
				    		database = db_cfg["database"],
				    		user = db_cfg["user"],
				    		password = db_cfg["password"],
				    		port = db_cfg["port"])
				#cursor
				cur = con.cursor()
				con.autocommit = True
				print("Plis, type your credentials to register!")
				username1 = input('Nick: ')
				user = input('Username: ')
				pswd = input('Password: ')
				sc = 0#rnd.randint(0,100)

				try:
					cur.execute("INSERT INTO users(usrname, usr, pwd, karma) VALUES(%s, %s, %s, %s)", (username1, user, pswd, sc))
					#Table info
					print("====================================================")
					#cur.execute("SELECT usr, pwd ,score FROM users")
					cur.execute("SELECT usrname , karma FROM users WHERE karma IS NOT NULL")
					rows = cur.fetchall()
					for r in rows:
						print (f"Nick : {r[0]} Karma : {r[1]}")
					print("====================================================")
				except:
					print("##### UPS!!!  User already exists :(  #####")


				#closing cursor
				cur.close()
				#closing the connection
				con.close()
			elif data == "show-db":
				#connecting to the data base
				con = psycopg2.connect(
				    		host = db_cfg["host"],
				    		database = db_cfg["database"],
				    		user = db_cfg["user"],
				    		password = db_cfg["password"],
				    		port = db_cfg["port"])
				#cursor
				cur = con.cursor()
				try:
					#Table info
					print("Info de la tabla pedida")
					cur.execute("SELECT usr, pwd ,karma FROM users")
					#cur.execute("SELECT usrname , score FROM users WHERE score IS NOT NULL")
					rows = cur.fetchall()
					c.sendall(bytes(rows,('utf-8')))
				except:
					print("##### Problem with connection... #####")
					c.sendall(bytes("Error...",('utf-8')))
				#closing cursor
				cur.close()
				#closing the connection
				con.close()
			else:
				print(f"Cliente <",client ,f">:  " + data)
		except: 
			vivo = 0
			c.close()
	print(f"===Cliente <" ,client ,f"> se ha desconectado.===")


# cargar configuración desde archivo json
with open(CONFIG_PATH) as cfg_file:
        config = json.load(cfg_file);
        
# creamos el objeto del socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado!")

# declaramos el puerto en el que haremos la conexion
port = 23451				

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
	t.start_new_thread(cliente, (c, addr, clientes, config['database']))	 
	clientes += 1

# cerrando la conexion (IMPORTANTE o SUSPENDEIS) 
c.close()
	

