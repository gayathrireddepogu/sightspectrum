##fromkeys()----------
##a={"a","b","c"}
##b=(5)
##c=dict.fromkeys(a,b)
##print(c)
##print(type(a))
##print(type(b))
##
##a=("a","b","c")
##b=(5)
##c=dict.fromkeys(a,b)
##print(c)
##

##a={["a","b","c"]}
##b={(5)}
##c=dict.fromkeys(a,b)
##print(c)

##a=("a","b","c")
##b={(5,6)}
##c=dict.fromkeys(a,b)
##print(c)

##a={("a"),("b"),("c")}
##b=(5,3,5)
##c=dict.fromkeys(a,b)
##print(c)
##
####a={"a","b","c"}
##b=(5)
##c=dict.fromkeys(a,b)
##print(c)
##
##
##

##get()-------------
##car = {( "brand":"Ford"), ("model": "Mustang"), ("year": 1964)}
##x = car.get("model")
##print(x)

##car = {( "brand"):("Ford"), ("model"): ("Mustang"), ("year"): (1964)}
##x = car.get("model")
##print(x)
##items()----------------------------
##car = {"brand": "Ford", "model": "Mustang", "year": 1964}
##x = car.items()
##print(x)

##car = {( "brand"):("Ford"), ("model"): ("Mustang"), ("year"): (1964)}
##print(car["brand"])
##



##var={"name":(1,{"surname":["s","m","n"]})}
##print(var)
##var = {"name":[1:{"surname":["s","m","n"]}]}
##print(var)

##var = {"name":[1:{"surname":["s","m","n"]}]}
##print(var)


##var = {"name":{1:{"surname":["s","m","n"]}},"jega":{1:{"surname":["s","m","n"]}}}
##var["jega"][1]["surname"][1]="jega"
##print(var)       

##
##var = {"name":{1:{"surname":["s","m","n"]}},"jega":{1:{"surname":["s","m","n"]}}}
##print(var)



##x={"name":"gayathri","age":"20"}
##y=json.loads(x)
##print(Y["name"])
##
##

##import json--------------------
##var = '{"country":"india"}'
##print(type(var))
##output = json.loads(var)
##print(type(output))

##import json
##var = '{"country":"india"}'
##print(type(var))
##output = json.dumps(var)
##print(type(output))
##

##pop items()--------------------
##car = {"brand": "Ford",
##
##       "model": "Mustang",
##       "year": 1964}
##
##car.popitem()
##
##print(car)
##
##
##var = {"marriage": "effort",
##       "divya": "ramesh",
##       "year": 2021}
##var.popitem()
##print(var)
##

##setdefault()----------------

##var = {"marriage": "effort",
##       "divya": "ramesh",
##       "year": 2021}
##var.setdefault("2021")
##print(var)
##update()------------------------------
##values(()-----------------


a= {"marriage": "effort",
       "divya": "ramesh",
       "year": 2021}
x=a.values()
print(x)






































































