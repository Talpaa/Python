from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def render(self)->str:
        pass

    @abstractmethod
    def getArea(self)->int | float:
        pass


class Quadrato(Forma):

    def __init__(self, lato: float) -> None:

        self.nome: str= 'Quadrato'
        self.lato: float = lato

    def render(self)->str:

        lato: int= int(self.lato)
        render_quad: str = '\n'

        for i in range(0, lato):

            for j in range(0, lato):

                if (i == 0)or(i == (lato-1)):

                    render_quad += '*'

                elif (j == 0)or(j == (lato-1)):

                    render_quad += '*'

                else:

                    render_quad += ' '

            render_quad += '\n'
        
        return render_quad[:-1]

    
    def getArea(self)->float:
        
        return self.lato ** 2
    

class Rettangolo(Forma):

    def __init__(self, altezza: float, base: float) -> None:
        
        self.nome: str = 'Rettangolo'
        self.altezza:float = altezza
        self.base: float = base

    def render(self) -> str:
        
        altezza: int= int(self.altezza)
        base: int = int(self.base)
        render_ret: str = '\n'

        for i in range(0, altezza):

            for j in range(0, base):

                if (i == 0)or(i == (altezza-1)):

                    render_ret += '*'

                elif (j == 0)or(j == (base-1)):

                    render_ret += '*'

                else:

                    render_ret += ' '

            render_ret += '\n'
        
        return render_ret[:-1]
    
    def getArea(self) -> float:
        
        return self.altezza * self.base
    
class Triangolo(Forma):

    def __init__(self, altezza: float, base: float) -> None:

        self.altezza: float = altezza
        self.base: float = base
        
    def render(self) -> str:
        
        altezza: int = int(self.altezza)
        base: int = int(self.base)

        render_tri: str = f'\n'

        for i in range(altezza-1):

            if i > 0:

                render_tri += f'*'
                if i > 1:
                    for k in range(i-1):

                        render_tri += ' '

            render_tri += f'*\n'

        for j in range(base):

            render_tri += f'*'

        return render_tri

    def getArea(self) -> float:
        
        return (self.altezza * self.base) / 2 

quad: Quadrato = Quadrato(4)

print(quad.render())
print(quad.getArea())

ret: Rettangolo = Rettangolo(altezza=4, base=8)

print(ret.render())
print(ret.getArea())

tri: Triangolo = Triangolo(altezza=4, base=4)

print(tri.render())
print(tri.getArea())
