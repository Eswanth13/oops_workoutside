import sys

from alternatecapitalize import Altcap
class Stringmaliputation(Altcap):


    def DoTheStringOperation(self,choice,string):
        if choice ==1:
            print(self.reverse_cap_upper(string))
        elif choice ==2:
            print(self.reverse_cap_lower(string))


alt=Stringmaliputation()
string = str(input('enter a string : ' ))
try:
    choice = int(input('enter your choice, 1 for upper and 2 for lower : ' ))
except ValueError:
    print("Choice should be only numbers \nBy default upper is selected")
    choice =1
except NameError:
    print("Choice should be only numbers \nBy default upper is selected")
    choice =1
finally:
    print("Here is your result\n")

alt.DoTheStringOperation(choice,string)