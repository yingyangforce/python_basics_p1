#---------------------------------------------------------
# | p6 - | input sequence of comma-separated nums,
#          generate/print a list and a tuple of said nums
#---------------------------------------------------------

numslist = input("Input a sequence of comma-separated numbers: ").split(', ')

if len(numslist) < 2: # if user didn't use spaces
    numslist = numslist[0].split(',')

print(f"List: {numslist}\nTuple: {tuple(numslist)}")

