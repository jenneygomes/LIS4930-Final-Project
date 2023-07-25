#In this project I wanted to create something for scuba divers to plan out different dive sites to visit in the Yucatan of Mexico utilizing input from the user to create an itinerary!
#
#Janet Gomez LIS 4930
#July 26 2023
#
import random
import time
from pprint import pprint

dive_count = 0
yes_no = ["Yes" , "No"]
diveAnswer = ["A" , "B" , "C" , "D" , "E" , "F"]

# El cielo beach - starfish
# Isla mujeres - whale sharks
# MUSA - sunken man made structures
# Paradise reef Cozumel - reef
# Cenote angelita - free diving
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


def createClass():  
  global dive_count
  print("On your dive would you rather see A. whale sharks or B. seastars?")
  print("Please enter A or B\n")
  a = input("> ")
  while a == "A" and a == "B":  
    print("invalid selection")
    a = input("> ")

  if a == "B":  
    diveCielo = "El Cielo Beach"
    diveIsla = ""
    dive_count += 1
  elif a == "A":  
    diveCielo = ""
    diveIsla = "Isla mujeres"
    dive_count += 2
    
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
    dive_count += 1

  elif b =="B":  
    diveMUSA = ""
    diveParadise = "Paradise Reef in Cozumel"
    dive_count += 2

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
    dive_count += 2


    
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

print(f"\nTotal number of tanks to bring: {dive_count}")

response = ""
def divesiteInfo(): 
  global response
  while response not in yes_no:  
    print("\n-----------------------")
    print("Do you want to learn about any of the dive sites?")
    print("Yes/No\n")
    response = input(">")

    if response == "Yes":  
      diveSite = ""
      while diveSite not in diveAnswer:  
        print("Please select from below:")
        print("A. El Cielo Beach")
        print("B. Isla Mujeres")
        print("C. MUSA")
        print("D. Paradise Reef")
        print("E. Cenote Angelita")
        print("F. Cenote El Jardin del Eden\n")

        diveSite = input(">")

        if diveSite == "A":  
            print("El Cielo beach is a popular snorkeling and diving spot near the coast of Cozumel. The Palancar Reef and Columbia Reef are located there with depths of around 40-30ft. It is given it's name, heaven or sky in Spanish,  due to the abundance of sea stars, similar to stars in the sky.")

        elif diveSite == "B":  
            print("Isla Mujeres is a small 5 mile long island not far from the coast of Cancun. It is a former fishing village that now caters to tourists and divers with a large array of dive sites available near the island. The most popular is Punta Negra Reef. Whale sharks are commonly spotted from mid May to mid September.")

        elif diveSite == "C":  
            print("Museo Subacuatico de Arte, 'MUSA', is a large underwater museum near Isla Mujeres near the coast of Punta Nizuc in Cancun. You are able to see sunken boats, cars, and over 500 permanent life-size sculptures made by Jason deCaires Taylor.")

        elif diveSite == "D":  
            print("Paradise Reef is located south of the Cruise Ship Pier, consisting of 3 long coral ridges. It reaches depths of 45ft and is a popular spot for snorkeling and night diving. There is much to see so it is a common 2 tank dive site.")

        elif diveSite == "E":  
            print("Cenote Angelita is about 20km south of Tulum. It is popular due to its depth of over 55km. Most dives are taken to a depth of 30-40m due to a cloud of hydrogen sulfate, where underneath the salt water begins and is very dark, appearing like an underwater forest at night. It is also popular for Technical diving.")

        elif diveSite == "F":  
            print("Cenote Jardin del Eden is one of the most popular cenotes in Mexico, about 40km north of Tulum. It is popular for snorkeling and cavern diving, and cliff jumping into the clear water. Its extensive cave system is perfect for cave diving and spotting unique wildlife like Mayan gobies.")

        else:
            print("Invalid selection, please enter A,B,C,D,E, or F.")
    elif response == "No":  
      print("Have a great dive trip!")

    else:  
      print("Invalid character, please enter 'Yes' or 'No'")

divesiteInfo()
