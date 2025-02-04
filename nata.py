import random

tu=20
ele=20

while tu >= 0:
  atk =input("Atk y/n: ")
  if atk=="y":
    chan=random.randint(1, 20)

    if chan==20:
      print("crito")
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
      print("ele crita")
      tu-=10
    elif chan >=10:
      print("ele acerta")
      tu-=5
    elif chan < 10:
      print("...")  
  else:
    print("S/N: ")    

  if ele <=0:
    print("um destino se sela, outro aparece")
    ele=20
  if tu<=0:
    print("seu destino se sela, tudo se acalma")
