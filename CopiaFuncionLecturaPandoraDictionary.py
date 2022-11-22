from sys import stdin

def leeryProcesarEntrada():
    # Funcion que retorna el array de lectura
    n = stdin.readline().replace("\n", "")
    print("\nse van a leer:", n, "diccionarios")
    try:
        # Hace el procesamiento del diccionario dado el numero de veces establecido
        for x in range(int(n)):
            xd = stdin.readline()
            valeria = xd.split(" ")
            print("Se van a leer", valeria[0], "Lineas de tamano", valeria[1].replace("\n", ""))
            vanesa = leerDiccionario(valeria[0])
            print("Terminamos leer Diccionario")
            procesarArrayOrdenado(vanesa)
    except:
        print("hubo un Error procesando el input")


def leerDiccionario(valeria):
    totalOrden = {}
    # Mete todas las paginas con la llave de su numero en el diccionario
    for x in range(int(valeria)):
        print("Vamos a leer la ultima")
        input = stdin.readline().replace("\n", "").split(" ")
        print("Leimos la ultima")
        orden = int(input[0])
        input.pop(0)
        pagina = input
        print("la pagina", pagina, "se guarda bajo la llave", orden)
        totalOrden[orden] = pagina
    # Llama la funcion para que le de el array con todas las palabras en orden
    print("En general el diccionario final se ve asi:", totalOrden)
    sol = conseguirArraydeDiccionario(totalOrden, valeria)
    return sol

def conseguirArraydeDiccionario(diccionario,n):
    # Aqui n se comporta como el numeor de lineas que leyo este diccionario
    sol = []
    for i in range(int(n)):
        # Recorremos el diccionario para conseguir las cosas en orden
        sol+= diccionario.get(i)
    return sol

def procesarArrayOrdenado(victoria):
    print("El array a procesar se ve asi:", victoria, "\n")

leeryProcesarEntrada()
print("DONE")