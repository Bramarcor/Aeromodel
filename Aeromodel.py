#coding = UTF-8

# Log de desarrollo /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
# 27.10.15.v1 Terminando funcion modificar.
# 04.11.15.v2 Comenzando con funcion buscar.
# 05.11.15.v2 Siguiendo con la funcion de buscar, dando formato a los datos mostrados.
# 05.11.15.v3 Funcion buscar terminada. empesando con las funciones de ventas y corrigiendo las validaciones de la navegacion de menus.
# 16.11.15.v3 Funcion borrar comenzada y terminada
# 23.11.15.v4 Haciendo toda la carga y guardado de los datos de ventas
# 24.11.15.V5 Empezando con la funcion "fun_vender"
# 16.01.16.V5 Continuando con la funcion "fun_vender"
# 27.02.16.V5 Terminando la funcion "fun_vender"
# 29.02.16.V5 Funcion "fun_vender" Terminada e Implementada
# 29.02.16.V6 Se comienza con la funcion "fun_facturacion".
# 03.03.16.V6 Se termina con la funcion "fun_facturacion". Kamikase!!!
# /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

##################################################################
# Variacion del archivo original modificado para trabajar con archivos y clases
# Para mas placer.
##################################################################

# LISTA DE TAREAS!!!!

# MEJORAR TODA EL AREA DE VENTAS Y FACTURACION, DA VERGUENZA!!
# -- Es raro como vende los productos, revisar que se puede hacer, es medio incomodo y poco intuitivo.
# -- Tiene que hacer mas calculos asi esta re triste!! Que informe la facturacion diaria, semanal y mensual almenos!
# -- Tiene que mostrar la lista total (o de un rango determinado por fechas) de facturas con su nro. de facturacion, fecha e importe.

# PRODUCTOS
# -- tiene que administrar mejor el tema del stock y avisar o guardar en algun lado cuando algun producto esta con menos de X unidades. 
# -- Agregar una opcion para simplemente actualizar su stock. introcuciendo su codigo, validandolo e ingresando la cantidad que se repuso.

# Hacer si se puede un procedimiento que permita un backup automatico de los archivos en otra carpeta del sistema cuando se cierre correctamente el programa.
# En funcion Modificar: Cambiar la forma en como se muestran los datos correspondientes a las primary key de cada base.
# En funcion Buscar: Pensar e implementar un metodo o funcion para que el usuario pueda elejir que datos quiere que le muestre el sistema cuando encuentra conincidencias.
# En funcion Agregar: incluir como dato de ingreso la CIUDAD del CLIENTE.
# -URGENTE- En funcion Agregar: Validar las entradas numericas de cantidades, precios, numeros de identificaciones, altura de direccion. con try y except. IMPORTANTISIMO!!

"""
Declaracion de propositos
El Sistema 'Aeromodel' se encargara de gestionar a los clientes, los productos, como tambien las ventas del negocio.
El sistema contara con una aplicacion de preventa facilitandole la compra a los clientes, dandole mas libertad a la hora de elegir los productos y hacer sus compras. 


Clientes: Diccionario que contendra como clave un numero de identificacion unico y como valor una lista con los datos de los clientes. 

Dato de la clave: Nro_cliente
Datos del valor: [nombre, apellido, dni, [Direccion], [Contacto], habilitado]
Datos contenidos en la lista [Direccion]: [calle, altura, depto, piso, cp, localidad, provincia, pais]
Datos contenidos en la lista [Contacto]: [telefono, mail, celular]

Tipo de dato de la clave: Int
Tipos de datos del valor: [string, string, string, [lista direccion], [lista contacto], boolean]
Tipos de datos de la [lista direccion]: [string, string, string, string, string, string, string, string]
Tipos de datos de la [lista contacto]: [string, string, string]


Producto: Diccionario que contendra como clave un numero de identificacion unico y como valor una lista con los datos de los productos.

Dato de la clave: Nro_producto
Datos del valor: [nombre, marca, descripcion, cantidad, precio_costo, precio_venta]

Tipo de dato de la clave: Int
Tipos de datos del valor: [string, string, string, int, float, float]



Ventas: Diccionario que contendra como clave un numero de identificacion unico y como valor una lista con los datos de las ventas.

Dato de la clave: nro_venta.
Datos del valor: [nro_producto, nro_cliente, nombre_producto, cantidad, precio, fecha].

Tipo de dato de la clave: int.
Tipos de datos del valor: [int, int, string, int, float, string].



Proveedores: Diccionario que contendra como clave un numero de identificacion unico y como valor una lista con los datos del proveedor.

Dato de la clave: nro_proveedor.
Datos del valor: [nombre, cuit, [direccion], [contacto]].
Datos contenidos en la lista [Direccion]: [calle, altura, depto, piso, cp, localidad, provincia, pais]
Datos contenidos en la lista [Contacto]: [telefono, mail, celular]

Tipo de dato de la clave: int.
Tipos de datos del valor: [string, [lista_Direccion], string, [lista_Contacto]].
Tipos de datos de la [lista direccion]: [string, string, string, string, string, string, string, string]
Tipos de datos de la [lista contacto]: [string, string, string]
"""

"""
Formato de como se tienen que mostrar los datos de las facturas.

 Fecha: xx/xx/xx                        Nro. Factura: 00000
 Cliente: "Nombre Apellido Cliente"
 Nro. Cliente: 00000
+------+--------+------------------+----------+-------------+
|Cant. | Codigo | Nombre           | P. Unit. | P. Subtotal |
+------+--------+------------------+----------+-------------+
|      |        |                  |          |             |
+------+--------+------------------+----------+-------------+
|                                  |TOTAL:                  |
+------+--------+------------------+------------------------+
"""

###################################################################################
#INICIO DE PROGRAMA Funciones principales.
###################################################################################

import os 
import time
from record import record
#time.strftime("%d/%m/%y %H:%M:%S") devuelve "dia/mes/ano hora:minutos:segundos"
#Con lo anterior se obtiene la fecha del sistema para usar en las ventas.

class Productos(record):
	nro_producto = 0
	nombre = ""
	marca = ""
	descripcion = ""
	cantidad = ""
	precio_costo = ""
	precio_venta = ""

class Proveedores(record):
	nro_proveedor = 0
	nombre = ""
	cuit = ""
	calle = ""
	altura = ""
	ciudad = ""
	depto = ""
	piso = ""
	cp = ""
	localidad = ""
	provincia = ""
	pais = ""
	telefono = ""
	mail = ""
	celular = ""

class Cliente(record): # Se instancia el objeto cliente con sus atributos.
	# Por ahora es asi, para la prox se va a agregar herencia de direccion y contacto.
	codigo_cliente = 0
	nombre = ""
	apellido = ""
	dni = ""
	calle = ""
	altura = ""
	ciudad = ""
	depto = ""
	piso = ""
	cp = ""
	localidad = ""
	provincia = ""
	pais = ""
	telefono = ""
	mail = ""
	celular = ""
	habilitado = True

class Ventas(record):
	nro_facturacion = 0
	cliente = Cliente(nombre="", codigo_cliente="")
	productos = [] 
	total = 0
	fecha = ""

