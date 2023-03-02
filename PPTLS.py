from colorama import Fore, init
import random, time

init(autoreset = True)

def juego(J1, J2):
      choices = {'Piedra': ["Tijera", "Lagarto"], "Papel": ["Piedra", "Spock"], "Tijera": ["Papel", "Lagarto"],
      "Lagarto": ["Papel", "Spock"], "Spock": ["Piedra", "Tijera"]}

      if J1 not in choices:
            return "Ocurrio un error. Intentelo de nuevo"
      elif J2 in choices[J1]:
            return "Ganaste la ronda"
      elif J1 == J2:
            return "Es un Empate!"
      else:
            return "La Pc gano la ronda!!"

reglas = Fore.CYAN + """Las reglas de este juego son las siguientes:

Piedra: Rompe Tijera - Aplasta Lagarto
Tijera: Corta Papel - decapita Lagarto
Papel: Cubre Piedra - Desaprueba Spock
Lagarto: Envenena Spock - Come Papel
Spock: Destruye Tijera - Vaporiza Piedra

"""

x = ["Piedra", "Papel", "Tijera" ,"Lagarto", "Spock"]
countPC = 0
countJ1 = 0
count = 0

while True:
      #Entrada de datos, y poner el juego en marcha
      print("\n")
      print("Piedra, Papel, Tijeras, Lagarto, Spock".center(130, "-"))
      if count == 0:
            print(reglas)
      count += 1

      y = random.choice(x)
      pp = input("Ingrese su Eleccion (S: Salir): ").capitalize()
      print("\n")
      if pp == "S":
            print(Fore.YELLOW + "Gracias por jugar! \n")
            print("-".center(130, "-"))
            break

      yo = juego(pp,y)

      if yo == "La Pc gano la ronda!!":
            countPC += 1
      elif yo == "Ganaste la ronda":
            countJ1 += 1
      elif yo == "Ocurrio un error. Intentelo de nuevo":
            print(Fore.RED + yo)
            continue
      elif yo == "Es un Empate!":
            print(Fore.CYAN + pp, "vs", Fore.RED + y, "\n")
            print(Fore.BLUE + yo)
            print(countJ1, "-", countPC)
            continue
            
      #Cantidad de rondas que se van a hacer, y si el usuario va a seguir jugando     
      if countPC == 3 or countJ1 == 3:
            print(Fore.CYAN + pp, "vs", Fore.RED + y, "\n")
            print(countJ1, "-", countPC)

            if countPC == 3:
                  print(Fore.RED + "Perdiste el Juego!")
            elif countJ1 == 3:
                  print(Fore.GREEN + "Ganaste el Juego!")

            repetir = input("Quisieras volver a intentarlo? (si/no): ")
            if repetir == "si":
                  countPC = 0
                  countJ1 = 0
                  print("\n")
                  print(Fore.YELLOW + "Lessgo")
                  continue
            else:
                  print(Fore.YELLOW + "\nGracias por jugar!!!\n")
                  print("-".center(130, "-"))
                  break

      print("...")
      time.sleep(0.5)
      print(Fore.CYAN + pp, "vs", Fore.RED + y, "\n")
      print(Fore.RESET + yo, "\n", countJ1, "-", countPC)
      
     