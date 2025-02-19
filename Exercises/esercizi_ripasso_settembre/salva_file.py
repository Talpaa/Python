def memorizza_file(lista: list[float])->None:

    message: str = ''
    blo: int = 0
    num_blocchi: int = 1000
    new_list: list = []

    for file in lista:

        #File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.

        com_file: float = (file / 100.0) * 80.0

        message = f'File di {file} byte compresso in {com_file} byte e memorizzato. '
        new_list.append(com_file)

        if com_file%512 > 0:

            blo = (com_file // 512) + 1

        else:

            blo = (com_file // 512)

        if blo <= num_blocchi:

            num_blocchi -= blo

            message += f'Blocchi usati: {int(blo)}. Blocchi rimanenti: {int(num_blocchi)}. '

        else:

            print(f'Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.')
            return

        print(message)


memorizza_file([1100, 20000, 1048576, 512, 5000])