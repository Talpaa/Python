#from typing import Any
class Room:

    def __init__(self,
                 id: str,
                 floor: int,
                 seats: int) -> None:
        
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_id(self) -> str:
        return self.id


    def __str__(self) -> str:
        
        return f'Room(id={self.id}, floor{self.floor}, seats={self.seats})'


class Building:

    def __init__(self,
                 name: str,
                 address: str,
                 num_floors: int,
                 rooms: list[Room] = []) -> None:
        
        self.name: str = name
        self.address: str = address
        self.num_floors: int = num_floors
        self.rooms: list[Room] = rooms

    def get_num_floors(self) -> int:
        return self.num_floors
    
    def get_rooms(self) -> list[Room]:

        return self.rooms

    def add_room(self, room: Room):

        if room not in self.rooms\
            and (room.get_floor() <= self.get_num_floors()):

            self.rooms.append(room)

    def __str__(self) -> str:
        
        return f'{self.name.capitalize()} @ {self.address}'
    
smi = Building(name = 'SMI', address='via abc 7424', num_floors=5)

smi.add_room(Room(id='472', floor=3, seats=28))

print(smi.get_num_floors())
