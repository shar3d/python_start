d = {'test' : 1, 'test_2' : "TeST"} # First method for creation of dictionaries
print(d)

d = dict (short='dict', longer='dictionary') # Second method for creation of dictionaries
print(d)

d = dict ([(23, 34), (56, 87)])
print(d)

d = dict.fromkeys(['a', 'b', 'c'], 1) # Third  method for creation of dictionaries
print(d)

d = {a : a ** 2 for a in range(7)} # Fourth method for creation of dictionaries
print(d)