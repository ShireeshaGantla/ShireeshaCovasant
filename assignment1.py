d1={'ok':1,'nok':2}
d2={'ok':2,'new':3}
d_union = d1 | d2
d_intersection = {key: d1[key] for key in d1.keys() & d2.keys()}
d_minus = {key: d1[key] for key in d1.keys() - d2.keys()}
d_merge=d1.copy()
for key1 in d2.keys():
    if key1 in d2.items(): 
        for key1 in merge:
            d_merge[key1] += d2[key1]
    else :
        d_merge[key1] = d2[key1]
print(d_union)
print(d_intersection)
print(d_minus)
print(d_merge)
