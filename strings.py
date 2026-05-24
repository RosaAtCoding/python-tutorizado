nombre = "Juan"

# La función print imprime en consola
print("Hola, mi nombre es " + nombre)

print("Hola, mi nombre es " + "Juan")


edad = 18

#print("Hola, mi nombre es Juan y tengo la edad de " + edad)    # error!
print("Hola, mi nombre es Juan y tengo la edad de " + str(edad) + " años")


salario = 2500
comision = 150

print(salario + comision)
print("El sueldo total es: " + str(salario + comision))

print('El sueldo total es: ' + str(salario + comision))


texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat.'''

print(texto)
