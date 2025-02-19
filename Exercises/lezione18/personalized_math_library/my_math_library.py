class FractionError(Exception):
    """Eccezione di base per errori nelle operazioni con le frazioni."""
    pass

class NoneNumDenError(FractionError):
    """Eccezione sollevata quando o il numeratore o il denominatore non sono stati settati."""
    def __init__(self):
        super().__init__("Il numeratore o il denominatore devono essere settati.")

class NullDenominatorError(FractionError):
    """Eccezione sollevata quando il denominatore è zero."""
    def __init__(self):
        super().__init__("Il denominatore non può essere zero.")

class UnsupportedOperationError(FractionError):
    """Eccezione sollevata quando un'operazione non è supportata."""
    def __init__(self, operation):
        super().__init__(f"L'operazione '{operation}' non è supportata.")

class PersonalizedMathLibrary:

    def __init__(self, numeratore: float, denominatore: float) -> None:
        
        self.numeratore: float = float(numeratore)
        
        if denominatore == 0:

            raise NullDenominatorError
        
        else:
        
            self.denominatore: float = float(denominatore)

    def set_numeratore(self, numeratore: str):

        self.numeratore = numeratore

    def set_denominatore(self, denominatore: str):

        if denominatore == 0:

            raise NullDenominatorError
        
        else:
        
            self.denominatore = denominatore

    def get_numeratore(self):

        numeratore: float = self.numeratore
        return numeratore
    
    def get_denominatore(self):

        denominatore: float = self.denominatore
        return denominatore

    def semplifica(self)->int:

        if (self.get_numeratore() == None)or(self.get_denominatore() == None):

            raise NoneNumDenError
        
        else:

            i: int = 0

            numeratore: float = self.get_numeratore()
            denominatore: float = self.get_denominatore()

            if numeratore < denominatore:

                i = numeratore

            elif denominatore < numeratore:

                i = denominatore

            else:

                self.set_numeratore(numeratore)
                self.set_denominatore(denominatore)

                return f'{numeratore} {denominatore}'

            while (i > 1):

                if ((numeratore) % i == 0)and((denominatore) % i == 0):

                    numeratore /= i
                    denominatore /= i        

                elif(numeratore == 1)or(denominatore == 1):

                    self.set_numeratore(numeratore)
                    self.set_denominatore(denominatore)

                    return f'{numeratore} {denominatore}'
                
                i -= 1

            self.set_numeratore(numeratore)
            self.set_denominatore(denominatore)
            return f'{numeratore} {denominatore}'
        
    def add_fractions(self, frazione: 'PersonalizedMathLibrary'):

        numeratore: float = 0.0
        denominatore: float = 0.0


        if self.get_denominatore() == frazione.get_denominatore():

            numeratore = self.get_numeratore() + frazione.get_numeratore()
            denominatore = self.get_denominatore()

            return f'{numeratore} {denominatore}'
        
        elif (self.get_denominatore() == 1):

            denominatore = frazione.get_denominatore()

            numeratore = (self.get_numeratore() * denominatore) + frazione.get_numeratore()
            return f'{numeratore} {denominatore}'
        
        elif (frazione.get_denominatore() == 1):

            denominatore = self.get_denominatore()

            numeratore = (frazione.get_numeratore() * denominatore) + self.get_numeratore()
            return f'{numeratore} {denominatore}'
        
        elif((frazione.get_denominatore() % self.get_denominatore())== 0):

            denominatore = frazione.get_denominatore()

            numeratore = (self.get_numeratore() * (denominatore / self.get_denominatore())) + frazione.get_numeratore()

            return f'{numeratore} {denominatore}'

        elif((self.get_denominatore() % frazione.get_denominatore())== 0):

            denominatore = self.get_denominatore()

            numeratore = self.get_numeratore() + (frazione.get_numeratore() * (denominatore / frazione.get_denominatore()))

            return f'{numeratore} {denominatore}'

        else:

            denominatore = self.get_denominatore() * frazione.get_denominatore()

            numeratore = (self.get_numeratore() * (denominatore / self.get_denominatore()))+(frazione.get_numeratore() * (denominatore / frazione.get_denominatore()))

            return f'{numeratore} {denominatore}'
        
    def sub_fractions(self, frazione: 'PersonalizedMathLibrary'):

        numeratore: float = 0.0
        denominatore: float = 0.0


        if self.get_denominatore() == frazione.get_denominatore():

            numeratore = self.get_numeratore() - frazione.get_numeratore()
            denominatore = self.get_denominatore()

            return f'{numeratore} {denominatore}'
        
        elif (self.get_denominatore() == 1):

            denominatore = frazione.get_denominatore()

            numeratore = (self.get_numeratore() * denominatore) - frazione.get_numeratore()
            return f'{numeratore} {denominatore}'
        
        elif (frazione.get_denominatore() == 1):

            denominatore = self.get_denominatore()

            numeratore = self.get_numeratore() - (frazione.get_numeratore() * denominatore)
            return f'{numeratore} {denominatore}'
        
        elif((frazione.get_denominatore() % self.get_denominatore())== 0):

            denominatore = frazione.get_denominatore()

            numeratore = (self.get_numeratore() * (denominatore / self.get_denominatore())) - frazione.get_numeratore()

            return f'{numeratore} {denominatore}'

        elif((self.get_denominatore() % frazione.get_denominatore())== 0):

            denominatore = self.get_denominatore()

            numeratore = self.get_numeratore() - (frazione.get_numeratore() * (denominatore / frazione.get_denominatore()))

            return f'{numeratore} {denominatore}'

        else:

            denominatore = self.get_denominatore() * frazione.get_denominatore()

            numeratore = (self.get_numeratore() * (denominatore / self.get_denominatore()))-(frazione.get_numeratore() * (denominatore / frazione.get_denominatore()))

            return f'{numeratore} {denominatore}'
        
    def multiply_fractions(self, frazione: 'PersonalizedMathLibrary'):

        numeratore: float = self.get_numeratore() * frazione.get_numeratore()

        denominatore: float = self.get_denominatore() * frazione.get_denominatore()

        return f'{numeratore} {denominatore}'
    
    def divide_fractions(self, frazione: 'PersonalizedMathLibrary'):

        numeratore: float = self.get_numeratore() * frazione.get_denominatore()

        denominatore: float = self.get_denominatore() * frazione.get_numeratore()

        return f'{numeratore} {denominatore}'
    
    def equal_fractions(self, frazione: 'PersonalizedMathLibrary'):

        self.semplifica()
        frazione.semplifica()

        if (self.numeratore == frazione.numeratore)and(self.denominatore == frazione. denominatore):

            return True
        
        else: return False