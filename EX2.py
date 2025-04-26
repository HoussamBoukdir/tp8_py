# Ce programme permet de vérifier si un nombre donné est un nombre parfait.
# Un nombre parfait est un nombre égal à la somme de ses diviseurs propres 
def est_parfait(n: int) -> bool:
    
    somme_diviseurs: int = 0  

    
    for i in range(1, n):  
        
        if n % i == 0:
           
            somme_diviseurs += i

   
    if somme_diviseurs == n:
        return True  
    else:
        return False  

nombre = 28  
if est_parfait(nombre):
    print(f"{nombre} est un nombre parfait")
else:
    print(f"{nombre} n'est pas un nombre parfait")
