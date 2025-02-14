import requests

res=requests.get('http://127.0.0.1:8000/app_furniture/getAll')
if res.status_code==200:
    objects=res.json()
    # for i in objects:
    #     print(i)
    list=[]
    
    #converting objects to dictionary and appending it
    for i in objects:
        dict={}
        dict.setdefault("id",i["id"])
        dict.setdefault("name",i["name"])
        dict.setdefault("price",i["price"])
        dict.setdefault("dop",i["dop"])
        dict.setdefault("quant",i["quant"])
        list.append(dict)
        
    print(list)
else:
    print("Sorry, Some connection error!!")

