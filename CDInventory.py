#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# VJackson, 2021-Aug-06, 
#------------------------------------------#

# Declare variabls

key = ['ID', 'Title', 'Artist']
dctLst = []
strChoice = '' # User input

# Get user Input
print('The Magic CD Inventory\n')

#  1.Display menu allowing the user to choose:
    
while True:
    print(
        '[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory'
        )
    print(
        '[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit'
        )
    strChoice = input('l, a, i, d, s or x: ').lower()  
    # convert choice to lower case at time of input
    print()


# 5. Exit the program if the user chooses so

    if strChoice == 'x':
        #
        break


# 4. load existing data

    if strChoice == 'l':
        with open('CDInventory.txt', 'r') as file:
            for line in file:
                ftemp = line.strip().split(',')
                dctLst.append(
                    {key[0]: ftemp[0],
                     key[1]: ftemp[1],
                     key[2]: ftemp[2]}
                    )
        file.close()
        print("File Loaded! \n")

# 2. Add data to the table 2d-list each time the user wants to add data

    elif strChoice == 'a':
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dctLst.append({
            "ID": intID,
            "Title": strTitle,
            "Artist": strArtist
            })

# 3. Display the current data to the user each time
#    the user wants to display the data

    elif strChoice == 'i':
        print(
            f"{'*ID' : <10}",
            f"{'*Title' : <20}",
            f"{'*Artist' : <20}", sep=' | ',
            end='\n'
            )
        for value in dctLst:
            print(
                f"{value['ID'] : <10}",
                f"{value['Title'] : <20}",
                f"{value['Artist'] : <20}",
                sep=' | ',
                end='\n'
                )
        print('\n')

    elif strChoice == 'd':
        dlt = input("What is the ID of CD you want to delete?")
        for i in range(len(dctLst)):
            dltLst = [key for key in dctLst if key['ID'] == dlt]
        for element in dltLst:
            if element in dctLst:
                dctLst.remove(element)
        print("Choice deleted! \n")
            
    elif strChoice == 's':
        with open('CDInventory.txt', 'w') as wrtfile:
            for i in dctLst:
                filetemp = str(i['ID'] + ',' + i['Title'] +',' + i['Artist'] + '\n')
                wrtfile.write(filetemp)
        wrtfile.close()
        print("File Saved! \n")
    else:
        print('Please choose either l, a, i, d, s or x!')
