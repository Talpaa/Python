"""
Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words 
e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente 
(ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.
"""

import re

#crea una lista di parole levando spazi e punteggiatura
def rim_punt(text):
    new_words = []
    text = re.split("\s", text) #crea una lista di parole prese da una stringa separate da uno spazio
    for word in text:
        w = re.sub(r'[^\w\s]','',word) #rimuove tutto tranne spazi e parole
        w = re.sub(r'_','',w) #rimuove anche gli underscore
        new_words.append(w)
    return new_words


def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:

    dizionario_parole: dict = {}
    n: int = 0
    text = text.lower()
    text = rim_punt(text)

    for i in text:

        for j in stopwords:

            if j in text:
                
                text.remove(j)

    for key in text:

        if key not in dizionario_parole:

            dizionario_parole[key] = 1

        else:

            n = dizionario_parole[key]
            n += 1
            dizionario_parole[key] = n
            n = 0



    return(dizionario_parole)


stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."

print(word_frequency(text, stopwords))