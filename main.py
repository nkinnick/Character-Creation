RACES = ["Human", "Elf", "Dwarf"]
#*******************************************************
class genericCharacter:

  RACES = ["Human", "Elf", "Dwarf"]

  #init method is when you create a new genericCharcter object from the genericCharcter class
  def __init__(self, name, boast, race):
    self.name = name
    self.boast = boast
    self.race = race

  def giveGreeting(self):
      return ("Hello, my name is " + str(self.name))

  def giveBoast(self):
    return (boast)
  
#*******************************************************    
#Ask user to provide a character nameand a boast
name = input("Enter your character's name: ")
boast = input("Enter your character's boast: ")
print("Character race options: " + str(genericCharacter.RACES))

#defining race as blank value to be input by the user
race=""
while race not in RACES:
  #Allows user to try again
  race = input("Enter your character's race: ")
  if race not in RACES:
    print ("Error. Race must be Human, Elf, or Dwarf. Capitialization matters. Please try again.")
    
#If user types invalid race, sends an error message



#Create new object (playerCharcter) from a class (genericCharacter) 
#Pass in the input parameters for the init method
playerCharacter = genericCharacter(name, boast, race)
print(playerCharacter.name)

greeting = playerCharacter.giveGreeting()
print(greeting)

taunt = playerCharacter.giveBoast()
print("Boast: " + taunt)

race = playerCharacter.race
print("Race: " + race)