# Se Carga y actualiza solo la base de clientes.
# Modificar para que la carga sean todas al mismo tiempo, pero se actualizen de forma individual.
def cargar_lista_bd():
	global basededatos_clientes
	global basededatos_productos
	global basededatos_proveedores
	global basededatos_facturacion

	fichero = open("Backup BD clientes.csv","r+") # se abre el archivo con los datos.
	#Lee el fichero linea por linea y le elimina un salto de linea
	lista = []
	for linea in fichero.readlines(): # obtengo una lista con listas que contienen los datos guardados del archivo.
		lista.append(linea.rstrip().split(',')) # A la linea se le quita el retorno de carro y se convierte en una lista.
		#linea se obtiene asi: "nombre,apellido,dni" sin comillas
		# linea.split(',') me retorna una lista asi ["nombre","apellido","dni"] apartir de linea
		# esa lista se agrega a lo ultimo con el metodo .append()

	basededatos_clientes = []
	for x in range(len(lista)):
		ld = lista[x] # se separa una lista de las listas guardadas en la lista
		dato_a_ingresar = Cliente(codigo_cliente = ld[0],nombre = ld[1],apellido = ld[2],dni = ld[3],calle = ld[4],altura = ld[5],ciudad = ld[6],depto = ld[7],piso = ld[8],cp = ld[9],localidad = ld[10],provincia = ld[11],pais = ld[12],telefono = ld[13],mail = ld[14],celular = ld[15],habilitado = ld[16])
 		# en "dato_a_ingresar" se asigna el objeto cliente con los datos tomados de la lista por sus indices
 		basededatos_clientes.append(dato_a_ingresar) # en una lista que se tomata como base de datos general de todo el sistema se guardan los objetos clientes.

	#basededatos_clientes  esto obtengo de el for anterior, una lista con todos los objetos clientes con sus respectivos atributos.
	fichero.close() # se cierra el archivo despues de cargar la lista con los objetos y sus datos.
	#esto es para evitar posibles errores y la perdida de datos importantes.
	#FIN DE CARGA DE BASE CLIENTES

	#SE CARGAN LA SIGUENTE BASE
	fichero = open("BD Productos.csv","r")
	lista = []
	for linea in fichero.readlines():
		lista.append(linea.rstrip().split(',')) 

	basededatos_productos = []
	for x in range(len(lista)):
		ld = lista[x]
		dato_a_ingresar = Productos(nro_producto = ld[0],nombre = ld[1],marca = ld[2],descripcion = ld[3],cantidad = ld[4],precio_costo = ld[5],precio_venta = ld[6])
 		basededatos_productos.append(dato_a_ingresar)

	fichero.close()
	#FIN DE CARGA BASE PRODUCTOS

	#SE CARGA LA SIGUENTE BASE
	fichero = open("BD Proveedores.csv","r")
	lista = []
	for linea in fichero.readlines():
		lista.append(linea.rstrip().split(',')) 

	basededatos_proveedores = []
	for x in range(len(lista)):
		ld = lista[x]
		dato_a_ingresar = Proveedores(nro_proveedor = ld[0],nombre = ld[1],cuit = ld[2],calle = ld[3],altura = ld[4],ciudad = ld[5],depto = ld[6],piso = ld[7],cp = ld[8],localidad = ld[9],provincia = ld[10],pais = ld[11],telefono = ld[12],mail = ld[13],celular = ld[14])
 		basededatos_proveedores.append(dato_a_ingresar)

	fichero.close()
	# FIN DE CARGA BASE PROVEEDORES

	# CARGA DE LAS VENTAS
	fichero = open("BD Facturacion.csv","r")
	lista = []
	for linea in fichero.readlines():
		# Este for le da formato a una cadena que recibe del archivo y lo convierte en listas anidadas.
		# linea ==> "1234,codigo;nombre,Nombre;codigo;cant;punit-Nombre;codigo;cant;punit,1234,24/12/45\n"
		linea = linea.rstrip().split(',')
		# linea ==> ['1234','codigo;nombre','Nombre;codigo;cant;punit-Nombre;codigo;cant;punit','1234','24/12/45']
		linea[1] = linea[1].split(';')
		# linea ==> ['1234',['codigo','nombre'],'Nombre;codigo;cant;punit-Nombre;codigo;cant;punit','1234','24/12/45']
		linea[2] = linea[2].split('-')
		# linea ==> ['1234',['codigo','nombre'],['Nombre;codigo;cant;punit','Nombre;codigo;cant;punit'],'1234','24/12/45']
		for z in range(len(linea[2])):
			linea[2][z] = linea[2][z].split(';')
		# linea ==> ['1234',['codigo','nombre'],[['Nombre','codigo','cant','punit'],['Nombre','codigo','cant','punit']],'1234','24/12/45']
		lista.append(linea) 
	
	basededatos_facturacion = []
	for x in range(len(lista)):
		ld = lista[x]
		# ld ==> ['1234',['codigo','nombre'],[['Nombre','codigo','cant','punit'],['Nombre','codigo','cant','punit']],'1234','24/12/45']
		comprador = Cliente(codigo_cliente = ld[1][0], nombre = ld[1][1])
		productos_comprados = []
		for i in range(len(ld[2])):
			dato = Productos(nombre = ld[2][i][0], nro_producto = ld[2][i][1], cantidad = ld[2][i][2], precio_venta = ld[2][i][3])
			productos_comprados.append(dato)
	
		dato_a_ingresar = Ventas(nro_facturacion = ld[0], cliente = comprador, productos = productos_comprados, total = ld[3], fecha = ld[4])
		basededatos_facturacion.append(dato_a_ingresar)
	
	fichero.close()
	# FIN CARGA DE VENTAS
	return


def actualizar_clientes():
	"""se usa para guardar los datos denuevo en el archivo de origen"""
	fichero = open("Backup BD clientes.csv","w+") # se abre el archivo con los datos.
	for x in basededatos_clientes: # Recorre la lista de base de datos y asigna en "x" un objeto distinto por cada vuelta del bucle
		fichero.write(x.codigo_cliente + ",") #Codigo_cliente se ingresa como STR
		fichero.write(x.nombre + ",")
		fichero.write(x.apellido + ",")
		fichero.write(x.dni + ",")
		fichero.write(x.calle + ",")
		fichero.write(x.altura + ",")
		fichero.write(x.ciudad + ",")
		fichero.write(x.depto + ",")
		fichero.write(x.piso + ",")
		fichero.write(x.cp + ",")
		fichero.write(x.localidad + ",")
		fichero.write(x.provincia + ",")
		fichero.write(x.pais + ",")
		fichero.write(x.telefono + ",")
		fichero.write(x.mail + ",")
		fichero.write(x.celular + ",")
		fichero.write(x.habilitado) # Se ingresa como STR
		fichero.write("\n")

	fichero.close()
	return

def actualizar_productos():
	"""se usa para guardar los datos denuevo en el archivo de origen"""
	fichero = open("BD Productos.csv","w+")
	for x in basededatos_productos:
		fichero.write(x.nro_producto + ",")
		fichero.write(x.nombre + ",")
		fichero.write(x.marca + ",")
		fichero.write(x.descripcion + ",")
		fichero.write(str(x.cantidad) + ",")
		fichero.write(str(x.precio_costo) + ",")
		fichero.write(str(x.precio_venta))
		fichero.write("\n")

	fichero.close()
	return

