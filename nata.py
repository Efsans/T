import random

inv=[]

def inicio():
  print("voce acorda em uma clareira tudo é extranhamente familiar")
  escolha=input("ao longe voce avista A caverna, ")

  if escolha.lower() == "caverna":
    caverna()


def caverna():
  global inv
  if "tocha" not in inv:
    print("ao dexer a colina voce chega a entrada da caverna")
  escolha=input("a caverna esta escura e a pedasos de madeira quebrados por toda a entrada, oque fazer: ")

  if escolha.lower()=="madeira":
    if "tocha" in inv :
      print("não a nada mais a fazer aqui")
      caverna()
      
    else:
      print("ao se aproximar das madeiras voce ve uma tocha e a pega ") 
      inv.append("tocha")
      caverna()
  elif escolha.lower()=="caverna":
    if "tocha" in inv:
      print("voce adentra nas entranhas da caverna")

    
     


def luta_limbo():
  tu=20
  ele=20
  while tu >= 0:
    atk =input("Atk y/n, cure q:  ")
    if atk=="y":
      chan=random.randint(1, 20)

      if chan==20:
        print("acerto certeiro")
        ele-=10
      elif chan >=10:
        print("acerto")
        ele-=5
      elif chan < 10:
        print("ele revida")
        tu-=1   
    elif atk == "n":
      chan=random.randint(1, 20)

      if chan==20:
        print("ele te subjulga")
        tu-=10
      elif chan >=10:
        print("ele te acerta")
        tu-=5
      elif chan < 10:
        print("...")
    elif atk=="q":
      chan=random.randint(1, 30)
      if chan==30:
        tu+=20
        print("a sobriedade te alcança e te amaldiçoa com vida ")
      elif chan>=15:
        tu+=10
        print("uma calma momentania alivia suas feridas. ")
      elif chan < 15:
        tu+=random.randint(1,10)
        tu-=random.randint(1, 10)
        print("uma calma momentania é imterrompida")
    else:
      print("S/N: ")    

    if ele <=0:
      print("um destino se sela, outro aparece")
      ele=20
    if tu<=0:
      print("seu destino se sela, tudo se acalma")
if __name__ == "__main__":
    inicio()