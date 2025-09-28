"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter name: ")
while True:
    print("(H)ello")
    print("(G)oodye")
    print("(Q)uit")
    choice = input(">>> ").upper()
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    elif choice == "Q":
        break
    else:
        print("Invalid choice")
print("Finished")


