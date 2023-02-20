# how to replace characters!
def replace_char(that):
   this = "*" * (len(that)-4) + that[-4:]
   return this

def replace_all(that):
   this = "*" * len(that)
   return this


def calc_this(x, y):
   return x + y


print("hello class")

result = calc_this(3,1)
print(result)


print(replace_char("I don't want to you to see all the characters"))
print(replace_all("I don't want to you to see all the characters"))




