from datetime import datetime
class Otdel:

    def __init__(self, nazvanie_otdela, kol_prilavkov, kol_prodavcov, nomer_zala):
        self.nazvanie_otdela = nazvanie_otdela
        self.kol_prilavkov = kol_prilavkov
        self.kol_prodavcov = kol_prodavcov
        self.nomer_zala = nomer_zala
        self.date = datetime.today()

    def redo_name(self, newname):
        self.name = newname

class Cloth(Otdel):
    '''potomok_otdela'''

    def __init__(self, type_of_clothing, color, fabric, gender, otdel1):
        super().__init__(otdel1.nazvanie_otdela, otdel1.kol_prilavkov, otdel1.kol_prodavcov, otdel1.nomer_zala)
        self.type_of_clothing = type_of_clothing
        self.color = color
        self.fabric = fabric
        self.gender = gender
        self.data_registration = datetime.today()

    def redo_name(self, newtype_of_clothing):
        self.type_of_clothing = newtype_of_clothing

    def add_color(self, amount):
        self.color += amount

class Product(Otdel):
    '''potomok_otdela'''
    def __init__(self,type_of_product, otdel1, expiration_date, price,name_otdela):
        super().__init__(otdel1.nazvanie_otdela, otdel1.kol_prilavkov, otdel1.kol_prodavcov, otdel1.nomer_zala)
        self.type_of_product = type_of_product
        self.expiration_date = expiration_date
        self.price = price
        self.name_otdela = name_otdela
        self.data_registration = datetime.today()

    def redo_name(self, newtype_of_clothing):
        self.type_of_clothing = newtype_of_clothing

    def add_type_of_product(self, amount):
        self.type_of_product += amount
