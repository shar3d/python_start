l = []

l.append (23) # Adds element to the end of list
l.append (34)
b = [24, 67]
l.extend (b) # Extend list with elements, that will be added to the end
l.insert (1, 56) # Insert element by index in the list
l.append (34)
l.remove (34) # Remove first found element in the list specified here
l.pop (0) # Remove element specified by index and returns it. Remove last element in the list, if index is not specified
print (l.index (56)) # Return index of element in the list
print (l.count (34)) # Return number of elements in the list specified here
l.sort () # Sort list using specified function. Sort in ascending order, if not specified
l.reverse () # Reverse list
l.clear () # Clear list

print(l)