import random



def reloj(response):
      
      while response ==  "Y": 
            no = random.randint(1,6)
            reloj2(no)

      
def reloj2(no):
           
      if no == 1:
                    print("[-----]")
                    print("[     ]")
                    print("[  0  ]")
                    print("[     ]")
                    print("[-----]")

      if no == 2:
                   print("[-----]")
                   print("[ 0   ]")
                   print("[     ]")
                   print("[    0]")
                   print("[-----]")

      if no == 3:
                   print("[-----]")
                   print("[  0  ]")
                   print("[  0  ]")
                   print("[  0  ]")
                   print("[-----]")
            
      if no == 4:
                   print("[-----]")
                   print("[ 0 0 ]")
                   print("[     ]")
                   print("[ 0 0 ]")
                   print("[-----]")
            
      if no == 5:
                   print("[-----]")
                   print("[ 0 0 ]")
                   print("[  0  ]")
                   print("[ 0 0 ]")
                   print("[-----]")

      if no == 6:
                   print("[-----]")
                   print("[ 0 0 ]")
                   print("[ 0 0 ]")
                   print("[ 0 0 ]")
                   print("[-----]")
      reloj1()
def reloj1():
     response = input ("Ingresa Y en mayúscula para tirar: ") 
     reloj(response)





   
        
reloj1()
        