from typing import Any 
#print(open("lezione15/file.txt",mode="r", encoding="utf-8"))

#reader = open("lezione15/file.txt",mode="r", encoding="utf-8")

#il file viene chiuso quanto finisce di eseguire tutte le istruzioni del blocco with
with open("lezione15/file.txt",mode="r", encoding="utf-8") as reader:

    print(reader)

try:

    reader.readline()
    print('Sono nella try')
    print(reader)
    raise Exception('Eccezione')

except Exception:

    print('Sono nella except')

finally:

    print('Sono nella finally')
    reader.close()


class ContexManager:

    def __enter__(self):

        print('Ciao sono nell\'enter')

        return self
    
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):

        if exc_type is not None:

            print('Eccezione')

        return False
    
try:

    with ContexManager() as cm:

        print('Ciao')
        print(cm)
        
except Exception as e:

    print(f'Errore: {e}')