def actualizar_proveedores():
	"""se usa para guardar los datos denuevo en el archivo de origen"""
	fichero = open("BD Proveedores.csv","w+")
	for x in basededatos_proveedores:
		fichero.write(x.nro_proveedor + ",")
		fichero.write(x.nombre + ",")
		fichero.write(x.cuit + ",")
		fichero.write(x.calle + ",")
		fichero.write(x.altura + ",")
		fichero.write(x.ciudad + ",")
		fichero.write(x.depto + ",")
		fichero.write(x.piso + ",")
		fichero.write(x.cp + ",")
		fichero.write(x.localidad + ",")
		fichero.write(x.provincia + ",")
		fichero.write(x.pais + ",")
		fichero.write(x.telefono + ",")
		fichero.write(x.mail + ",")
		fichero.write(x.celular)
		fichero.write("\n")

	fichero.close()
	return

def actualizar_facturacion():
	"""se usa para guardar los datos denuevo en el archivo de origen"""
	fichero = open("BD Facturacion.csv","w+")
	for x in basededatos_facturacion:
		fichero.write(x.nro_facturacion + ",")
		fichero.write(x.cliente.codigo_cliente + ";")
		fichero.write(x.cliente.nombre + ",")
		
		termina = len(x.productos)
		for i in x.productos:
			termina = termina - 1
			fichero.write(i.nombre + ";")
			fichero.write(i.nro_producto + ";")
			fichero.write(str(i.cantidad) + ";")
			fichero.write(str(i.precio_venta) + ";")
			if termina >= 1:
				fichero.write("-")
			else:
				fichero.write(",")
	
		fichero.write(str(x.total) + ",")
		fichero.write(x.fecha)
		fichero.write("\n")
	
	fichero.close()
	return

def limpiar_pantalla():
	if os.name == 'posix':
		os.system ('clear')
	elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
		os.system ('cls')


###################################################################################
#Validaciones
###################################################################################

clientes = ("1","C","Cl","CLI","CLIE","CLIEN","CLIENT","CLIENTE","CLIENTES")
productos = ("2","PROD","PRODU","PRODUC","PRODUCT","PRODUCTO","PRODUCTOS")
proveedores =("3","PROV","PROVEE","PROVEED","PROVEEDO","PROVEEDOR","PROVEEDORE","PROVEEDORES")
ventas = ("4","V","VE","VEN","VENT","VENTA","VENTAS")
preventa = ("5","PRE","PREV","PREVE","PREVEN","PREVENT","PREVENTA")
agregar = ("1","A","AG","AGR","AGRE","AGREG","AGREG","AGREGA","AGREGAR")
modificar = ("2","M","MO","MOD","MODI","MODIF","MODIFI","MODIFIC","MODIFICA","MODIFICAR")
buscar = ("3","B","BU","BUS","BUSC","BUSCA","BUSCAR")
eliminar = ("4","E","EL","ELI","ELIM","ELIMI","ELIMIN","ELIMINA","ELIMINAR")
vender = ("1","VEND","VENDE","VENDER")
registro_ventas = ("2","R","RE","REG","REGI","REGIS","REGIST","REGISTR","REGISTRO")
facturacion = ("3","F","FA","FAC","FACT","FACTU","FACTUR","FACTURA","FACTURAC","FACTURACI","FACTURACIO","FACTURACION")
salir = ("0","S","SA","SAL","SALI","SALIR","EXIT")


###################################################################################
# Funciones de muestras por pantalla.
###################################################################################
def menu_principal():
	limpiar_pantalla()
	print "+-----------------------------------------------+"
	print "|>>=============SISTEMA AEROMODEL=============<<|"
	print "+-----------------------------------------------+"
	print ":.:.Menu principal.:.:"
	print "\n"
	print "  1.-Clientes."
	print "  2.-Productos."
	print "  3.-Proveedores."
	print "  4.-Ventas."
	print "  0.-Salir."

def menu_clientes():
	limpiar_pantalla()
	print ":.:.Menu Clientes.:.:"
	print "\n"
	print "  1.-Agregar."
	print "  2.-Modificar."
	print "  3.-Buscar."
	print "  4.-Eliminar"
	print "  0.-Salir."

def menu_productos():
	limpiar_pantalla()
	print ":.:.Menu Productos.:.:"
	print "\n"
	print "  1.-Agregar."
	print "  2.-Modificar."
	print "  3.-Buscar."
	print "  4.-Eliminar"
	print "  0.-Salir."

def menu_proveedores():
	limpiar_pantalla()
	print ":.:.Menu Proveedores.:.:"
	print "\n"
	print "  1.-Agregar."
	print "  2.-Modificar."
	print "  3.-Buscar."
	print "  4.-Eliminar"
	print "  0.-Salir."

def menu_ventas():
	limpiar_pantalla()
	print ":.:.Menu Ventas.:.:"
	print "\n"
	print "  1.-Vender." # realiza una venta
	print "  2.-Registro de ventas." # Busca en la base como la funcion buscar y muestra parte de la info de cada coincidencia
	print "  3.-Facturacion." # Se muestra todos los datos detallados ingresando un nero de facturacion especifico.
	print "  0.-Salir."

###################################################################################################
# Funciones de tratado de datos
###################################################################################################
def generador_codigos(base):
	# Genera un codigo nuevo, con referencia a la base que se le pase.
	if base == basededatos_clientes:
		cod = []
		for x in basededatos_clientes:
			cod.append(int(x.codigo_cliente))
		
		cod.sort() # Importante que los numeros sean Int para poder ordenar adecuadamente.
		cod = cod.pop()
		clave_retorno = str(int(cod)+1)
		return clave_retorno

	elif base == basededatos_productos:
		cod = []
		for x in basededatos_productos:
			cod.append(int(x.nro_producto))
		
		cod.sort() # Importante que los numeros sean Int para poder ordenar adecuadamente.
		cod = cod.pop()
		clave_retorno = str(int(cod)+1)
		return clave_retorno

	elif base == basededatos_proveedores:
		cod = []
		for x in basededatos_proveedores:
			cod.append(int(x.nro_proveedor))
		
		cod.sort() # Importante que los numeros sean Int para poder ordenar adecuadamente.
		cod = cod.pop()
		clave_retorno = str(int(cod)+1)
		return clave_retorno

	elif base == basededatos_facturacion:
		cod = []
		for x in basededatos_facturacion:
			cod.append(int(x.nro_facturacion))
		
		cod.sort() # Importante que los numeros sean Int para poder ordenar adecuadamente.
		cod = cod.pop()
		clave_retorno = str(int(cod)+1)
		return clave_retorno

