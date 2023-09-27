import random

def generar_numeros():
    a = 0
    b = 0

    while a == b:
        a = random.randint(0, 2)
        b = random.randint(0, 2)

    return (a, b)


a,b = generar_numeros()

points = 0

if (a == 0 or b ==0 ):
    print("Una adivinanza: Tengo hojas pero no soy un árbol, tengo una cara pero no soy una persona, ¿qué soy?" )
    print("a) Un libro\nb) Una montaña\nc) Una nube\n\n\n")

    r = input("Respuesta: ")


    if r == "a":
        print("Correcto!")
        points = points + 10
        
    else:
        print("Incorrecto")
        points = points - 5


if (a == 1 or b ==1 ):
    print("Volando en el cielo sin alas que mostrar, busco el tesoro que en las alturas he de hallar. Mi vista es aguda, no me pierdo detalle, ¿Quién soy yo, dime, en este viaje celestial?" )
    print("a) Un Halcon\nb) Un Avion\nc) Un dron\n\n\n")

    r = input("Respuesta: ")


    if r == "a":
        print("Correcto!")
        points = points + 10
        
    else:
        print("Incorrecto")
        points = points - 5
        

if (a == 2 or b ==2 ):
    print("En el campo me encuentro, en el día y en la noche,con un lomo rayado y un ronroneo que derroche. Soy cazador furtivo, pero también tierno amigo, ¿Quién soy yo en este abrigo?" )
    print("a) Un tigre\nb) Un gato\nc) Un Leopardo\n\n\n")

    r = input("Respuesta: ")


    if r == "b":
        print("Correcto!")
        points = points + 10
        
    else:
        print("Incorrecto")
        points = points - 5
        
        
        
        
    
    
print(points + " Puntos")
    
    
    


