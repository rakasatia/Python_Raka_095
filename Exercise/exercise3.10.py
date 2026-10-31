mountains = ["Merapi", "Semeru", "Rinjani"]
print(mountains)                 

mountains.append("Bromo")
print(mountains)             

mountains.insert(1, "Sumbing")
print(mountains) 

del mountains[0]
print(mountains) 

popped_mountain = mountains.pop()
print(popped_mountain)   

mountains.remove("Semeru")
print(mountains)

mountains.append("Lawu")
mountains.append("Slamet")
print(sorted(mountains))  

mountains.sort()
print(mountains)                 

mountains.reverse()
print(mountains)                 

print(len(mountains))          