###################################################################################################
def fun_agregar(bd): # Idea a implementar, dar la opcion de cancelar el ingreso si se arrepiente de hacerlo. durante el ingreso o despues de haberlo hecho se pueden descartar los datos.
	limpiar_pantalla()
	if bd == "cliente":
		print "Ingrese los datos del cliente, conforme se los va pidiendo.\n"
		datos_Clientes = ["Nombre: ","Apellido: ","D.N.I: ","Calle: ","Altura: ","Depto: ","Piso: ","Codigo Postal: ","Localidad: ","Provincia: ","Pais: ","Telefono de linea: ","Correo Electronico: ","Telefono Celular: "]
		ld = []
		for x in datos_Clientes:
			print x
			ingreso = raw_input("").capitalize()
			ld.append(ingreso)

		new_clave = generador_codigos(basededatos_clientes)
		dato_a_ingresar = Cliente(codigo_cliente = new_clave,nombre = ld[0],apellido = ld[1],dni = ld[2],calle = ld[3],altura = ld[4],depto = ld[5],piso = ld[6],cp = ld[7],localidad = ld[8],provincia = ld[9],pais = ld[10],telefono = ld[11],mail = ld[12],celular = ld[13],habilitado = "True")
		basededatos_clientes.append(dato_a_ingresar)
		actualizar_clientes()
		print "La operacion fue un exito la clave del nuevo usuario es: ", new_clave
		raw_input()

	elif bd == "proveedor":
		print "Ingrese los datos del proveedor, conforme se los va pidiendo.\n"
		datos_Proveedores = ["Nombre: ", "CUIT: ", "Calle: ", "Altura: ","Ciudad: ", "Depto: ", "Piso:", "Codigo Postal: ", "Localidad: ", "Provincia: ", "Pais: ", "Telefono de linea: ", "Mail: ", "Celular: "]
		ld = []
		for x in datos_Proveedores:
			print x
			ingreso = raw_input("").capitalize()
			ld.append(ingreso)

		new_clave = generador_codigos(basededatos_proveedores)
		dato_a_ingresar = Proveedores(nro_proveedor = new_clave,nombre = ld[0],cuit = ld[1],calle = ld[2],altura = ld[3],ciudad = ld[4],depto = ld[5],piso = ld[6],cp = ld[7],localidad = ld[8],provincia = ld[9],pais = ld[10],telefono = ld[11],mail = ld[12],celular = ld[13])
		basededatos_proveedores.append(dato_a_ingresar)
		actualizar_proveedores()
		print "La operacion fue un exito la clave del nuevo Proveedor es: ", new_clave
		raw_input()

	elif bd == "producto":
		print "Ingrese los datos del producto, conforme se los va pidiendo.\n"
		datos_Productos = ["Nombre: ", "Marca: ", "Descripcion del Producto: ", "Cantidad que ingresa: ", "Precio de Costo: ", "Precio de Venta: "]
		ld = []
		for x in datos_Productos:
			print x
			ingreso = raw_input("").capitalize()
			ld.append(ingreso)

		new_clave = generador_codigos(basededatos_productos)
		dato_a_ingresar = Productos(nro_producto = new_clave,nombre = ld[0],marca = ld[1],descripcion = ld[2],cantidad = ld[3],precio_costo = ld[4],precio_venta = ld[5])
		basededatos_productos.append(dato_a_ingresar)
		actualizar_productos()
		print "La operacion fue un exito la clave del nuevo Producto es: ", new_clave
		raw_input()

###################################################################################################

