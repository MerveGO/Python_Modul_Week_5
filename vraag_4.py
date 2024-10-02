class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year


class OffRoadVehicle(Vehicle):
    def __init__(self,make,model,year,four_wheel_drive):
        super().__init__(make,model,year)
        self.four_wheel_drive=four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self,make,model,year,max_speed):
        super().__init__(make,model,year)
        self.max_speed=max_speed

o_r_v=OffRoadVehicle("Jeep","Wrangler",2023,True)
s_c=SportsCar("Ferrari","488 GTB",2022,210)

print(f"Arazi Araci:\nMarka:{o_r_v.make}\nModel:{o_r_v.model}"
      f"\nYil:{o_r_v.year}\nDort Tekerden Cekis:{'Evet'if o_r_v.four_wheel_drive else 'Hayir'}\n")

print(f"Spor Araba:\nMarka:{s_c.make}\nModel:{s_c.model}"
      f"\nYil:{s_c.year}\nMaksimum Hiz:{s_c.max_speed}")