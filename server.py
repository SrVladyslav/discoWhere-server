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
		except: 
			vivo = 0
			c.close()
	print(f"===Cliente <" ,client ,f"> se ha desconectado.===")

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
	t.start_new_thread(cliente, (c, addr, clientes))	 
	clientes += 1

# cerrando la conexion (IMPORTANTE o SUSPENDEIS) 
c.close()
	

