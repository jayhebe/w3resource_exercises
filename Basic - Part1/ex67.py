kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi" % psi)
print("The pressure in millimeter of mercury: %.2f mmHg" % mmhg)
print("Atmosphere pressure: %.2f atm." % atm)