def fun_modificar(bd,clave): # Validar el ingreso de una clave.
	if bd == "cliente":
		ingreso = 1
		while  ingreso == 1:
			limpiar_pantalla()
			datos_Clientes = ["1-Nombre: ","2-Apellido: ","3-D.N.I: ","4-Calle: ","5-Altura: ","6-Ciudad: ","7-Depto: ","8-Piso: ","9-Codigo Postal: ","10-Localidad: ","11-Provincia: ","12-Pais: ","13-Telefono de linea: ","14-Correo Electronico: ","15-Telefono Celular: "]
			encontrado = ""
			for x in basededatos_clientes:
				if x.codigo_cliente == str(clave):
					encontrado = x

			if encontrado != "":
				print datos_Clientes[0], encontrado.nombre
				print datos_Clientes[1], encontrado.apellido
				print datos_Clientes[2], encontrado.dni
				print datos_Clientes[3], encontrado.calle
				print datos_Clientes[4], encontrado.altura
				print datos_Clientes[5], encontrado.ciudad
				print datos_Clientes[6], encontrado.depto
				print datos_Clientes[7], encontrado.piso
				print datos_Clientes[8], encontrado.cp
				print datos_Clientes[9], encontrado.localidad
				print datos_Clientes[10], encontrado.provincia
				print datos_Clientes[11], encontrado.pais
				print datos_Clientes[12], encontrado.telefono
				print datos_Clientes[13], encontrado.mail
				print datos_Clientes[14], encontrado.celular
				print "0-SALIR\n"
			
				print "Verifique si los datos son correctos. Si son correctos ingrese 0."
				selec = raw_input("Ingrese el numero correspondiente al dato a modificar: ")
				
				if selec == "1":
					valor_cambiar = raw_input("Ingrese el nuevo Nombre: ")
					encontrado.nombre = valor_cambiar.capitalize()
				elif selec == "2":
					valor_cambiar = raw_input("Ingrese el nuevo Apellido: ")
					encontrado.apellido = valor_cambiar.capitalize()
				elif selec == "3":
					valor_cambiar = raw_input("Ingrese el nuevo DNI: ")
					encontrado.dni = valor_cambiar.capitalize()
				elif selec == "4":
					valor_cambiar = raw_input("Ingrese la nueva Calle: ")
					encontrado.calle = valor_cambiar.capitalize()
				elif selec == "5":
					valor_cambiar = raw_input("Ingrese la nueva Altura: ")
					encontrado.altura = valor_cambiar.capitalize()
				elif selec == "6":
					valor_cambiar = raw_input("Ingrese la nueva Ciudad: ")
					encontrado.ciudad = valor_cambiar.capitalize()
				elif selec == "7":
					valor_cambiar = raw_input("Ingrese el nuevo Departamento: ")
					encontrado.depto = valor_cambiar.capitalize()
				elif selec == "8":
					valor_cambiar = raw_input("Ingrese el nuevo Piso: ")
					encontrado.piso = valor_cambiar.capitalize()
				elif selec == "9":
					valor_cambiar = raw_input("Ingrese el nuevo Codigo Postal: ")
					encontrado.cp = valor_cambiar.capitalize()
				elif selec == "10":
					valor_cambiar = raw_input("Ingrese la nueva Localidad: ")
					encontrado.localidad = valor_cambiar.capitalize()
				elif selec == "11":
					valor_cambiar = raw_input("Ingrese la nueva Provincia: ")
					encontrado.provincia = valor_cambiar.capitalize()
				elif selec == "12":
					valor_cambiar = raw_input("Ingrese el nuevo Pais: ")
					encontrado.pais = valor_cambiar.capitalize()
				elif selec == "13":
					valor_cambiar = raw_input("Ingrese el nuevo Telefono de linea: ")
					encontrado.telefono = valor_cambiar
				elif selec == "14":
					valor_cambiar = raw_input("Ingrese el nuevo Email: ")
					encontrado.mail = valor_cambiar
				elif selec == "15":
					valor_cambiar = raw_input("Ingrese el nuevo Telefono celular: ")
					encontrado.celular = valor_cambiar
				elif selec == "0":
					ingreso = 0
				else:
					print "El valor ingresado es incorrecto por favor vuelva a intentarlo "
					raw_input("OK")	

			else: 
				print "La Clave ingresada no existe, por favor vuelva a intentarlo"
				ingreso = 0 
				raw_input()

		actualizar_clientes()

	elif bd == "producto":
		ingreso = 1
		while  ingreso == 1:
			limpiar_pantalla()
			datos_Productos = ["1-Nombre: ", "2-Marca: ", "3-Descripcion del Producto: ", "4-Cantidad que ingresa: ", "5-Precio de Costo: ", "6-Precio de Venta: "]
			encontrado = ""
			for x in basededatos_productos:
				if x.nro_producto == str(clave):
					encontrado = x

			if encontrado != "":
				print datos_Productos[0], encontrado.nombre
				print datos_Productos[1], encontrado.marca
				print datos_Productos[2], encontrado.descripcion
				print datos_Productos[3], encontrado.cantidad
				print datos_Productos[4], encontrado.precio_costo
				print datos_Productos[5], encontrado.precio_venta
				print "0-SALIR\n"
				
				print "Verifique si los datos son correctos. Si son correctos ingrese 0."
				selec = raw_input("Ingrese el numero correspondiente al dato a modificar: ")
				
				if selec == "1":
					valor_cambiar = raw_input("Ingrese el nuevo Nombre: ")
					encontrado.nombre = valor_cambiar.capitalize()
				elif selec == "2":
					valor_cambiar = raw_input("Ingrese la nueva marca: ")
					encontrado.marca = valor_cambiar.capitalize()
				elif selec == "3":
					valor_cambiar = raw_input("Ingrese la nueva descripcion: ")
					encontrado.descripcion = valor_cambiar.capitalize()
				elif selec == "4":
					valor_cambiar = raw_input("Ingrese la nueva cantidad: ")
					encontrado.cantidad = valor_cambiar.capitalize()
				elif selec == "5":
					valor_cambiar = raw_input("Ingrese el nuevo precio de costo: ")
					encontrado.precio_costo = valor_cambiar.capitalize()
				elif selec == "6":
					valor_cambiar = raw_input("Ingrese el nuevo precio de venta: ")
					encontrado.precio_venta = valor_cambiar.capitalize()
				elif selec == "0":
					ingreso = 0
				else:
					print "El valor ingresado es incorrecto por favor vuelva a intentarlo "
					raw_input("OK")	

			else:
				print "La Clave ingresada no existe, por favor vuelva a intentarlo"
				ingreso = 0 
				raw_input()

		actualizar_productos()
		
	elif bd == "proveedor":
		ingreso = 1
		while ingreso == 1:
			limpiar_pantalla()
			datos_Proveedores = ["1-Nombre: ", "2-CUIT: ", "3-Calle: ", "4-Altura: ","5-Ciudad: ", "6-Depto: ", "7-Piso:", "8-Codigo Postal: ", "9-Localidad: ", "10-Provincia: ", "11-Pais: ", "12-Telefono de linea: ", "13-Mail: ", "14-Celular: "]
			encontrado = ""
			for x in basededatos_proveedores:
				if x.nro_proveedor == str(clave):
					encontrado = x

			if encontrado != "":
				print datos_Proveedores[0], encontrado.nombre
				print datos_Proveedores[1], encontrado.cuit
				print datos_Proveedores[2], encontrado.calle
				print datos_Proveedores[3], encontrado.altura
				print datos_Proveedores[4], encontrado.ciudad
				print datos_Proveedores[5], encontrado.depto
				print datos_Proveedores[6], encontrado.piso
				print datos_Proveedores[7], encontrado.cp
				print datos_Proveedores[8], encontrado.localidad
				print datos_Proveedores[9], encontrado.provincia
				print datos_Proveedores[10], encontrado.pais
				print datos_Proveedores[11], encontrado.telefono
				print datos_Proveedores[12], encontrado.mail
				print datos_Proveedores[13], encontrado.celular
				print "0-SALIR\n"
			
				print "Verifique si los datos son correctos. Si son correctos ingrese 0."
				selec = raw_input("Ingrese el numero correspondiente al dato a modificar: ")
				
				if selec == "1":
					valor_cambiar = raw_input("Ingrese el nuevo Nombre: ")
					encontrado.nombre = valor_cambiar.capitalize()
				elif selec == "2":
					valor_cambiar = raw_input("Ingrese el nuevo CUIT: ")
					encontrado.cuit = valor_cambiar.capitalize()
				elif selec == "3":
					valor_cambiar = raw_input("Ingrese el nuevo Calle: ")
					encontrado.calle = valor_cambiar.capitalize()
				elif selec == "4":
					valor_cambiar = raw_input("Ingrese la nueva Altura: ")
					encontrado.altura = valor_cambiar.capitalize()
				elif selec == "5":
					valor_cambiar = raw_input("Ingrese la nueva Ciudad: ")
					encontrado.ciudad = valor_cambiar.capitalize()
				elif selec == "6":
					valor_cambiar = raw_input("Ingrese la nueva Departamento: ")
					encontrado.depto = valor_cambiar.capitalize()
				elif selec == "7":
					valor_cambiar = raw_input("Ingrese el nuevo Piso: ")
					encontrado.piso = valor_cambiar.capitalize()
				elif selec == "8":
					valor_cambiar = raw_input("Ingrese el nuevo Codigo Postal: ")
					encontrado.cp = valor_cambiar.capitalize()
				elif selec == "9":
					valor_cambiar = raw_input("Ingrese el nuevo Localidad: ")
					encontrado.localidad = valor_cambiar.capitalize()
				elif selec == "10":
					valor_cambiar = raw_input("Ingrese la nueva Provincia: ")
					encontrado.provincia = valor_cambiar.capitalize()
				elif selec == "11":
					valor_cambiar = raw_input("Ingrese la nueva Pais: ")
					encontrado.pais = valor_cambiar.capitalize()
				elif selec == "12":
					valor_cambiar = raw_input("Ingrese el nuevo Telefono: ")
					encontrado.telefono = valor_cambiar.capitalize()
				elif selec == "13":
					valor_cambiar = raw_input("Ingrese el nuevo Email: ")
					encontrado.mail = valor_cambiar
				elif selec == "14":
					valor_cambiar = raw_input("Ingrese el nuevo Celular: ")
					encontrado.celular = valor_cambiar.capitalize()
				elif selec == "0":
					ingreso = 0
				else:
					print "El valor ingresado es incorrecto por favor vuelva a intentarlo "
					raw_input("OK")

			else:
				print "La Clave ingresada no existe, por favor vuelva a intentarlo"
				ingreso = 0 
				raw_input()

		actualizar_proveedores()
	
###################################################################################################

