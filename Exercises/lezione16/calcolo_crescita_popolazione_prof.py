# Definizione della classe base Specie
class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome  # str: nome della specie
        self.popolazione = popolazione_iniziale  # int: popolazione iniziale
        self.tasso_crescita = tasso_crescita  # float: tasso di crescita percentuale annuo

    def cresci(self):
        """Calcola la popolazione dell'anno successivo."""
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))  # Aggiorna la popolazione

    def anni_per_superare(self, altra_specie: 'Specie') -> int | str:
        """Determina in quanti anni la popolazione di questa specie supererà quella dell'altra."""
        anni = 0  # int: Contatore degli anni
        while self.popolazione <= altra_specie.popolazione:  # Loop finché questa popolazione non supera l'altra
            self.cresci()  # Incrementa la popolazione di questa specie
            altra_specie.cresci()  # Incrementa la popolazione dell'altra specie
            anni += 1  # Incrementa il contatore degli anni
            if anni > 1000:  # Impostiamo un limite per evitare loop infiniti
                return f"{self.nome} non supererà mai {altra_specie.nome}"  # Ritorna un messaggio se il limite è raggiunto
        return anni  # Ritorna il numero di anni necessari
    
    def getDensita(self, area_kmq: float) -> int | str:
        """Calcola gli anni necessari per raggiungere una densità di 1 individuo per km quadrato."""
        if not area_kmq:  # Controlla se l'area è specificata
            return "Area non specificata"  # Ritorna un messaggio di errore
        anni = 0  # int: Contatore degli anni
        while self.popolazione / area_kmq < 1:  # Loop finché la densità è inferiore a 1 individuo/km²
            self.cresci()  # Incrementa la popolazione
            anni += 1  # Incrementa il contatore degli anni
        return anni  # Ritorna il numero di anni necessari

# Sottoclasse per Bufalo Klingon
class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Sottoclasse per Elefante
class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")