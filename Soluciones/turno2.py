# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función para calcular el porcentaje entero entre sus parámetros.
def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 // total
    return porcentaje


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r2 = r3 = r4 = 0

    # contador de letras en una palabra...
    cl = 0

    # item 1: flag de dígitos y contador de consonantes...
    sv23, ccp4 = False, 0

    # item 2: flag de vocal, contador de palabras con vocal terminadas en dígito, y contador total de palabras...
    sv, cpvd, cpt = False, 0, 0

    # item 3: contador de vocales ...
    cv3p = 0

    # item 4: flags para d, de y t...
    sd = sde = stp = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada2.txt")
    texto = m.read()
    m.close()

    # texto = "ataderas."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if sv23 and ccp4 >= 2:
                    r1 += 1

                # item 2...
                # cantidad de palabras del texto...
                cpt += 1

                # cantidad de palabras con vocal terminadas en dígito...
                if sv and es_digito(ul):
                    cpvd += 1

                # item 3...
                if cl >= 4 and cv3p == 3:
                    r3 += 1

                # item 4...
                if sde and stp:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            sv23, ccp4 = False, 0

            # item 2...
            sv = False

            # item 3...
            cv3p = 0

            # item 4...
            sd = sde = stp = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_digito(car) and cl in (2, 3):
                sv23 = True
            elif es_consonante(car) and cl >= 4:
                ccp4 += 1

            # item 2...
            if es_vocal(car):
                sv = True

            # item 3...
            if cl <= 3 and es_vocal(car):
                cv3p += 1

            # item 4...
            if car in "dD":
                sd = True
            else:
                if sd and car in "eéEÉ":
                    sde = True
                sd = False

            if sde and car in "tT":
                stp = True

            # item 2...
            # guardar la última letra...
            ul = car

    # cálculo del porcentaje para r2...
    r2 = calcular_porcentaje(cpvd, cpt)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
