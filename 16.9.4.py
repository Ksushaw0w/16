class Customers:
    def __init__(self, first_name, second_name, city):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city

    def __str__(self):
        return f"{self.first_name} {self.second_name}. {self.city}"

    def get_guest(self):
        return f'{self.first_name} {self.second_name}. г.{self.city}'

costomer_1 = Customers('Алекснадр', 'Муромов', 'Новосибриск')
costomer_2 = Customers('Петр', 'Красилов', 'Калининград')
costomer_3 = Customers('Илья', 'Олейников', 'Сыктывкар')

guest_list = [costomer_1, costomer_2, costomer_3]

for guest in guest_list:
    print(guest.get_guest())


