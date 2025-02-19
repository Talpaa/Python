from restaurant import Restaurant

from restaurant import Ice_cream_stand

r1: Restaurant = Restaurant(name = 'La Vecchia Roma', cuisin_type = 'Romana')

r2: Restaurant = Restaurant(name = 'Dumpling Bar', cuisin_type = 'Cinese')

r3: Restaurant = Restaurant(name = 'La Cucaracha', cuisin_type = 'Messicana')

Restaurant.describe_restaurant(r1)

Restaurant.describe_restaurant(r2)

Restaurant.describe_restaurant(r3)

Restaurant.open_restaurant(r1)


r1.set_number_served(r1.num_serv)


r1.set_number_served(r1.num_serv)


r1.set_number_served(r1.num_serv)

g1: Ice_cream_stand = Ice_cream_stand(name = 'Fatamorgana', cuisin_type = 'Gelateria', flavors = ['crema', 'yougurt', 'cocco'])

g1.flavors_list()