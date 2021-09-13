# Write Python 3 code in this online editor and run it.
def sort_arr(L):
    t = [L[0]]
    for i in range(1,len(L)):
        n_added = True
        for n in t:
            if L[i]<n:
                t.insert(t.index(n),L[i])
                n_added = False
                break
        if n_added:
            t.append(L[i])
    return t

l = [1,2,8,6,3,2]
print(sort_arr(l))