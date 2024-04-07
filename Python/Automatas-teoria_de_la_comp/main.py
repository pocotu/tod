from DFA import DFA
from NFA import NFA
from ExpReg import ExpReg
from PDA import PDA
from CFG import CFG
from Turing import Turing

def main():
    while True:
        print("Seleccione una opción:")
        print("A. DFA")
        print("B. NFA")
        print("C. Exp Reg")
        print("D. PDA")
        print("E. CFG")
        print("F. Máquina de Turing")
        print("G. Salir")

        option = input().upper()

        if option == "A":
            dfa = DFA()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = dfa.evaluate(input_str)
            print("Resultado:", result)
        elif option == "B":
            nfa = NFA()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = nfa.evaluate(input_str)
            print("Resultado:", result)
        elif option == "C":
            expreg = ExpReg()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = expreg.evaluate(input_str)
            print("Resultado:", result)
        elif option == "D":
            pda = PDA()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = pda.evaluate(input_str)
            print("Resultado:", result)
        elif option == "E":
            cfg = CFG()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = cfg.evaluate(input_str)
            print("Resultado:", result)
        elif option == "F":
            turing = Turing()
            input_str = input("Ingrese la cadena a evaluar: ")
            result = turing.evaluate(input_str)
            print("Resultado:", result)
        elif option == "G":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
