# Define the valid_phone_number function
def valid_phone_number(phoneNumber):
    phoneNumber = str(phoneNumber)
    if len(phoneNumber) != 10 or not phoneNumber.isdigit():
        return False
    return True

# Define the personne dictionary
personne = {
    2222222222: "Mohamed",
    1111111111: "amal",
    3333333333: "Khadijah",
    4444444444: "Abdullah",
    5555555555: "Rawan",
    6666666666: "Faisal",
    7777777777: "Layla"
}


def searchByNumber(phoneNumber):
    if not valid_phone_number(phoneNumber):
        print("This is an invalid number")
        return

    if(phoneNumber in personne):
         print(personne.get(phoneNumber))
    else:
         print("Sorry, the number is not found ")


def searchByName(pname):
    found = False
    for phone, name in personne.items():
       if(name == pname):
           print(phone)
           found = True
    if not found:
        print("Sorry, this name "+ pname + " is not found")

def add_personne(name, phone_number):
    personne.update({phone_number: name})

searchByNumber(2222222222)
add_personne('rayen',2222222288)
searchByName('rayen')