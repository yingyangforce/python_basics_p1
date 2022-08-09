#---------------------------------------------------------
# | p6 - | input sequence of comma-separated nums,
#          generate/print a list and a tuple of said nums
#---------------------------------------------------------

numslist = input("Input a sequence of comma-separated numbers: ").split(', ')

print(f"List: {numslist}\nTuple: {tuple(numslist)}")

