# Made By Simo
# 31/03/2026
import math
C1 = float(input("inserisci la misura del primo cateto: "))
C2 = float(input("inserisci la misura del primo cateto: "))
Area = (C1*C2)/2
Ipotenusa = math.sqrt(C1*C1 + C2*C2)
Perimetro = C1 + C2 + Ipotenusa
print("L'area del rettangolo è " + str (Area)+ " Cm2")
# Ho usato str perchè volevo specificare che era in cm, quindi mi serviva converti da float a stringa
print("L'ipotenusa è " + str (round(Ipotenusa,2))+ " Cm")
print("Il perimetro è " + str (round(Perimetro,2))+ " Cm")                                                    
