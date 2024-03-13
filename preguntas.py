"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # def suma_segunda_columna(data.csv):

    with open("data.csv") as data:
        data = data.readlines()

    suma = 0
    for line in data:  # divide por linea
        line = line.split()  # divide por palabras
        suma += int(line[1])  # suma la segunda línea y lo convierte en entero
    return suma


print(pregunta_01())


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    new_sequence = []
    diccionario = {}
    sequence = []

    for line in data:  # divide por línea
        line = line.split()  # divide por palabras
        letra = line[0]  # el primer elemento lo guarda en vble letra

        new_sequence.append((letra, 1))  # Agrega la tupla en la lista new_sequence
    sorted_sequence = sorted(new_sequence, key=lambda x: x[0])  # ordena las tuplas
    for clave, valor in sorted_sequence:
        diccionario[clave] = (
            diccionario.get(clave, 0) + 1
        )  # creamos diccionario y suma si existen
    for clave, valor in diccionario.items():
        sequence.append((clave, valor))
    return sequence  # retorna la lista de tuplas


print(pregunta_02())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    with open("data.csv") as data:
        data = data.readlines()

    new_sequence = []
    diccionario = {}
    sequence = []

    for line in data:  # divide por línea
        line = line.split()  # divide por palabras
        letra = line[0]  # el primer elemento lo guarda en vble letra
        valor = int(
            line[1]
        )  # el segundo elemento, guarda en vble valor y lo convierte en entero

        new_sequence.append((letra, valor))  # Agrega la tupla en la lista new_sequence
    sorted_sequence = sorted(new_sequence, key=lambda x: x[0])  # ordena las tuplas
    for clave, valor in sorted_sequence:
        diccionario[clave] = (
            diccionario.get(clave, 0) + valor
        )  # creamos diccionario y suma si existen
    for clave, valor in diccionario.items():
        sequence.append((clave, valor))
    return sequence  # retorna la lista de tuplas


print(pregunta_03())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    new_sequence = []
    diccionario = {}
    sequence = []

    for line in data:  # divide por linea
        line = line.split()  # divide por palabras
        fecha = line[2]  # el tercer elemento lo guarda en vble fecha
        fecha = fecha.split(sep="-")[1]

        new_sequence.append((fecha, 1))  # Agrega la dupla en la lista new_sequence
    for fecha, valor in new_sequence:
        diccionario[fecha] = diccionario.get(fecha, 0) + int(valor)
        # creamos diccionario y suma si existen
    for fecha, valor in diccionario.items():
        sequence.append((fecha, valor))
    sorted_sequence = sorted(sequence, key=lambda x: x[0])  # ordena las tuplas

    return sorted_sequence  # retorna la lista de tuplas


print(pregunta_04())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    diccionarios = {}

    for line in data:  # divide por línea

        line = line.split()  # divide por lista de palabras
        letra = line[0]  # el primer elemento lo guarda en vble letra
        numero = int(line[1])  # el segundo elemento lo guarda en vble numero

        if letra in diccionarios:
            diccionarios[letra] = (
                max(diccionarios[letra][0], numero),
                min(diccionarios[letra][1], numero),
            )
        else:
            diccionarios[letra] = (numero, numero)

    diccionarios = sorted(diccionarios.items(), key=lambda x: x[0])
    diccionarios = [(clave, valores[0], valores[1]) for clave, valores in diccionarios]
    return diccionarios


print(pregunta_05())


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    diccionario = {}

    for line in data:  # divide por linea

        line = line.split()  # divide por lista de palabras
        columna = line[4]  # el quinto elemento lo guarda en vble columna
        columna = columna.split(",")

        for clave_valor in columna:
            clave, valor = clave_valor.split(":")
            valor = int(valor)
            if clave in diccionario:

                diccionario[clave] = (
                    min(diccionario[clave][0], valor),
                    max(diccionario[clave][1], valor),
                )
            else:
                diccionario[clave] = (valor, valor)

    diccionario = sorted(diccionario.items(), key=lambda x: x[0])
    diccionario = [(clave, valores[0], valores[1]) for clave, valores in diccionario]
    return diccionario


print(pregunta_06())


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    diccionario = {}

    for line in data:  # divide por línea

        line = line.split()  # divide por lista de palabras
        columnaNumeros = int(line[1])
        columnaLetras = line[0]  # el primer elemento lo guarda en vble columnaletras

        if columnaNumeros in diccionario:
            diccionario[columnaNumeros].append(columnaLetras)
        else:
            diccionario[columnaNumeros] = [columnaLetras]

    diccionario = sorted(diccionario.items(), key=lambda x: x[0])

    return diccionario


print(pregunta_07())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv") as data:
        data = data.readlines()

    diccionario = {}

    for line in data:  # divide por línea

        line = line.split()  # divide por lista de palabras
        columnaNumeros = line[1]
        columnaLetras = line[0]  # el primer elemento lo guarda en vble columnaletras

        if columnaNumeros in diccionario:

            if columnaLetras not in diccionario[columnaNumeros]:
                diccionario[columnaNumeros].append(columnaLetras)

        else:
            diccionario[columnaNumeros] = [columnaLetras]
    diccionario = sorted(diccionario.items(), key=lambda x: x[0])

    diccionario = [(int(clave), sorted(valor)) for clave, valor in diccionario]
    return diccionario


print(pregunta_08())


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open("data.csv") as data:
        data = data.readlines()

    diccionario = {}

    for line in data:  # divide por línea

        line = line.split()  # divide por lista de palabras
        columna = line[4]
        columna = columna.split(",")  # separa por comas

        for clave_valor in columna:
            clave, valor = clave_valor.split(":")

            if clave in diccionario:
                diccionario[clave] += 1
            else:
                diccionario[clave] = 1

    diccionario = sorted(diccionario.items(), key=lambda x: x[0])
    diccionario = dict(diccionario)
    return diccionario


print(pregunta_09())


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    with open("data.csv") as data:
        data = data.readlines()

    lista = []

    for line in data:  # divide por línea

        line = line.split()
        letra = line[0]
        valor1 = line[3]
        valor2 = line[4]
        tupla = (letra, len(valor1.split(",")), len(valor2.split(",")))
        lista.append(tupla)
    return lista


print(pregunta_10())

pregunta_10()


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open("data.csv") as data:
        data = data.readlines()

    diccionario = {}

    for line in data:  # divide por línea
        line = line.split()  # separa la vble line
        columna3 = line[3].split(",")
        valor = int(line[1])

        for letra in columna3:
            if letra in diccionario:
                diccionario[letra] += valor
            else:
                diccionario[letra] = valor
    diccionario = sorted(diccionario.items(), key=lambda x: x[0])

    return dict(diccionario)


print(pregunta_11())


def pregunta_12():
    """

    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario = {}
    with open("./data.csv") as data:
        data = data.readlines()

    for line in data:
        linea = line.split()
        columna1 = linea[0]
        columna5 = linea[4].split(",")
        suma = 0
        for clave_valor in columna5:
            clave, valor = clave_valor.split(":")
            suma += int(valor)

        if columna1 in diccionario:
            diccionario[columna1] += suma
        else:
            diccionario[columna1] = suma
    diccionario = sorted(diccionario.items(), key=lambda x: x[0])
    return dict(diccionario)


print(pregunta_12())