def fun_buscar(bd): # SEGUIR ACA
	if bd == "cliente":
		# Va a recorrer toda la base buscando coincidencias y almacenandolas en un array
		limpiar_pantalla()
		print "Busqueda de clientes."
		ingreso = raw_input("Ingrese un dato que contenga su cliente a buscar: ").upper()
		encontrado = []
		for x in basededatos_clientes:
			if x.codigo_cliente == ingreso:
				encontrado.append(x)
			elif x.nombre.upper() == ingreso:
				encontrado.append(x)
			elif x.apellido.upper() == ingreso:
				encontrado.append(x)
			elif x.dni.upper() == ingreso:
				encontrado.append(x)
			elif x.calle.upper() == ingreso:
				encontrado.append(x)
			elif x.altura.upper() == ingreso:
				encontrado.append(x)
			elif x.ciudad.upper() == ingreso:
				encontrado.append(x)
			elif x.depto.upper() == ingreso:
				encontrado.append(x)
			elif x.piso.upper() == ingreso:
				encontrado.append(x)
			elif x.cp.upper() == ingreso:
				encontrado.append(x)
			elif x.localidad.upper() == ingreso:
				encontrado.append(x)
			elif x.provincia.upper() == ingreso:
				encontrado.append(x)
			elif x.pais.upper() == ingreso:
				encontrado.append(x)
			elif x.telefono.upper() == ingreso:
				encontrado.append(x)
			elif x.mail.upper() == ingreso:
				encontrado.append(x)
			elif x.celular.upper() == ingreso:
				encontrado.append(x)

		if encontrado != []: # Por ahora solo muestra estos datos, mas adelante el usuario eligira que datos quiere ver.
			# Tambien que los espacios en blancos sean dinamicos, segun la longitud del string mas largo de cada dato.
			print "Operacion realizada con exito!\n"
			print "-----+--------------+----------------+------------+------------------------------+--------+--------------+--------------------------------------+------------+"
			print "Nro. | Nombre       | Apellido       | DNI        | Calle                        | Altura | Telefono     | Mail                                 | Celular    |"
			print "-----+--------------+----------------+------------+------------------------------+--------+--------------+--------------------------------------+------------+"
			for x in encontrado:
				print (x.codigo_cliente).zfill(4),"|", (x.nombre).ljust(12," "),"|", (x.apellido).ljust(14, " "),"|", (x.dni).rjust(10," "),"|", (x.calle).ljust(28," "),"|", (x.altura).rjust(6," "),"|", (x.telefono).rjust(12," "),"|", (x.mail).ljust(36," "),"|", (x.celular).rjust(10," "),"|"
				print "-----+--------------+----------------+------------+------------------------------+--------+--------------+--------------------------------------+------------+"

			print "\n"
			raw_input("ENTER para continuar...")
		else:
			raw_input("No se encontraron coincidencias...")

	elif bd == "producto":
		limpiar_pantalla()
		print "Buscar Productos"
		ingreso = raw_input("Ingrese un dato que contenga su Producto a buscar: ").upper()
		encontrado = []
		for x in basededatos_productos:
			if x.nro_producto.upper() == ingreso:
				encontrado.append(x)
			elif x.nombre.upper() == ingreso:
				encontrado.append(x)
			elif x.marca.upper() == ingreso:
				encontrado.append(x)
			elif x.descripcion.upper() == ingreso:
				encontrado.append(x)
			elif x.cantidad == ingreso:
				encontrado.append(x)
			elif x.precio_costo == ingreso:
				encontrado.append(x)
			elif x.precio_venta == ingreso:
				encontrado.append(x)

		if encontrado != []:
			print "Operacion realizada con exito!\n"
			print "-----+-----------------+------------+------------------------------------------+-------+----------+----------+"
			print "Nro. | Nombre          | Marca      | Descripcion                              | Stock | P.Costo  | P.Venta  |"
			print "-----+-----------------+------------+------------------------------------------+-------+----------+----------+"
			for x in encontrado:
				print (x.nro_producto).zfill(4),"|", (x.nombre).ljust(15," "),"|", (x.marca).ljust(10, " "),"|", (x.descripcion).ljust(40," "),"|", (x.cantidad).rjust(5," "),"|", (x.precio_costo).rjust(8," "),"|", (x.precio_venta).rjust(8," "),"|"
				print "-----+-----------------+------------+------------------------------------------+-------+----------+----------+"

			print "\n"
			raw_input("ENTER para continuar...")

		else:
			print "\n"
			raw_input("No se encontraron coincidencias...")

	elif bd == "proveedor":
		limpiar_pantalla()
		print "Buscar Proveedores"
		ingreso = raw_input("Ingrese un dato que contenga su Proveedor a buscar: ").upper()
		encontrado = []
		for x in basededatos_proveedores:
			if x.nro_proveedor == ingreso:
				encontrado.append(x)
			elif (x.nombre).upper() == ingreso:
				encontrado.append(x)
			elif (x.cuit).upper() == ingreso:
				encontrado.append(x)
			elif x.calle.upper() == ingreso:
				encontrado.append(x)
			elif x.altura.upper() == ingreso:
				encontrado.append(x)
			elif x.ciudad.upper() == ingreso:
				encontrado.append(x)
			elif x.depto.upper() == ingreso:
				encontrado.append(x)
			elif x.piso.upper() == ingreso:
				encontrado.append(x)
			elif x.cp.upper() == ingreso:
				encontrado.append(x)
			elif x.localidad.upper() == ingreso:
				encontrado.append(x)
			elif x.provincia.upper() == ingreso:
				encontrado.append(x)
			elif x.pais.upper() == ingreso:
				encontrado.append(x)
			elif x.telefono.upper() == ingreso:
				encontrado.append(x)
			elif x.mail.upper() == ingreso:
				encontrado.append(x)
			elif x.celular.upper() == ingreso:
				encontrado.append(x)

		if encontrado != []:
			print "Operacion realizada con exito!\n"
			print "-----+-----------------+-----------------+------------------------------+--------+--------------+--------------------------------------+------------+"
			print "Nro. | Nombre          | Cuit            | Calle                        | Altura | Telefono     | Mail                                 | Celular    |"
			print "-----+-----------------+-----------------+------------------------------+--------+--------------+--------------------------------------+------------+"
			for x in encontrado:
				print (x.nro_proveedor).zfill(4),"|", (x.nombre).ljust(15," "),"|", (x.cuit).rjust(15," "),"|", (x.calle).ljust(28," "),"|", (x.altura).rjust(6," "),"|", (x.telefono).rjust(12," "),"|", (x.mail).ljust(36," "),"|", (x.celular).rjust(10," "),"|"
				print "-----+-----------------+-----------------+------------------------------+--------+--------------+--------------------------------------+------------+"
		
			print "\n"
			raw_input("ENTER para continuar...")

		else:
			print "\n"
			raw_input("No se encontraron conincidencias...")

