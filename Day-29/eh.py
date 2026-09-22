'''
try:
    print(10/0)
except ZeroDivisionError:
    print("unable to divide a number with zero")

else:
    print("No error")

finally:
    print("end of the program")

try:
    d={1:2,3:5}
    print(d[8])
    l=[1,2,3,4,5]
    print(l[7])
    print('a'+7)
    a=int(input("enter the number: "))
    print(a)
    print(10/0)
except NameError:
    print("var is not defind")
except ValueError:
    print("enter the proper value")
except TypeError:
    print("use same datatypes")
except IndexError:
    print("index is out of range")
except KeyError:
    print("key is not present")
except ZeroDivisionError:
    print("unable to divide a number with zero")
else:
    print("no error")
finally:
    print("end of the program")


try:
    d={1:2,3:5}
    print(d[8])
    l=[1,2,3,4,5]
    print(l[7])
    print('a'+7)
    a=int(input("enter the number: "))
    print(a)
    print(10/0)
except (NameError,ValueError,TypeError,IndexError, KeyError,ZeroDivisionError) as e:
    print("error occured:",e)
else:
    print("no error")
finally:
    print("end of the program")

try:
    d={1:2,3:5}
    print(d[8])
    l=[1,2,3,4,5]
    print(l[7])
    print('a'+7)
    a=int(input("enter the number: "))
    print(a)
    print(10/0)
except Exception as e:
    print("error occured:",e)
else:
    print("no error")
finally:
    print("end of the program")
'''
try:
    amount=int(input("enter the amount: "))
    if amount<0:
        raise Exception("amount needs to be greaterthan 0")
except Exception as e:
    print("error occured:",e)
else:
    print("no error")
finally:
    print("end of the program")