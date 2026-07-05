#list --> account
account = [
    {'owner' : 'Aishwary','balance':500, 'DOB': '2 June 2000'}, #contain disctionaries in list
    {'owner' : 'Om','balance':1500, 'DOB': '2 Feb 2002'},
    {'owner' : 'Pratiksh','balance':2500, 'DOB': '22 June 2000'}
]

#adding new details
account.append({'owner' : 'Shubham','balance':300, 'DOB': '12 June 2001'})

#printing all info present in account
for acc in account:
    print(acc['owner']," with DOB:",acc['DOB'], " has Rs.",acc['balance'], 'in account')

print(account[0].get("pin")) #return None as no key with name 'pin' is present in account 

rich = [acc ["owner"] for acc in account if acc['balance'] >500 and '2000'in (acc['DOB']) ] #comprehension data filteration

print("Rich elder(s): ",rich)

#negative testing handling using try/except 
try:
    pin = account[0]['pin']

except KeyError:
    print("Hey, pin is not set for your database. Making default pin for all account as '0000'")
    for acc in account:
        acc['pin'] = "0000" #setting pin = int(0000) will only return 0 instead of 0000 hence used string

#file handling using with & open => used with function to open and automatically close the file as open file leaks the resources
with open("note.txt","w") as f: # "w" use for writing
    for acc in account:
        f.write(str(acc)+"\n") #to write the lines in file we need to convert dict to str

with open("note.txt","r") as f: # "r" use for reading the file contnent
    content = f.read()

print(content)



