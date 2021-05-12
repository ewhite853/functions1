romanInventions = {
    "Aquaducts": "Bridges carrying water",
    "Sanitation": "Clean water and adequate sewage disposal",
    "Roads": "Wide ways leading from anywhere to Rome"
    }

menu = [
    "List inventions",
    "Look up an invention",
    "Add an invention",
    "Edit an invention",
    "Delete an invention",
    "Quit"]
def displayMenu(m):
    print("\nWhat did the Romans ever give us?\n")
    for i in range(len(m)):
        print(str(i+1), m[i])
    print()
def getOption():
    a = int(input("Please enter a number: "))
    return a
def listInventions(ri):
    print("\nThe Romans gave us...\n")
    for i in ri.keys():
        print(i)

loopMenu = True

while loopMenu:
        displayMenu(menu)
        loopMenu = False

        option = getOption()
        if option == 1:
        listInventions(roamanInventions)

        if option 
        
