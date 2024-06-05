try:
    print(x)
except:
    print("an error occured")
try:
    print(x)
except NameError:
    print("x is not defined ")
except:
    print("x is defined")
try:
    x="22"
    print(x)
except:
    print("x is defined")
else:
    print("there is no error")
finally:
    print("finished")
y=-5
if y<0:
    raise Exception("no negative numbers allowed")