def fun_borrar(bd):
	if bd == "cliente":
		limpiar_pantalla()
		bucle = 0
		while bucle == 0:
			datos_Clientes = ["1-Nombre: ","2-Apellido: ","3-D.N.I: ","4-Calle: ","5-Altura: ","6-Ciudad: ","7-Depto: ","8-Piso: ","9-Codigo Postal: ","10-Localidad: ","11-Provincia: ","12-Pais: ","13-Telefono de linea: ","14-Correo Electronico: ","15-Telefono Celular: "]
			ingreso = raw_input("Ingrese el codigo del cliente a eliminar: ")
			encontrado = []
			indice = -1
			for x in basededatos_clientes:
				indice = indice + 1
				if x.codigo_cliente == ingreso:
					encontrado.append(x)
					break
				
			if encontrado != []:
				print datos_Clientes[0], basededatos_clientes[indice].nombre
				print datos_Clientes[1], basededatos_clientes[indice].apellido
				print datos_Clientes[2], basededatos_clientes[indice].dni
				print datos_Clientes[3], basededatos_clientes[indice].calle
				print datos_Clientes[4], basededatos_clientes[indice].altura
				print datos_Clientes[5], basededatos_clientes[indice].ciudad
				print datos_Clientes[6], basededatos_clientes[indice].depto
				print datos_Clientes[7], basededatos_clientes[indice].piso
				print datos_Clientes[8], basededatos_clientes[indice].cp
				print datos_Clientes[9], basededatos_clientes[indice].localidad
				print datos_Clientes[10], basededatos_clientes[indice].provincia
				print datos_Clientes[11], basededatos_clientes[indice].pais
				print datos_Clientes[12], basededatos_clientes[indice].telefono
				print datos_Clientes[13], basededatos_clientes[indice].mail
				print datos_Clientes[14], basededatos_clientes[indice].celular
				print "0-SALIR\n"
				print "Son los datos del cliente que desea borrar?"
				selecciona = raw_input("Ingrese 1 para borrar, 0 para salir: ")
				
				if selecciona == "1":
					basededatos_clientes.pop(indice)
					limpiar_pantalla()
					raw_input("Cliente eliminado con exito!")
					actualizar_clientes() # Acatualiza el archivo para que tambien desaparesca de ahi el dato borrado.
					bucle = 1

				elif selecciona == "0":
					bucle = 1

				else:
					limpiar_pantalla()
					print "El ingreso es incorrecto, vuelva a intentarlo."
					raw_input()
			else:
				limpiar_pantalla()
				print "El codigo", ingreso, "no existe, verifique el codigo y vuelva a intentarlo."
				raw_input()

	elif bd == "producto":
		limpiar_pantalla()
		bucle = 0
		while bucle == 0:
			datos_Productos = ["1-Nombre: ", "2-Marca: ", "3-Descripcion del Producto: ", "4-Cantidad que ingresa: ", "5-Precio de Costo: ", "6-Precio de Venta: "]
			ingreso = raw_input("Ingrese el codigo del producto a eliminar: ")
			encontrado = []
			indice = -1
			for x in basededatos_productos:
				indice = indice + 1
				if x.nro_producto == ingreso:
					encontrado.append(x)
					break
			
			if encontrado != []:
				print datos_Productos[0], basededatos_productos[indice].nombre
				print datos_Productos[1], basededatos_productos[indice].marca
				print datos_Productos[2], basededatos_productos[indice].descripcion
				print datos_Productos[3], basededatos_productos[indice].cantidad
				print datos_Productos[4], basededatos_productos[indice].precio_costo
				print datos_Productos[5], basededatos_productos[indice].precio_venta
				print "0-SALIR\n"

				print "Los datos corresponden al poducto que desea eliminar?"
				selecciona = raw_input("Ingrese 1 para borrar, 0 para salir: ")
				
				if selecciona == "1":
					basededatos_productos.pop(indice)
					limpiar_pantalla()
					raw_input("Producto eliminado con exito!")
					actualizar_productos() # Acatualiza el archivo para que tambien desaparesca de ahi el dato borrado.
					bucle = 1

				elif selecciona == "0":
					bucle = 1

				else:
					limpiar_pantalla()
					print "El ingreso es incorrecto, vuelva a intentarlo."
					raw_input()
			else:
				limpiar_pantalla()
				print "El codigo", ingreso, "no existe, verifique el codigo y vuelva a intentarlo."
				raw_input()
	elif bd == "proveedor":
		limpiar_pantalla()
		bucle = 0
		while bucle == 0:
			datos_Proveedores = ["1-Nombre: ", "2-CUIT: ", "3-Calle: ", "4-Altura: ","5-Ciudad: ", "6-Depto: ", "7-Piso:", "8-Codigo Postal: ", "9-Localidad: ", "10-Provincia: ", "11-Pais: ", "12-Telefono de linea: ", "13-Mail: ", "14-Celular: "]
			ingreso = raw_input("Ingrese el codigo del proveedor a eliminar: ")
			encontrado = []
			indice = -1
			for x in basededatos_proveedores:
				indice = indice + 1
				if x.nro_proveedor == ingreso:
					encontrado.append(x)
					break
				
			if encontrado != []:
				print datos_Proveedores[0], basededatos_proveedores[indice].nombre
				print datos_Proveedores[1], basededatos_proveedores[indice].cuit
				print datos_Proveedores[2], basededatos_proveedores[indice].calle
				print datos_Proveedores[3], basededatos_proveedores[indice].altura
				print datos_Proveedores[4], basededatos_proveedores[indice].ciudad
				print datos_Proveedores[5], basededatos_proveedores[indice].depto
				print datos_Proveedores[6], basededatos_proveedores[indice].piso
				print datos_Proveedores[7], basededatos_proveedores[indice].cp
				print datos_Proveedores[8], basededatos_proveedores[indice].localidad
				print datos_Proveedores[9], basededatos_proveedores[indice].provincia
				print datos_Proveedores[10], basededatos_proveedores[indice].pais
				print datos_Proveedores[11], basededatos_proveedores[indice].telefono
				print datos_Proveedores[12], basededatos_proveedores[indice].mail
				print datos_Proveedores[13], basededatos_proveedores[indice].celular
				print "0-SALIR\n"

				print "Son los datos del Proveedor que desea borrar?"
				selecciona = raw_input("Ingrese 1 para borrar, 0 para salir: ")
				
				if selecciona == "1":
					basededatos_proveedores.pop(indice)
					limpiar_pantalla()
					raw_input("Proveedor eliminado con exito!")
					actualizar_proveedores() # Acatualiza el archivo para que tambien desaparesca de ahi el dato borrado.
					bucle = 1

				elif selecciona == "0":
					bucle = 1

				else:
					limpiar_pantalla()
					print "El ingreso es incorrecto, vuelva a intentarlo."
					raw_input()
			else:
				limpiar_pantalla()
				print "El codigo", ingreso, "no existe, verifique el codigo y vuelva a intentarlo."
				raw_input()


def mostrar_factura(venta):
	print " Fecha: ",venta.fecha,"			Nro. Factura:",(venta.nro_facturacion).zfill(5)
	print " Cliente:",venta.cliente.nombre
	print " Nro. Cliente:",venta.cliente.codigo_cliente
	print "+------+--------+------------------+----------+-------------+"
	print "|Cant. | Codigo | Nombre           | P. Unit. | P. Subtotal |"
	print "+------+--------+------------------+----------+-------------+"
	for x in venta.productos:
		print "|",str(x.cantidad).rjust(4," "),"|",str(x.nro_producto).rjust(6," "),"|",str(x.nombre).ljust(16," "),"|",str(x.precio_venta).rjust(8," "),"|",str(int(x.cantidad) * float(x.precio_venta)).rjust(11," "),"|"
	print "+------+--------+------------------+----------+-------------+"
	print "|                                  |TOTAL:",str(venta.total).rjust(16," "),"|"
	print "+----------------------------------+------------------------+"


