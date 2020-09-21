pa = float(input("Pressure in kPa: "))
psi = pa / 6.89475729
mm = pa * 760 / 101.325
atm = pa / 101.325

print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mm" % (mm))
print("Atmosphere pressure: %.2f atm." % (atm))