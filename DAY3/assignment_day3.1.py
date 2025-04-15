list1 = [1,2,3, [1,2,3,[3,4],2]]
out = []
def final_list(lst):
    for i in lst:
        if type(i) is int:
            out.append(i)
        else:
            final_list(i)
final_list(list1)
print(out)
