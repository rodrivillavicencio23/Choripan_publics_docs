canalobj = int(input())
canalactual = int(input())
#canal 2 arriba
dif1 = abs(canalobj - canalactual)
dif2= 0
if canalobj < canalactual:
    dif2 = abs(100-canalactual+canalobj)
elif canalactual < canalobj:
    dif2 = abs(100-canalobj+canalactual)
print(dif1)
print(dif2)
#xdd
if canalactual < canalobj:
    if dif1 < dif2:
        print(dif1,"veces arriba")
    elif dif1 > dif2:
        print(dif2,"veces abajo")
elif canalobj < canalactual:
    if dif1 < dif2:
        print(dif1,"veces abajo")
    elif dif1 > dif2:
        print(dif2,"veces arriba")

