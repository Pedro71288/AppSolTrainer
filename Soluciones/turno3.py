# función para determinar si un caracter es un digito.
def es_digito(car):
    return "0" <= car <= "9"


# función para determinar si un caracter es una consonante...
def es_consonante(car):
    return car.lower() in "bcdfghjklmnñpqrstvwxyz"


# función principal del programa.
def principal():
    # inicialización de variables de resultados..
    r1 = r3 = r4 = 0
    r2 = None

    # contador de letras en una palabra...
    cl = 0

    # item 1: contador de dígitos y contador de minúsculas...
    cd = cm = 0

    # item 2: flag de dígito...
    sdig = False

    # item 3: contador de letras n y flag para la letra a...
    cn, sa = 0, False

    # item 4: flags para s y se...
    ss = sse = False

    # apertura del archivo de entrada, lectura del texto a procesar y cierre del archivo...
    m = open("entrada2.txt")
    texto = m.read()
    m.close()


    # ciclo general de procesamiento...
    for car in texto:
        # chequeo de final de palabra...
        if car in " .":
            # corte de palabra...
            # procesar solo si la palabra tenía al menos un caracter...
            if cl > 0:
                # item 1...
                if cd == 1 and cm == cl - 1:
                    r1 += 1

                # Item 2: menor longitud de las que tienen dígitos...
                if sdig and (r2 is None or cl < r2):
                    r2 = cl

                # item 3...
                if cn == 2 and sa:
                    r3 += 1

                # item 4...
                if sse and es_consonante(ul):
                    r4 += 1

            # resetear variables para la siguiente palabra...
            # contador de letras...
            cl = 0

            # item 1...
            cd = cm = 0

            # item 2...
            sdig = False

            # item 3...
            cn, sa = 0, False

            # item 4...
            ss = sse = False

        else:
            # caracter dentro de la palabra... contarlo...
            cl += 1

            # item 1...
            if es_digito(car):
                cd += 1
            elif car.islower():
                cm += 1

            # item 2...
            if es_digito(car):
                sdig = True

            # item 3...
            if car in "nN":
                cn += 1
            elif cl <= 4 and car in "aáAÁ":
                sa = True

            # item 4...
            if cl == 1 and car in "sS":
                ss = True
            else:
                if ss and car in "eéEÉ":
                    sse = True
                ss = False

            # guardar la última letra...
            ul = car

    # visualizacion de los resultados pedidos...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


# script principal.
if __name__ == "__main__":
    principal()
