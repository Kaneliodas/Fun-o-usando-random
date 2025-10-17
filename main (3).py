import random
def media(n1,n2,n3):
    return (n1+n2+n3)/3 
a = media(random.randint(1,10),random.randint(1,10),random.randint(1,10))
if a >= 7 and a < 10:
   print(f" Aprovado, sua nota foi: {a}")
elif a < 7:
    print(f"Reprovado, sua nota foi: {a}")
else:
    print(f"Aprovado com distinção")
    
    
