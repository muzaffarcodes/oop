# Problem1
class Mashinalar():
    def __init__(self,nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi):
        self.name = nomi
        self.model = modeli
        self.type = turi
        self.color = rangi
        self.weight = ogirligi
        self.oil = yoqilgisi
        self.price = narxi
        
    def showInfo(self):
        print(f""" |-Welcome to CarWorld-| 
			       |Car name: {self.name}| 
				   |Model: {self.model}|
				   |Type: {self.type}|
				   |Color: {self.color}|                  
                   |Weight: {self.weight} kilos|
				   |Oil type: {self.oil}|
				   |Car price: {self.price} $|
""")

class Sports_Cars(Mashinalar):
    def __init__(self,nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi):
        super().__init__(nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi)
    def showerInfo(self):
        super(showInfo,self)
        
sport_car = Sports_Cars("Audi R8","V10","Sports-Cars","Qizil",1595,"AI-95",197000)
sport_car.showInfo()

class PickUp(Mashinalar):
    def __init__(self,nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi):
        super().__init__(nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi)
    def showerInfo(self):
        super.showInfo()
        
pickup_cars = PickUp("Ford","Ranger","PickUp-Truck","Qora",1200,"AI-200",30000)
pickup_cars.showInfo()

class Sedan(Mashinalar):
    def __init__(self,nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi):
        super().__init__(nomi,modeli,turi,rangi,ogirligi,yoqilgisi,narxi)
    def showerInfo(self):
        super.showInfo()

sedan_car = Sedan("Mercedes-Benz","S-Class","Sedan","Oq",2275,"AI-210",116300)
sedan_car.showInfo()
