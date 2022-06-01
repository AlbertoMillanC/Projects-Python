#formulario para nombre, telefono, dirección y email

#importamos el módulo cgi
import cgi, cgitb

#creamos una instancia de FieldStorage
form = cgi.FieldStorage()

#obtenemos los valores enviados
nombre = form.getvalue('nombre')
telefono = form.getvalue('telefono')
direccion = form.getvalue('direccion')
email = form.getvalue('email')

#mostramos los valores recibidos
print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Formulario</title>")
print("</head>")
print("<body>")
print("<h2>Datos recibidos</h2>")
print("<p>")
print("Nombre: %s<br>" % nombre)
print("Teléfono: %s<br>" % telefono)
print("Dirección: %s<br>" % direccion)
print("Email: %s<br>" % email)
print("</p>")
print("</body>")
print("</html>")


#ejecutamos el módulo cgitb para mostrar los errores
cgitb.enable()