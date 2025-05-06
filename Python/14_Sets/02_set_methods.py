s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
s.add(322)
s.add(12)
s.remove(23)    # Throws an error
s.discard(34535) # no error if element not found
print(s)
