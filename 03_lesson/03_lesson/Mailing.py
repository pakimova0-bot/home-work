class Mailing:
    def __init__(self, to_Address, from_Address, cost, track):
        self.to_Address = to_Address
        self.from_Address = from_Address
        self.cost = cost
        self.track = track


    def __str__(self):
        return f"отправление {
            self.track}"; из 
        {self.from_address}; в 
        {self.to_address}; стоимость 
        {self.cost} 
        рублей; 




