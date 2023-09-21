from datetime import date
# td=date.today()
# print(td.strftime("%b %d,%Y"))
td=date.today()
currentdate=td.strftime("Uploaded on %b %d, %Y")
#cd=f"Uploaded on {currentdate}"
print(currentdate)