def fun_vender(): #### Marcar un limite en la cantidad segun con el stock que se cuente. ####
	"""Funcion que hace y registra una venta"""
	print "Ingrese los datos para realizar la venta.\n"
	validacion = 0

	while validacion == 0: # Este while es para validar el codigo ingresado del comprador.
		print "Si el comprador es un cliente ingrese su codigo de identificacion, de lo contrario no ingrese nada."
		ingreso = raw_input("Ingreso: ")
		
		if ingreso != "":
			encontrado = 0
			for x in basededatos_clientes:
				if x.codigo_cliente == ingreso:
					encontrado = x

			if encontrado != 0:
				cliente = Cliente(codigo_cliente = encontrado.codigo_cliente, nombre = encontrado.nombre+" "+encontrado.apellido)
				validacion = 1
			
			else:
				limpiar_pantalla()
				print "El codigo del cliente ingresado no es valido o no existe, por favor vuelva a intentarlo."

		else:
			cliente = Cliente(codigo_cliente = "01-01", nombre = "Particular")
			validacion = 1
		## Fin del Bucle de validacion de CLientes
		
	validacion = 0
	productos = []
	v_total = 0
	while validacion == 0: # Este while se usa para validar todos los codigos de los productos a comprar.
		ingreso = raw_input("Ingrese el codigo del producto que se va a vender: ")
		
		encontrado = 0
		for x in basededatos_productos: # Este For busca una coincidencia con los codigos guardados y cuando la encuentra guarda todo el producto en encontrado.
			if x.nro_producto == ingreso:
				encontrado = x
				break
		
		if encontrado != 0:
			bucle = 0
			while bucle == 0: # Este while se usa para validar el ingreso de la cantidad para que solo se puede ingresar un numero entero y no otra cosa.
				# Hacer este bucle en todos los ingresos donde los datos sean numeros.
				cantidad = raw_input("Ingrese cual es la cantidad a vender: ")
				try:
					cantidad = int(cantidad)
				except:
					limpiar_pantalla()
					print "Por favor ingrese solo numeros enteros.\n"

				if cantidad <= int(encontrado.cantidad): # Este if Controla de no vender mas cantidad de la que se cuenta
					# La linea diguente le descuenta al stock la cantidad que se va a vender del producto. 
					# la variable encontrado, al hacer referencia del dato y ubicacion del objeto producto seleccionado, 
					# premite simplemente descontarle a la variable sin tener que buscar en la base denuevo a ese objeto para modificarlo.
					encontrado.cantidad = int(encontrado.cantidad) - cantidad 
					bucle = 1
				else:
					limpiar_pantalla()
					print "\n"
					print "Solo cuenta con",encontrado.cantidad," unidades del producto en Stock."
					print "Vuelva a ingresar un valor, menor o igual al que se encuentra en Stock."

			# Ahora hay que guardar en la lista "productos" el producto a comprar con su formato.
			dato = Productos(nombre = encontrado.nombre, nro_producto = encontrado.nro_producto, cantidad = cantidad, precio_venta = encontrado.precio_venta)
			productos.append(dato)

			limpiar_pantalla()
			print "\n"
			print "Quedan en Stock",encontrado.cantidad,"Unidades del producto seleccionado.\n"

			ingreso = raw_input("Si desea ingresar otro producto presione Enter, De lo contrario ingrese 0: ")
			if ingreso == "":
				validacion = 0
			else:
				validacion = 1

			

		else:
			limpiar_pantalla()
			print "\n"
			print "El codigo del producto ingresado no es valido o no existe, por favor vuelva a intentarlo."
		## Fin del bucle ingreso de productos

	### Apartir de aca se procede a Generar el dato "venta" con todos sus componentes para luego mostrarlos en la "Factura"
	total = 0
	for x in productos: # Este for calcula el precio total de la venta.
		total = total + (int(x.cantidad) * float(x.precio_venta))

	
	venta = Ventas(nro_facturacion = generador_codigos(basededatos_facturacion), cliente = cliente, productos = productos, total = total, fecha = time.strftime("%d/%m/%y"))

	mostrar_factura(venta)
	
	check = raw_input("Confirma la venta de estos productos? Enter=Si / 0=No: ")
	
	if check == "":
		basededatos_facturacion.append(venta)
		actualizar_facturacion()
		actualizar_productos()
	else:
		pass

def fun_facturacion():
	bucle = 0
	while bucle == 0: # Este while funciona para cuando el codigo no se encuentra o no existe.
		codigo = raw_input("Ingrese el codigo de la Factura: ")

		while 0==0: ## Este while valida que el codigo sea un numero
			try:
				codigo = int(codigo)
				break
			except:
				limpiar_pantalla()
				print "\n"
				print "Usted solo debe ingresar Numeros."
				codigo = raw_input("Reingrese el codigo de la Factura: ")
	
		encontrado = 0
		for x in basededatos_facturacion: # Este For busca en la lista base una coincidencia con el codigo ingresado
			if int(x.nro_facturacion) == codigo:
				encontrado = x

		if encontrado != 0:
			limpiar_pantalla()
			mostrar_factura(encontrado)
			raw_input("Continuar...")
			bucle = 1

		else:
			limpiar_pantalla()
			print "\n"
			print "El codigo ingresado no Existe o es Incorrecto"


###################################################################################
#Fin de definiciones de las Funciones
###################################################################################

###################################################################################
#Cuerpo principal del programa
###################################################################################

cargar_lista_bd() # carga las listas base con todos los datos de los archivos. (Las listas son como la base de datos.)

exit = False

while exit != True:
	menu_principal()
	opcion = (raw_input("Por favor selecciona una opcion: ")).upper()

	if opcion in clientes:
		exit_menu = False
		while exit_menu != True:
			menu_clientes()
			opcion_menu = (raw_input("Por favor selecciona una opcion: ")).upper()

			if opcion_menu in agregar:
				fun_agregar("cliente") # Segun el parametro agrega un dato en la BD correspondiente

			elif opcion_menu in modificar:
				codcli= raw_input("Ingrese el codigo interno del Cliente a modificar: ")
				fun_modificar("cliente",codcli)
								
			elif opcion_menu in buscar:
				fun_buscar("cliente")

			elif opcion_menu in eliminar:
				fun_borrar("cliente")

			elif opcion_menu in salir:
				exit_menu = True
			else:
				limpiar_pantalla()
				raw_input("El valor ingresado no es valido. Vuelva a intentarlo.")

	elif opcion in productos:
		exit_menu = False
		while exit_menu != True:
			menu_productos()
			opcion_menu = (raw_input("Por favor selecciona una opcion: ")).upper()

			if opcion_menu in agregar:
				fun_agregar("producto") # Segun el parametro agrega un dato en la BD correspondiente
								
			elif opcion_menu in modificar:
				codprod= raw_input("Ingrese el codigo interno del Producto a modificar: ")
				fun_modificar("producto",codprod)
				
			elif opcion_menu in buscar:
				fun_buscar("producto")

			elif opcion_menu in eliminar:
				fun_borrar("producto")

			elif opcion_menu in salir:
				exit_menu = True
			else:
				limpiar_pantalla()
				raw_input("El valor ingresado no es valido. Vuelva a intentarlo.")

	elif opcion in proveedores:
		exit_menu = False
		while exit_menu != True:
			menu_proveedores()
			opcion_menu = (raw_input("Por favor selecciona una opcion: ")).upper()

			if opcion_menu in agregar:
				fun_agregar("proveedor") # Segun el parametro agrega un dato en la BD correspondiente
				
			elif opcion_menu in modificar:
				codprovee= raw_input("Ingrese el codigo interno del Proveedor a modificar: ")
				fun_modificar("proveedor",codprovee)
				
			elif opcion_menu in buscar:
				fun_buscar("proveedor")

			elif opcion_menu in eliminar:
				fun_borrar("proveedor")

			elif opcion_menu in salir:
				exit_menu = True
			else:
				limpiar_pantalla()
				raw_input("El valor ingresado no es valido. Vuelva a intentarlo.")

	elif opcion in ventas:
		exit_menu = False
		while exit_menu != True:
			menu_ventas()
			opcion_menu = (raw_input("Por favor selecciona una opcion: ")).upper()

			if opcion_menu in vender:
				fun_vender()
		
			elif opcion_menu in registro_ventas:
				# Funcion Registro de ventas
				# se va autilizar para revisar las ventas del dia semana o mes.
				pass
		
			elif opcion_menu in facturacion:
				# Funcion Facturacion Se puede unir con el registro de ventas. (pensando que voy a hacer)
				# Funcion que sirve para saber los los movimientos de mercaderia y dinero como tambien que indique las ganancias o perdidas.
				fun_facturacion()
		
			elif opcion_menu in salir:
				exit_menu = True
		
			else:
				limpiar_pantalla()
				raw_input("El valor ingresado no es valido. Vuelva a intentarlo.")

		
	elif opcion in salir:
		exit = True

	else:
		limpiar_pantalla()
		raw_input("El valor ingresado no es valido. Vuelva a intentarlo.")


limpiar_pantalla()

