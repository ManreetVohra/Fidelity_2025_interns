#1 First Task
#Add 17% gst on items with price greater than 100

price_list=[100,90,70,110,120,60,200,95,135]
gst=17
newprice_list=[]

for i in range(len(price_list)):
    if(price_list[i]>100):
        new_price=price_list[i]+price_list[i]*(gst/100)
        newprice_list.append(new_price)
    else:
        newprice_list.append(price_list[i])

print(newprice_list)