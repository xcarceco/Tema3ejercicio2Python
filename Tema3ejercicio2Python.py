#Escribe un programa en la consola de python
# que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable,
# e imprima por pantalla la frase Tu índice de masa corporal es <imc>
# donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
# Tienes que subir capturas de pantalla en una carpeta comprimida zip.

peso=float(input('Pon tu peso en Kg, por favor:'))
estatura=float(input('Pon tu estatura en metros cuadrados, por favor:'))

imc=peso//estatura
print('Tu índice de masa corporal es:', imc)

