thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print(type(thisdict))

thisdict = dict(name = "Beket", age = 22, country = "Kazakhstan")
print(thisdict)


x = thisdict["name"]
print(x)

x = thisdict.get("name")
print(x)

print(thisdict.keys())

print(thisdict.values())

print(thisdict.items())

print("name" in thisdict)
print("class" in thisdict)

thisdict = {
  "brand": "Hyundai",
  "model": "Sonata",
  "year": 2010
}
print(thisdict['year'])
thisdict["year"] = 2022
print(thisdict['year'])


thisdict.update({"model": "Grandeur"})
print(thisdict)

thisdict["color"] = "white"
print(thisdict)

thisdict.update({'engine_volume': 2.5})
print(thisdict)


thisdict.pop('color')
print(thisdict)

thisdict.popitem()
print(thisdict)


del thisdict['year']
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Hyundai",
  "model": "Sonata",
  "year": 2010
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)


for keys, values in thisdict.items():
    print(keys, values)


dict_copy = thisdict.copy()
print(dict_copy)

dict_copy1 = dict(thisdict)


uni_dict = {
    "uni1": {
        "name": "KBTU",
        "rank": 1
    },
     "uni2": {
        "name": "SDU",
        "rank": 2
    },
     "uni3": {
        "name": "IITU",
        "rank": 3
    }
}
print(uni_dict)


uni1 = {
        "name": "KBTU",
        "rank": 1
}
uni2 = {
        "name": "SDU",
        "rank": 2

}
uni3 = {
    "name": "IITU",
    "rank": 3

}
uni_dict1 = {
    "uni1": uni1,
    "uni2": uni2,
    "uni3": uni3
}

print(uni_dict1)