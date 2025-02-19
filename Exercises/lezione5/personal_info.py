#3. Personal Info:

"""write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
    Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
    demonstrating how it handles these optional parameters.
    Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)"""


def build_profile(name: str, surname: str, occupation: str = None, location: str = None, age: str = None)->dict:

    personal_profile: str = f"{name.title()} {surname.title()}"

    if occupation != None:

        personal_profile = f"{personal_profile}, {occupation}"

    if location != None:

        personal_profile = f"{personal_profile}, {location}"

    if age != None:

        personal_profile = f"{personal_profile}, {age}"

    return personal_profile


print(build_profile("john", "doe", occupation="Developer", location="USA", age=30))

print(build_profile("john", "doe",location="USA", age=30))

print(build_profile("john", "doe", occupation="Developer", age=30))

print(build_profile("john", "doe", occupation="Developer", location="USA"))