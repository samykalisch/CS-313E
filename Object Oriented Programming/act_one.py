class Main_Controller:
   
  def ask_beverage(self):
    
    #gives optinos
    print('Make your choice:')
    print('1. Espresso')
    print('2. Americano')
    print('3. Latte Macchiato')
    print('4. Black Tea')
    print('5. Green Tea')
    print('6. Yellow Tea')
    
    #makes sure a correct input is given
    while True:
      options = {1: Expresso(),2: Americano(),3: Latte_Macchiato(),\
        4: Black_Tea(), 5 : Green_Tea(), 6 : Yellow_Tea() }
      user_input = input()
      if user_input.isnumeric():
        choice = int(user_input)
        if 0< choice < 7:
          return options[choice]
      print('Please select a correct value.')   
        
  def ask_condiments(self, name):
    #gives optinos
    print(f'Choose your units of {name}: (between 0 and 3)')
    
    while True:
      user_input = input()
      if user_input.isnumeric():
        choice = int(user_input)
        if 0<=choice < 4:
          return choice
      print('Please select a correct value.')  
  


class Beverage:
  
  def __init__(self, name):
    self.name = name
    self.units_of_milk = 0
    self.units_of_sugar= 0
 
  @property
  def units_of_milk(self):
    return self.__units_of_milk
  
  @units_of_milk.setter
  def units_of_milk(self, value):
    if 0 <= value <= 3:
      self.__units_of_milk = value 
    else:
      print('Value needs to be between 0 and 3')
  
  @property
  def units_of_sugar(self):
    return self.__units_of_sugar
    
  @units_of_sugar.setter
  def units_of_sugar(self, value):
    if 0 <= value <= 3:
      self.__units_of_sugar = value 
    else:
      print('Value needs to be between 0 and 3')
  
  def __str__(self):
    return 'Beverage: ' + str(self.name )+'\n'+\
           'Units of milk: ' + str(self.__units_of_milk)+'\n'+\
           'Units of sugar: ' + str(self.__units_of_sugar)   
                   
class Expresso(Beverage):
  
  def __init__(self):
    super().__init__('Expresso')
    
class Americano(Beverage):
  def __init__(self):
    super().__init__('Americano')
    
class Latte_Macchiato(Beverage):
  def __init__(self):
    super().__init__('Latte Macchiato') 
    
class Black_Tea(Beverage):  
  def __init__(self):
    super().__init__('Black Tea') 
    
class Green_Tea(Beverage): 
  def __init__(self):
    super().__init__('Green Tea') 
    
class Yellow_Tea(Beverage): 
  def __init__(self):
    super().__init__('Yellow Tea') 


#Gets the input from the user and prints it out to the standard output.  
def main():
  while True:
    #initiate machine
    machine = Main_Controller()
    
    #ask for bverage and complements
    beverage = machine.ask_beverage()
    print()
    beverage.units_of_milk = machine.ask_condiments('milk')
    print()
    beverage.units_of_sugar = machine.ask_condiments('sugar')
    
    #print outcome
    print('\n'+str(beverage)+ '\nThanks for your purchase!!!\n')
  
  
if __name__ == '__main__':
  main()
