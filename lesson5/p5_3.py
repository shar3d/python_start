l = []

l.append (23) # Adds element to the end of list
l.append (34)
b = [24, 67]
l.extend (b) # Extends list with elements, that will be added to the end
l.insert (1, 56) # Inserts element by index in the list
l.append (34)
l.remove (34) # Removes first found element in the list specified here
l.pop (0) # Removes element specified by index and returns it. Removes last element in the list, if index is not specified
print (l.index (56)) # Returns index of element in the list
print (l.count (34)) # Returns number of elements in the list specified here
l.sort () # Sorts list using specified function. Sorts in ascending order, if not specified
l.reverse () # Reverses list
l.clear () # Clears list

print(l)