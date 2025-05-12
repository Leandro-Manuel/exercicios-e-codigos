def chat_table():
    print("Decimal\tHexadecimal\tBinário\t\tCaractere")
    # Limitando a um intervalo mais prático (ASCII estendido 0-255)
    for i in range(256):  # Alterado para 256 para ASCII estendido
        decimal = i  # Corrigido para usar o valor atual de i
        hexadecimal = hex(i)[2:].upper()  # Remove '0x' e coloca em maiúsculas
        binary = bin(i)[2:]  # Remove '0b'
        try:
            character = chr(i)
            # Para caracteres não imprimíveis, podemos mostrar um placeholder
            if i < 32 or i == 127:
                character = '[controle]'
        except:
            character = '[inválido]'
        print(f'{decimal}\t{hexadecimal}\t\t{binary:>8}\t{character}')

chat_table()