# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una vocal.
def es_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: contador de dígitos y contador de mayúsculas...
    cd = cm = 0

    # item 2: flag de inicio con letra t...
    st1 = False

    # item 3: contador de vocales que no sean la u...
    cv = 0

    # item 4: flags para d, di e inicio con di...
    sd = sdi = di1 = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada.txt")
    texto = m.read()
    m.close()

    # texto = "Usted imagina doscientos videos sobre aduioses lo adimos y lo perdimos todo."

    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if cd == 2 and cm == cl - 2:
                    r1 += 1

                # Item 2: menor longitud de las que empiezan con t...
                if st1 and (r2 is None or cl < r2):
                    r2 = cl

                # item 3...
                if cv == cl:
                    r3 += 1

                # item 4...
                if sdi and not di1:
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            cd = cm = 0

            # item 2...
            st1 = False

            # item 3...
            cv = 0

            # item 4...
            sd = sdi = di1 = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_digito(car) and cl in (2, 4):
                cd += 1
            elif car.isupper():
                cm += 1

            # item 2...
            if car in "tT" and cl == 1:
                st1 = True

            # item 3...
            if car.lower() in "aeioáéíó":
                cv += 1

            # item 4...
            if car in "dD":
                sd = True
            else:
                if sd and car in "iíIÍ":
                    sdi = True

                    # si el if que sigue es cierto, la palabra empieza con di...
                    if cl == 2:
                        di1 = True

                sd = False

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
