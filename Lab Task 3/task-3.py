class ModelBaseAgent:
    def __init__(self,temp,FilePath="file.txt"):
        self.drjaharaat = temp
        self.FilePath = FilePath

    def retrive_content(self):
        try:
            with open(self.FilePath, 'r') as file:
                content = file.readlines()
            return content
        
        except FileNotFoundError:
            with open(self.FilePath, 'w') as file:
                file.write("")
            return False
        
    def store_content(self,string):
        with open(self.FilePath, 'a') as file:
            file.write(string + "\n")
        return True
    

    def neurons(self,abhi_ka_temp):
        self.abhi_ka_drjaharaat = abhi_ka_temp

    def operation(self):
        if self.abhi_ka_drjaharaat > self.drjaharaat:
            string = f"{self.abhi_ka_drjaharaat} , AC ON KRDO"
            self.store_content(string)
            return "AC ON KRDO"
        
        else:
            string = f"{self.abhi_ka_drjaharaat} , AC OFF KRDO"
            self.store_content(string)
            return "AC OFF KRDO"
        
    def operator(self):
        content = self.retrive_content()
        if content:
            list_of_temps = [ int(i.split(",")[0].strip()) for i in content]
            list_of_actions = [ i.split(",")[1].strip() for i in content]
            idex_of_abhi_ka_temp = None

        if content and self.abhi_ka_drjaharaat in list_of_temps:
            idex_of_abhi_ka_temp = list_of_temps.index(self.abhi_ka_drjaharaat)
            action = list_of_actions[idex_of_abhi_ka_temp]
            print(f"{self.abhi_ka_drjaharaat} ==> {action} From Memory")
        else:
            print(f"{self.abhi_ka_drjaharaat} ==> {self.operation()} ")

rooms = {
    "living room" : 33,
    "bed room" : 25,
    "kitchen" : 29,
    "bath room" : 27,
    "Store room" : 30,
    "Dining room" : 28,
    "Living room" : 32,
    "Guest room" : 26,
    "New room" : 40,
    "Extra room" : 89,
}


for room,temp in rooms.items():
    print(f"{room} --> ",end=" ")
    model = ModelBaseAgent(23)
    model.neurons(temp)
    model.operator()
    print()


            

    


    

    