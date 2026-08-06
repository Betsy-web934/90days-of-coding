#write a python that prints a numbers 1-50, skips every multiple of 5 using continue and breaks after reaching 37

for i in range(1,51):
    if i % 5 == 0:
        continue
    print(i)
    if i == 37:
        break