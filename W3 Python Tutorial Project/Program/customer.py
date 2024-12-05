cardict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"],
}

print(cardict)
print()

persondict = dict(name = "John", age = 36, country = "Norway")
print(persondict)
print()

for x, y in cardict.items():
    print(x,':',y)