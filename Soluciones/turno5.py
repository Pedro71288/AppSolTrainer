# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es un digito par.
def es_digito_par(car):
    return car in "02468"


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
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: contador de letras en posición 1 o 2 y contador de dígitos pares...
    clet = cdp = 0

    # item 3: contador de vocales, de consonantes, de palabras del punto 3 y del texto...
    cv = cc = cpp3 = cpt = 0

    # item 4: flags para t, tu, letra b y digitos...
    st = stu = sb = sdig = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "Los tucumanos tumbaron at uno ritmo de tutu y quedaron en el atium."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 3...
                # cantidad de palabras del texto...
                cpt += 1

                # item 1...
                if clet == 2 and cl > 2 and cdp == cl - 2:
                    r1 += 1

                # Item 2: menor longitud de las que tienen más de tres caracteres...
                if cl > 3 and (r2 is None or cl < r2):
                    r2 = cl

                # item 3...
                if cv > cc:
                    cpp3 += 1

                # item 4...
                if stu and not sb and not sdig:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            clet = cdp = 0

            # item 3...
            cv = cc = 0

            # item 4...
            st = stu = sb = sdig = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if car.isalpha() and cl in (1, 2):
                clet += 1
            elif es_digito_par(car):
                cdp += 1

            # item 3...
            if es_vocal(car):
                cv += 1
            elif es_consonante(car):
                cc += 1

            # item 4...
            if car in "tT":
                st = True
            else:
                if st and car in "uúUÚ":
                    stu = True
                st = False

            if car in "bB":
                sb = True
            elif es_digito_par(car):
                sdig = True

    # cálculo del porcentaje para r3...
    r3 = calcular_porcentaje(cpp3, cpt)

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
