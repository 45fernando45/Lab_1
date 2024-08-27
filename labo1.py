


def vol_num(numero):
    numero_str = str(numero) #cadena
    numero_invertido_str = numero_str[::-1]

    numero_invertido = int(numero_invertido_str)
    return numero_invertido

entrada_usuario = input("Introduce un número: ")

if entrada_usuario.isdigit():
    numero = int(entrada_usuario)
    resultado = vol_num(numero)
    print(f'Primer Nro: {numero}')
    print(f'Número invertido: {resultado}')


