import random
import time
from pprint import pprint
# el cielo beach - starfish
# isla mujeres - whale sharks
# MUSA - sunken man made structures
# paradise reef Cozumel - reef
# cenote angelita - free diving
# Cenote El Jardin del Eden - cave diving and mayan gobies

class diver:  
  def __init__(self, Dname, Dcielo, Disla, Dmusa, Dparadise, Dlength, Dangelita, Djardin):  
    self.name = Dname
    self.cielo = Dcielo
    self.isla = Disla
    self.musa = Dmusa
    self.paradise = Dparadise
    self.length = Dlength
    self.angelita = Dangelita
    self.jardin = Djardin

  def getCielo(self):  
    return self.cielo
  def getIsla(self):  
    return self.isla
  def getMusa(self):  
    return self.musa
  def getParadise(self):  
    return self.paradise
  def getName(self):  
    return self.name
  def getLength(self):  
    return self.length
  def getAngelita(self):  
    return self.angelita
  def getJardin(self):  
    return self.jardin  

def createClass():  
  
  print("On your dive would you rather see A. whale sharks or B. seastars?")
  print("Please enter A or B\n")
  a = input("> ")
  while a == "A" and a == "B":  
    print("invalid selection")
    a = input("> ")

  if a == "B":  
    diveCielo = "El Cielo Beach"
    diveIsla = ""
  elif a == "A":  
    diveCielo = ""
    diveIsla = "Isla mujeres"
    
  print("\n-----------------------")
  print("Would you rather see A. an underwater museum with hundreds of man made statues or B. a large coral reef with thousands of colorful fish?")
  print("Please enter A or B\n")
  b = input("> ")
  while b == "A" and b =="B":  
    print("invalid character")
    b = input("> ")

  if b =="A":  
    diveMUSA = "MUSA underwater museum"
    diveParadise = ""

  elif b =="B":  
    diveMUSA = ""
    diveParadise = "Paradise Reef in Cozumel"

  print("\n-----------------------")
  print("Would you rather become A. free dive certified or B. cave certified?")
  print("Please enter A or B\n")
  c = input("> ")
  while c == "A" and c =="B":  
    print("invalid character")
    c = input("> ")

  if c =="A":  
    diveAngelita = "Cenote Angelita"
    diveJardin = ""

  elif c =="B":  
    diveAngelita = ""
    diveJardin = "Cenote Jardin"


    
  print("\n-----------------------")
  d = input("Press enter to find out how long your dive trip will be")
  print("Generating...")
  time.sleep(0.5)
  diveLength = random.randint(3,7)
  print("Your dive trip will be ", diveLength, " days long!\n")

  print("\n-----------------------")
  print("What is your name?\n")
  diverName = input("> ")
  print("\n-----------------------")
  print("Here's your dive itinerary. Have a great dive,", diverName,"!")

  return(diverName, diveLength, diveCielo, diveIsla, diveMUSA, diveParadise, diveAngelita, diveJardin)

class_data = createClass()

diverName, diveLength, diveCielo, diveIsla, diveMUSA, diveParadise, diveAngelita, diveJardin = class_data

diveTrip = diver(diverName, diveCielo, diveIsla, diveMUSA, diveParadise, diveLength, diveAngelita, diveJardin)
pprint(vars(diveTrip))

# character = diver(class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5], class_data[6])
#pprint(vars(character))
