fname =input("enter the file: ")
if len(fname) < 1 : fname ="clown.txt"
hand = open(fname)

di =dict()
for lin in hand:
    lin = lin.rstrip()
    wds=lin.split()
    for w in wds:
        di[w]=di.get(w,0)+1

print("dictionary is ",di )
x=di.items()
print("........")
print("di.items:", x)
y =sorted(di.items())
print("............")
print("the sorted items is " ,y[:5])

tmp =list()
for k,v in di.items():
    print(k,v)
    newt =(v,k)
    tmp.append(newt)
print("flipped",tmp)
tmp=sorted(tmp,reverse=True)
tmv=sorted(tmp)
print("reverse sorted",tmp)
print("sorted",tmv)

