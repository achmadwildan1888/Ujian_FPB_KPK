
def kpk(x, y):
   if x > y:
       faktor = x
   else:
       faktor = y

   while True:
       if((faktor % x == 0) and (faktor % y == 0)):
           kpk = faktor
           break
       faktor+= 1
   return faktor

a = int(input("Ketik angka pertama: "))
b = int(input("Ketik angka kedua: "))

print("kpk dari", a,"and", b,"is", kpk(a, b))

def FPB(x, y): 
  
    if x > y: 
        nilai = y 
    else: 
        nilai = x 
    for i in range(1,nilai+1): 
        if((x % i == 0) and (y % i == 0)): 
            FPB = i 
              
    return FPB 
  
d = int(input("Ketik angka pertama: "))
e = int(input("Ketik angka kedua: "))
  

print("FPB dari", d,"and", e,"is", FPB(d, e))