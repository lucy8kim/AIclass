def volume(cone, r=20, h=10):
    if cone == 0:
    
        return 3.14*r*r*h
    if cone == 1:
        return (3.14*r*r*h)/3

print(volume(0, r=20, h=10))


print(volume(1, r=20, h=10))

