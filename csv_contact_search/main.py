# https://www.reddit.com/r/learnpython/comments/je33y9/help_with_text_file/

import csv

addressBook = {}

def loadAddressBook(f):
    with open(f) as book:
        reader = csv.reader(book)
        for row in reader:
            name = row[0]
            number = row[1]
            addressBook[name] = number

def searchContact(searchKey):
   for key, value in addressBook.items():
        if searchKey == key:
           print("Name:",key)
           print("Contact:",addressBook[key])
           return True
   print("Contact not found")
   return False

loadAddressBook("contacts.csv")
searchContact("John")
searchContact("Eliza")
searchContact("Doug")
searchContact("Someone else")