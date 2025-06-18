# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función para cacular el promedio entero entre sus parámetros.
def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: contador de consonantes...
    ccon = 0

    # item 2: flags para vocal en posición 2 y para letra n...
    svp2 = sn = False

    # item 3: señal letra g, contador de digitos, acumulador de caracteres item 3, y contador palabras item3...
    sgp2 = False
    cdig = ccp3 = cpp3 = 0

    # item 4: flags para p, pe, y comienzo con vocal...
    sp = spe = svoc = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "Apenas la pereza lo permita apelaremos sobre el tapete y pienso ganar."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if cl % 2 == 1 and ccon == 1:
                    r1 += 1

                # Item 2: menor longitud de las que tienen vocal en posición 2 y ninguna n...
                if svp2 and not sn and (r2 is None or cl < r2):
                    r2 = cl

                # item 3...
                if sgp2 and cdig == 0:
                    ccp3 += cl
                    cpp3 += 1

                # item 4...
                if spe and not svoc:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            ccon = 0

            # item 2...
            svp2 = sn = False

            # item 3...
            sgp2, cdig = False, 0

            # item 4...
            sp = spe = svoc = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_consonante(car):
                ccon += 1

            # item 2...
            if es_vocal(car) and cl == 2:
                svp2 = True
            elif car in "nN":
                sn = True

            # item 3...
            if car in "gG" and cl == 2:
                sgp2 = True
            elif es_digito(car):
                cdig += 1

            # item 4...
            if car in "pP":
                sp = True
            else:
                if sp and car in "eéEÉ":
                    spe = True
                sp = False

            if es_vocal(car) and cl == 1:
                svoc = True

    # cálculo del promedio para r3...
    r3 = calcular_promedio(ccp3, cpp3)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()