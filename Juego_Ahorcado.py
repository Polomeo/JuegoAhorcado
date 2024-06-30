# Proyecto del día 5
# Juego del Ahorcado
from random import choice
from os import system

# Variables
palabras = ['kocher', 'bertola', 'kirminson', 'backhaus', 'davier']
palabra_seleccionada = ''
letras_correctas = []
letras_incorrectas = []
vidas_restantes = 6
jugando = True


def seleccionar_palabra_aleatoria(lista):
    '''
    Retorna una palabra al azar de la lista
    '''
    return choice(lista)


def estado_palabra(palabra, *args):
    '''
    Muestra la palabra en el estado actual
    (args son las letras que el usuario ya adivinó)
    '''
    # Si no se enviaron letras correctas
    if len(args) == 0:
        return '* ' + ' _ ' * len(palabra) + ' *'
    else:
        palabra_lista = list(palabra)
        palabra_compuesta = [
            letra if letra in args else '_' for letra in palabra_lista]

    return '* ' + ' '.join(palabra_compuesta) + ' *'


def solicitar_letra():
    '''
    Retorna una letra solicitada al jugador
    '''
    letra_ingresada = input('¿Qué letra querés probar?: ').lower()
    while not letra_ingresada.isalpha() or len(letra_ingresada) != 1:
        letra_ingresada = input('Tiene que ser una letra (a-z): ')

    return letra_ingresada


def verificar_letra(palabra, letra):
    '''
    Verifica si la letra es correcta o no
    '''
    if letra in palabra:
        return True
    return False


def verificar_victoria(palabra):
    '''
    Verifica si el usuario ha ganado
    '''
    if '_' not in palabra:
        return True
    return False


def mostrar_letras_arriesgadas(lista_letras_incorrectas):
    '''
    Muestra al usuario un mensaje con la lista de palabras incorrectas
    '''
    return print('Lista de letras arriesgadas: ' + '-'.join(lista_letras_incorrectas))


def mostrar_vidas_restantes(cantidad_vidas):
    '''
    Muestra en pantalla la cantidad de vidas restantes
    '''
    monigote = ''

    match cantidad_vidas:
        case 6:
            monigote = '''
                        ----------
                        |        |
                        |        
                        |      
                        |       
                        |
                        ---_________
                        '''
        case 5:
            monigote = '''
                        ----------
                        |        |
                        |        0
                        |      
                        |       
                        |
                        ---_________
                        '''
        case 4:
            monigote = '''
                        ----------
                        |        |
                        |        0
                        |        I 
                        |       
                        |
                        ---_________
                        '''
        case 3:
            monigote = '''
                        ----------
                        |        |
                        |        0
                        |      / I 
                        |       
                        |
                        ---_________
                        '''
        case 2:
            monigote = '''
                        ----------
                        |        |
                        |        0
                        |      / I \\
                        |       
                        |
                        ---_________
                        '''
        case 1:
            monigote = '''
                        ----------
                        |        |
                        |        0
                        |      / I \\
                        |       / 
                        |
                        ---_________
                        '''
        case 0:
            monigote = '''
                        ----------
                        |        |
                        |        0  * ouch! *
                        |      / I \\
                        |       / \\
                        |
                        ---_________
                        '''
        case _:
            monigote = '''
                        ----------
                        |        |
                        |        
                        |      
                        |       
                        |
                        ---_________
                        '''

    return print(f'{monigote}\nVidas restantes: {cantidad_vidas}')


# Game Loop
palabra_seleccionada = seleccionar_palabra_aleatoria(palabras)

while jugando:

    # Muestra la información del turno
    system('cls')  # limpia la consola
    print(''.center(70, '*'))
    print(' Juego del Ahorcado '.center(70, '*'))
    print(''.center(70, '*'))
    mostrar_vidas_restantes(vidas_restantes)
    mostrar_letras_arriesgadas(letras_incorrectas)
    print(estado_palabra(palabra_seleccionada, *letras_correctas))
    letra_seleccionada = solicitar_letra()

    # Verifica si la letra es correcta
    if verificar_letra(palabra_seleccionada, letra_seleccionada):
        letras_correctas.append(letra_seleccionada)
    else:
        if letra_seleccionada not in letras_incorrectas:
            letras_incorrectas.append(letra_seleccionada)
            vidas_restantes -= 1
        else:
            print(''.center(70, '*'))
            print('¡Esta letra ya la dijiste antes! Probá otra.')

    # Verifica si el usuario se quedó sin vidas
    if vidas_restantes == 0:
        system('cls')  # limpia la consola
        print(' ¡Juego finalizado! '.center(70, '*'))
        mostrar_vidas_restantes(vidas_restantes)
        print(f'¡Se te agotaron las oportunidades!')
        print(f'La palabra era: {palabra_seleccionada.capitalize()}')
        jugando = False
        break

    # Verifica si el usuario ganó
    if verificar_victoria(estado_palabra(palabra_seleccionada, *letras_correctas)):
        system('cls')  # limpia la consola
        print(' ¡Felicitaciones! '.center(70, '*'))
        monigote_ganador = '''
                        ----------
                        |        |
                        |         
                        |             * yeah! *
                        |       \\ 0 / 
                        |         I
                        ---_____/___\\_
                        '''
        print(
            f'{monigote_ganador}\nLa palabra era: {palabra_seleccionada.capitalize()}')
        print(f'Ganaste quedándote {vidas_restantes} vidas restantes!')
        jugando = False
        break

print(' ¡Gracias por jugar! '.center(70, '*'))
