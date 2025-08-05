shopping_list=[]

def show_menu():
    print("\n------ shooping list menu--------")
    print("\n 1.View the shopping list")
    print("\n 2.Add an item")
    print("\n 3.Remove an item")
    print("\n 4.clear list")
    print("\n5. Exit")

while True:
     show_menu()
     choice=input("Enter your choice(1-5):")
     if choice=="1":
         print("\n----shopping list---")
         if not shopping_list:
             print("Your shopping list is empty.")
         else:
             for index,item in enumerate(shopping_list):
                 print(f"{index+1}.{item}")
     elif choice=="2":
        item=input("Enter the item to add:")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

     elif choice=="3":
        item=input("Enter the item to remove:")
        if item in shopping_list:
          shopping_list.remove(item)
          print(f"{item} is removed from the shopping list.")

        else:
            print(f"{item}is  not in the shopping list.")

     elif choice=="4":
        shopping_list.clear()
        print("The shopping list has been cleared")

     elif choice=="5":
        print("Good bye!happy shopping")
        break
     else:
        print("Invalid choice!please try again")
        
            
              
        
     
          
