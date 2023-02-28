'''
Same of 3.1 but with validation of variables, exceptions about their types.
'''

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error! Please insert a NUMERIC value.")
    quit() # we have to put this here because of way python does things will fail on the print of variables. 

basis = 40
if h <= basis:
    print(h*r)
else:
    print((((h - basis) * r)* 1.5) + (basis * r))