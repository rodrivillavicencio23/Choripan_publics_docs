a ="00,01,02,03,04,05,06,07,08/10,11,12,13,14,15,16,17,18/20,21,22,23,24,25,26,27,28/30,31,32,33,34,35,36,37,38/40,41,42,43,44,45,46,47,48/50,51,52,53,54,55,56,57,58"

b = a.split("/")
print(b)
chelsea = []
for xd in b:
    print(xd)
    f = xd.split(",")
    print(f)
    chelsea.append(f)


print(chelsea)


print(chelsea[0][1])