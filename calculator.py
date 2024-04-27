def calculator():
        a = int(input("ENTER FIRST NUMBER: "))
        b = int(input("ENTER SECOND NUMBER: "))
        task = input("ENTER TASK: ")
        if task == "+":
          print(f"{a}+{b}={a+b}")
        elif task == "-":
          print(f"{a}-{b}={a-b}")
        elif task == "/":
          print(f"{a}/{b}={a/b}")
        elif task == "X":
          print(f"{a}X{b}={a*b}")
        else:
         print("INVALID TASK!!!!")
calculator()