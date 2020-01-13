setx = {"apple", "mango"}
sety = {"mango", "orange"}
setz = {"mango"}
issubset = setx <= sety
print(issubset)
issuperset = setx >= sety
print(issuperset)
issubset = setz <= sety
print(issubset)
issuperset = sety >= setz
print(issuperset)
print("*****************")
print(setx.issubset(sety))
print(sety.issubset(setx))
print(setz.issubset(setx))
print(setz.issubset(sety))
print(setx.issuperset(sety))
print(setx.issuperset(setz))
print(setx.issuperset(setx))
print(setx.issuperset(setx))
