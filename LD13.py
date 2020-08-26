'''
Created on Dec 9, 2019

@author: LDK_Guest
'''

L=[["Riga",500,5000]]

        
      
menu = {}
menu['1']="Pilsetas pievienosana saraksta sakuma." 
menu['2']="Pilsetas pievienosana saraksta beigas."
menu['3']="Pilsetas dzesana no saraksta sakuma."
menu['4']="Pilsetas dzesana no saraksta beigam."
menu['5']="Pilsetu kartosana pec iedzivotaju daudzuma augosa seciba."
menu['6']="Pilsetu kartosana pec iedzivotaju daudzuma dilstosa seciba."
menu['7']="Iziet no programmas"
while True: 
    options=menu.keys()
    for entry in options: 
        print (entry, menu[entry])
        
    selection = input("Izvelieties:")
    if selection =='1':        
        city = input("Ievadi pilsetu:")
        area = float(input("Ievadi platibu:"))
        people = int(input("Ievadi cilvekus"))
        L.append ([city,area,people])
        print(L)        
    elif selection == '2':
        city = input("Ievadi pilsetu:")
        area = float(input("Ievadi platibu:"))
        people = int(input("Ievadi cilvekus")) 
        L.insert(len(L),[city,area,people])
        print(L)                   
    elif selection == '3':
        if len(L) < 1:
            print("Saraksts ir tuks!")
        else:
            L.pop(0)
            print(L)
    elif selection == '4':
        L.pop(len(L)-1)
        print(L)

           
    elif selection == '7': 
        break
    else: 
        print ("Unknown Option Selected!") 


'''
print(D)
D.append(["Riga", 2000, 1000000])
print(D)

D.pop(0)
print(D)
'''