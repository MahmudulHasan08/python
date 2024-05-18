mySet = {1,3,4,5}

# set intersection 
mySet2 = mySet & {1,7}
mySet3 = mySet & {1,3}

print(mySet2)
print(mySet3)

#set union

mySet4 = mySet | {1,4}
mySet5 = mySet | {2,5,4,9}

print(mySet4)
print(mySet5)
print(mySet)

# set differences

mySet6 = mySet - {1,5}

print(mySet6)

mySet7 = mySet - {3,4}

print(mySet7)

mySet8 = mySet - {1,5,3,4}
print(mySet8)