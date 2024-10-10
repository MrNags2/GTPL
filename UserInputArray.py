Bus=[]
seats=int(input("how Many seats u wnated to Book"))
for i in range(seats):
    name=input("Enter the Next Name")
    Bus.append(name)
print("The seats Booked Succesfully for :",Bus)

name=input("Enter the Name you wanted to search")
if(name in Bus):
    print("Booked SuccessFully")
else:
    print("Data Not Found")
    
#to cancel the Ticket
delete=input("Enter the Name to cancel the ticket")
if(delete in Bus):
    Bus.remove(delete)
    print("Deleted")
else:
    print("Data Not Found")
print(Bus)

       