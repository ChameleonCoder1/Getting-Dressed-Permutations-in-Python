from getting_dressed import get_dressed
#Read in data from space_separated_permutations.csv (output of create_inputs.py)
permutations=[]
with open("./space_separated_permutations.csv") as f:
    perm=f.readlines()
    perm=[p.replace("\n","") for p in perm]
    permutations.append(perm)

permutations=permutations[0]

#if you just want the first 50
#for perm in permutations[0:50]:
#    print("Input: ")
#    print(perm)
#    print("Output: ")
#    print(get_dressed(perm))

for perm in permutations:
    this_perm =  get_dressed(perm)
    if not "fail" in this_perm:
        print("Successful Input: {} is {} ".format(perm, get_dressed(perm)))
