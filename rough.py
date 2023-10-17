'''
# Team ID:          eYRC#GG#3450
# Theme:            GeoGuide (GG)
# Author List:      ASHWANI SONI
# Filename:         INV_PY_solution.py
# Functions:        addItem, DeleteItem, main
# Global variables: List
'''

# Made a Dictionary to maintain all Items
List = {}

def addItem(Item_name, quantity):
    '''
    Purpose:
    ---
    To make update for ADD operation in list and print the respective condition

    Input Arguments:
    ---
    `Item_name` :  [ str ]
        Item_name store the name of Item which is added to list

    `quantity` :  [ int ]
        quantity stores how many units are added

    Returns:
    ---
    none

    Example call:
    ---
    addItem("Servo", 7)

    '''

    if Item_name in List:
        # update the list
        List[Item_name] += quantity
        # print UPDATED Item $item_name$
        print("UPDATED Item {}".format(Item_name))
    else:
        # update the list 
        List[Item_name] = quantity
        # print ADDED Item $item_name$
        print("ADDED Item {}".format(Item_name))

def deleteItem(Item_name, quantity):
    '''
    Purpose:
    ---
    To make update for Delete operation in list and print the respective condition

    Input Arguments:
    ---
    `Item_name` :  [ str ]
        Item_name store the name of Item which is to be deleted from list

    `quantity` :  [ int ]
        quantity stores how many units are to be deleted

    Returns:
    ---
    none

    Example call:
    ---
    DeleteItem("Servo", 7)
    '''
    if Item_name in List:
        if List[Item_name]<quantity:
            # print Item $item_name$ could not be DELETED
            print("Item {} could not be DELETED".format(Item_name))
        else:
            # update the list
            List[Item_name] -= quantity
            # print DELETED Item $item_name$
            print("DELETED Item {}".format(Item_name))
    else:
        # print Item $item_name$ does not exist
        print("Item {} does not exist".format(Item_name))

# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        List = {}
        # take the n input values
        n = int(input())
        # intializing the empty list
        List = {}
        # Loop to input the present intial items in List
        for idx in range(n):
            data = input()
            # spliting the data provided int Item_name and queantity
            Item_name, quantity = data.split(' ')
            # typecast quantity to int
            quantity = int(quantity)
            #Adding the value to List
            if Item_name in List:
                List[Item_name] += quantity
            else:
                List[Item_name] = quantity

        
        # Taking input q (number_of_operation)
        number_of_operation = int(input())

        # Loop for each operation
        for idx in range(number_of_operation):
            # Taking input for each operation performed
            query = input()
            # unpacking and splitting the query opreation
            operation, Item_name, quantity = query.split(' ')
            # typecasting the quantity
            quantity = int(quantity)
            if operation=="ADD":
                #if the operation is of ADD
                addItem(Item_name, quantity)
            else:
                # If the operation if Delete
                deleteItem(Item_name, quantity)

    # calculating total items in List
    total_Items = 0
    for Item in List:
        # Loop in the list adding quantity of every Item
        total_Items += List[Item]

    print("Total Items in Inventory: {}".format(total_Items))