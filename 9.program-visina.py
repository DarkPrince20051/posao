najnizi=0
najvisi=0

n=int(input("Koliko ucenika želite unijeti: "))
for i in range(0,n):
     u=int(input("Unesite visinu ucenika: "))

     if i==0:
         najnizi=najvisi=u
     if najnizi>u:
         najnizi=u
     if najvisi<u:
         najvisi=u
print("Najnizi",najnizi,"cm")
print("Najvisi",najvisi,"cm")
