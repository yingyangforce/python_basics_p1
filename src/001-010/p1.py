#------------------------------------------------
# | p1 - | print provided str in specific format
#------------------------------------------------
# >Twinkle, twinkle, little star,               
# >    How I wonder what you are!               
# >        Up above the world so high,          
# >        Like a diamond in the sky.           
# >Twinkle, twinkle, littlle star,              
# >    How I wonder what you are
#------------------------------------------------

sample = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

## 0:30 31:57 58:85 86:112 113:143 144:169

## i'd rather hard print spaces than find the
## length of each section to do padding
## 
## please don't @ me

print(f"{sample[0:30]}")
print(f"    {sample[31:57]}")
print(f"        {sample[58:85]}")
print(f"        {sample[86:112]}")
print(f"    {sample[113:143]}")
print(f"{sample[144:169]}")

