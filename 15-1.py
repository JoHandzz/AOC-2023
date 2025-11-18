# test = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'


with open('15-data.txt', 'r') as f:
    data = f.read()
    lst = [string for string in data.split(',')]

out = []

for string in lst:
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val = val % 256
    out.append(val)


print(sum(out))

