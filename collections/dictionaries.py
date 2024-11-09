# Dictionaries

band = {
    "vocals":"plant",
    "guitar":"page"
}

band2 = dict(vocals="plant",guitar="page")

print(band)
print(band2)

print(type(band))
print(len(band2))

# Access Items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list of values
print(band.values())

# list of key and value pair as a tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverable"
band.update({"base":"JPJ"})

print(band)

# Remove items
print(band.pop("base"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)


band["drums"] = "Bonham"
print(band)

# Delete and clear
del band["drums"]
print(band)


band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band    # Create a reference
# print("Bad Copy")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

# try below, above one not a exact copy dictionary
band2 = band.copy()
print("Good Copy")
band2["drums"] = "Dave"
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

# nested dictionaries
member1 = {
    "name":"plant",
    "instrument":"vocals"
}

member2 = {
    "name":"page",
    "instrument":"guitar"
}

band = {
    "member1":member1,
    "member2":member2
}
print(band)
print(band["member1"]["name"])