class User:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 cf: str,
                 email: str,
                 login_attempts: int = 0):
        
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.cf: str = cf
        self.email: str = email
        self.login_attempts: int = login_attempts


    def greet_user(self):

        return f'\nCiao {self.first_name} {self.last_name}, come stai?'
    
    def increment_login_attempts(self):
        
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        
        self.login_attempts = 0
        return self.login_attempts

    def __str__(self) -> str:
        
        return f'\n\nUSER \nName: {self.first_name},\n'\
             + f'Surname: {self.last_name}\n'\
             + f'Age: {self.age}\n'\
             + f'CF: {self.cf}\n'\
             + f'Email: {self.email}\n'
    
class Admin(User):

    def __init__(self, 
                 first_name: str, 
                 last_name: str, 
                 age: int, 
                 cf: str, 
                 email: str, 
                 login_attempts: int = 0,
                 privileges: list = ["can add post", "can delete post", "can ban user"]):
        
        super().__init__(first_name, last_name, age, cf, email, login_attempts)

        self.privileges =  privileges
        
    def __str__(self) -> str:

        message: str = super().__str__()

        message += f'\nQuesto profilo è admin e i suoi privileggi sono:\n'

        for i in self.privileges:

            message += f'    -{i}\n'

        return message
    
user1: User = User('Mario', 'Rossi', 42, 'MRRSS65S67M126L', 'Mario.Rossi@gmail.com')

user2: User = User('Luigi', 'Verdi', 37, 'LGVRD65S67M126L', 'Luigi.Verdi@gmail.com')

user3: User = User('Rosa', 'Esposito', 54, 'RSSPST65S67M126L', 'Rosa.Esposito@gmail.com')

print(user1)
print(user1.greet_user())

print(user2)
print(user2.greet_user())

print(user3)
print(user3.greet_user())


print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())

user1.reset_login_attempts()

print(user1.login_attempts)

admin1: Admin = Admin('Francesco', 'Proietti', 72, 'FRNPRT32I43K638P', 'Fra.Pro@gmail.com')

print(admin1)