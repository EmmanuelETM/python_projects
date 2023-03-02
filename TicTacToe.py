from colorama import Fore, init
import os, time

init(autoreset = True)

#Limpieza y ejemplo de posiciones
def cleanpositions():
      os.system('cls')
      print("\n")
      print(Fore.MAGENTA + "Tic Tac Toe".center(130, "-"))
      print("Posiciones\n")
      print(" 1:1 | 1:2 | 1:3 ")
      print('-----------------')
      print(" 2:1 | 2:2 | 2:3 ")
      print('-----------------')
      print(" 3:1 | 3:2 | 3:3 ")
      print("\n")
      print(Fore.CYAN + "J1 = 'X'"," y", Fore.MAGENTA + "J2 = 'O'")
      time.sleep(2)
      os.system('cls')

#Tabla gvi
def board():
      os.system('cls')
      print(Fore.MAGENTA + "Tic Tac Toe".center(130, "-"))
      print(f"{countJ1} - {countJ2}".center(12))
      print(f"\n {tabla['1:1']} | {tabla['1:2']} | {tabla['1:3']} ")
      print('-----------')
      print(f" {tabla['2:1']} | {tabla['2:2']} | {tabla['2:3']} ")
      print('-----------')
      print(f" {tabla['3:1']} | {tabla['3:2']} | {tabla['3:3']} ")
      print("\n")

#Yeahboi
def limpio():
      os.system('cls')
      board()

#Reiniciar la tabla
def reintentar():
      reintentar = input("Quisiera volver a jugar? (SI/NO) ").capitalize()
      if reintentar == "Si":
            for k in tabla:
                  if tabla[k] != " ":
                        tabla[k] = " "
                  else:
                        continue
            return "Si"
      else: return 'No'

#Determinar quien gana
def epic():
      if (tabla["1:1"] == tabla["2:2"] == tabla["3:3"] == "X") or (tabla["1:3"] == tabla["2:2"] == tabla["3:1"] == "X"): 
            return "Gana J1!"

      elif (tabla["1:1"] == tabla["1:2"] == tabla["1:3"] == "X") or (tabla["2:1"] == tabla["2:2"] == tabla["2:3"] == "X") or (tabla["3:1"] == tabla["3:2"] == tabla["3:3"] == "X"):
            return "Gana J1!"

      elif (tabla["1:1"] == tabla["2:1"] == tabla["3:1"] == "X") or (tabla["1:2"] == tabla["2:2"] == tabla["3:2"] == "X") or (tabla["1:3"] == tabla["2:3"] == tabla["3:3"] == "X"):
            return "Gana J1!"

      #Para J2 "O"
      elif (tabla["1:1"] == tabla["2:2"] == tabla["3:3"] == "O") or (tabla["1:3"] == tabla["2:2"] == tabla["3:1"] == "O"): 
            return "Gana J2!"

      elif (tabla["1:1"] == tabla["1:2"] == tabla["1:3"] == "O") or (tabla["2:1"] == tabla["2:2"] == tabla["2:3"] == "O") or (tabla["3:1"] == tabla["3:2"] == tabla["3:3"] == "O"):
            return "Gana J2!"

      elif (tabla["1:1"] == tabla["2:1"] == tabla["3:1"] == "O") or (tabla["1:2"] == tabla["2:2"] == tabla["3:2"] == "O") or (tabla["1:3"] == tabla["2:3"] == tabla["3:3"] == "O"):
            return "Gana J2!"


tabla = {"1:1": " ", "1:2": " ", "1:3": " ",
         "2:1": " ", "2:2": " ", "2:3": " ",
         "3:1": " ", "3:2": " ", "3:3": " "}


count = 0
countA = 0
countB = 0
countJ1 = 0
countJ2 = 0


while True: 
      if count == 0:
            cleanpositions()
      board()
      print("\n")

      while True:
            if countA == 0:
                  J1 = input(Fore.CYAN + "Turno de J1 ---> ")
                  if J1 not in tabla:
                        print(Fore.RED + "Error: Posicion fuera de los limites")
                        time.sleep(1)
                        limpio()
                        continue
                  elif tabla[J1] == " ":
                        tabla[J1] = "X"
                        count += 1
                        board()
                  else:
                        print(Fore.RED +  "Error: Esa posicion ya esta ocupada. ")
                        time.sleep(1)
                        limpio()
                        continue
                  countA += 1
            else:
                  countA = 0
                  break

      yo = epic()
      if yo == "Gana J1!":
            countJ1 += 1
            board()
            print(Fore.CYAN + "Gana J1!")
            w = reintentar()
            if w == "Si":
                  count = 0
                  countA  = 0
                  countB = 0
                  countJ1 += 1
                  continue
            else:
                  time.sleep(0.5)
                  limpio()
                  print(Fore.YELLOW + "Gracias por jugar!")
                  break

      

      while True:
            if countB == 0:
                  J2 = input(Fore.MAGENTA + "\nTurno de J2 ---> ")
                  if J2 not in tabla:
                        print(Fore.RED + "Error: Posicion fuera de los limites")
                        time.sleep(1)
                        board()
                        continue
                  elif tabla[J2] == " ":
                        tabla[J2] = "O"
                        count += 1
                        board()
                        time.sleep(1)
                  else:
                        print(Fore.RED + "Error: Esa posicion ya esta ocupada. ")
                        continue
                  countB += 1
            else:
                  countB = 0
                  break

      yo = epic()
      if yo == "Gana J2!":
            countJ2 += 1
            board()
            print(Fore.MAGENTA + "Gana J2!")
            w = reintentar()
            if w == "Si":
                  count = 0
                  countA  = 0
                  countB = 0
                  continue
            else:
                  limpio()
                  print(Fore.YELLOW + "Gracias por jugar!")
                  break
      
      #El juego esta trancado
      if count >= 8:
            os.system('cls')
            board()
            print(Fore.GREEN + "\nEl juego esta trancado")

            yo = reintentar()
            count = 0
            countA  = 0
            countB = 0
            if yo == "No":
                  print(Fore.YELLOW + "Gracias por Jugar!!")
                  break
            
      epic = input(Fore.CYAN + "Enter to continue (s = Salir)").capitalize()
      if epic == "S":
            print(Fore.YELLOW + "Gracias por jugar!!")
            break
      else:
            continue