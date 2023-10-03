from datetime import datetime
a=(input(" enter your name"))
b=(input(" enter your phone number"))

list= '''
RICE           RS 12/KG
SUGAR          RS 40/KG
IDLI RAVVA     RS 45/KG
MAGGIE         RS 12/PACK
SUNFLOWER OIL  RS 112/LITER
BOOK           RS 12
TEA POWDER     RS 200/KG
COFFEE POWDER  RS 350/KG
GROUNDNUTS     RS 52/KG
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':12,'sugar':40,'idli rava':45,
'maggie':12,'sunflower oil':112,'book':12,
'tea powder':200,'coffee':350,'groundnuts':52}
option=(input(" enter 1 for list of items"))
if option =="1":
    print(list)
else:
    print("invalid input")
for i in range(len(items)):
    inp1=int(input(" enter 1 to buy and enter 2 for exit"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item=input("enter your items")
        quantity=int(input("enter quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print("your item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i print the bill")
    if inp == 'yes':
        pass
        if finalprice!=0:
            print(25*"=","Imam Supermarket",25*"=")
            print(27*" ","Nizampatnam",25*" ")
            print("name: ",a,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',19*" ",'price')
        for i in range(len(pricelist)):
            print(i+1,11*" ",ilist[i],12*" ",qlist[i],22*" ",plist[i])
        print(75*"-")
        print(50*" ",'totalamount:','RS',totalprice)
        print("gst amount",50*" ",'RS',gst)
        print(75*"-")
        print(50*" ",'finalprice:','RS',finalprice)
        print(75*"-")
        print(25*" ","THANKS FOR VISITING")
        print(75*"-")




           
