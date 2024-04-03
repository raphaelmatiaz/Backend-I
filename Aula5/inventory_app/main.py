import click

arrayOfItems = []

@click.command()
@click.option("--option", prompt= "Choose an option: ", help="[1] Add Item    [2] Remove Item    [3] Export List")
def mainMenu(option):
    print("")
    print("[1] Add Item    [2] Remove Item    [3] Export List")
    print("")

    while True:
        option = input("Choose an option: ").strip()
        
        if option != '1' and option != '2' and option != '3':
            print("ERRO: Choose a valid option.")
        else:
            if option == '1':
                addItem()
            if option == '2':
                removeItem()
            if option == '3':
                pass

#-------------------------------------------------------------------


@click.command()
@click.argument()
def addItem():
    item = input("Choose an option: ").strip()
    arrayOfItems.append(item)
    return arrayOfItems
    

#-------------------------------------------------------------------


@click.command()
@click.argument()
def removeItem():
    for i in arrayOfItems:
        print(i)
    
    
    item = input("Choose an item remove: ").strip()

    if item in arrayOfItems:
        arrayOfItems.remove(item)
        print(f"Item {item} removed from list")
    else:
        print(f"Item {item} is NOT in the list")
        return arrayOfItems

#-------------------------------------------------------------------

#@click.command()
#@click.argument()
#def exportList(list, filename):



if __name__ == "__main__":
    mainMenu()
