print("欢迎使用kg换lbs")
weight=int(input("weight:"))
unit=input("(L)bs or(K)g:")
if unit=="L" :
    ti_g=weight*float(0.453)
    print(f"you are {ti_g:.2f}kilogram")

else:
    ti_g=weight*float(2.2)
    print(f"you are {ti_g:.2f} pound")


