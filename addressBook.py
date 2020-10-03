#This holds the street address
class Address:
   def __init__(self):
      self.street = "street"
      self.city = "city"
      self.state = "state"
      self.zip = int(00000)
   
   def setStreet(self):
      print("House number and street: ")
      self.street = input()

   def setCity(self):
      print("City: ")
      self.city = input()

   def setState(self):
      print("State abbreviation: (i.e., CA, ID, NV) ")
      self.state = input()
      self.state = self.state.upper()

   def setZip(self):
      print("Zipcode:")
      self.zip = input()

   def setAddress(self):
      self.setStreet()
      print()
      self.setCity()
      print()
      self.setState()
      print()
      self.setZip()
      print()

   #This display the address
   def displayAddress(self):
      print(self.street)
      print("{}, {} {}".format(self.city, self.state, self.zip))
      return ""

#This is a class that holds basic conctact info about a person
class Person:
   def __init__(self):
      self.name = "name"
      self.phoneNumber = int(5555555555)
      self.email = "name@domain.com"
      self.address = Address()
      
   def createPerson(self):
      self.setName()
      print()
      self.setPhoneNumber()
      print()
      self.setEmail()
      print()
      self.setPersonAddress()

   def setName(self):
      print("Please enter the persons full name: ")
      self.name = input()

   def setPhoneNumber(self):
      print("Please enter {}'s phone number: ".format(self.name))
      self.phoneNumber = input()

   def setEmail(self):
      print("Please enter {}'s email: ".format(self.name))
      self.email = input()
   
   def setPersonAddress(self):
      print("Please enter {}'s address-- ".format(self.name))
      self.address.setAddress()

   #This displays the person as a whole and includes their address
   def displayPerson(self):
      print(self.name)
      print(self.phoneNumber)
      print(self.email)
      print(self.address.displayAddress())

#This is a namable book that can hold multiple people
class AddressBook:
   def __init__(self):
      self.name = "Name"
      self.people = [Person()]
      self.numPeople = int(-1) 

   def bookName(self):
      print("What is the name of the address book? ")
      self.name = input()

   def personInput(self, index):
      print("Enter your persons information-- ")
      self.people[index].createPerson()
      self.numPeople += 1 #Every person who is created adds to the index

   def displayPerson(self, index):
      print("Here is {}'s information-- ".format(self.people[index].name))
      self.people[index].displayPerson()

   #A search funtion could be implemented here
   #A print to file function could be implemented here

def main():

   #Variables
   index = 0
   book1 = AddressBook()

   book1.bookName()
   book1.personInput(index)

   print("Would you like to add another person? (y/n)")
   addPeople = input()
   addPeople = addPeople.lower()
   while (addPeople != "y" and addPeople != "n"):
      print("Please respond with \'y\' or \'n\':")
      addPeople = input()
      addPeople = addPeople.lower()
   print()

   while (addPeople == 'y'):
      index += 1
      book1.people.append(Person())
      book1.personInput(index)
      #This could be simplified and reduced using a function
      print("Would you like to add another person? (y/n)")
      addPeople = input()
      addPeople = addPeople.lower()
      while (addPeople != "y" and addPeople != "n"):
         print("Please respond with \'y\' or \'n\':")
         addPeople = input()
         addPeople = addPeople.lower()
   print()

   #This displays all the information that was entered
   for x in range(index + 1):
      book1.displayPerson(x)

   return 0

main()