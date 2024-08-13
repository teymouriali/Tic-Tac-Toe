from random import choice
from os import system
from time import sleep
from colorama import Fore


def sefr():

    global listvaluedictmain
    global counter
    counter = 0

    dictmain = {"a1": 1, "a2": 2, "a3": 3, "a4": 4,
                "a5": 5, "a6": 6, "a7": 7, "a8": 8, "a9": 9}
    listvaluedictmain = list(dictmain.values())
    print(Fore.LIGHTRED_EX+"In this game, you are represented by the letter O and the computer is represented by the letter X"+Fore.LIGHTWHITE_EX)
    main()


def main():

    print(Fore.LIGHTWHITE_EX+f"""
        {listvaluedictmain[0]}|{listvaluedictmain[1]}|{listvaluedictmain[2]}
        {listvaluedictmain[3]}|{listvaluedictmain[4]}|{listvaluedictmain[5]}
        {listvaluedictmain[6]}|{listvaluedictmain[7]}|{listvaluedictmain[8]}           
      """)

    if counter == 1:
        inp = input("Do you want to repeat? ? (y/n)")

        if inp.lower() == "n":
            print(Fore.LIGHTWHITE_EX+"Good Bye")
            exit(0)

        elif inp.lower() == "y":
            system("clear")
            sefr()
            main()

        else:

            print(Fore.LIGHTCYAN_EX+"Just choose y or n"+Fore.LIGHTWHITE_EX)
            main()
    else:
        am()


def am():

    global counter
    inp = input(Fore.LIGHTWHITE_EX +
                "Which number is your choice in the table? (enter q for exit) ")

    if inp.lower() == "q":
        print(Fore.LIGHTWHITE_EX+"Good Bye")
        exit(0)

    if inp.isnumeric():
        inp = int(inp)

        for i in listvaluedictmain:

            if str(i).isnumeric():

                if inp == listvaluedictmain[i-1]:
                    i = int(i)
                    listvaluedictmain[i-1] = Fore.LIGHTGREEN_EX + \
                        "O"+Fore.LIGHTWHITE_EX

                    if (listvaluedictmain[4] == listvaluedictmain[5] and listvaluedictmain[4] == listvaluedictmain[3]) or (listvaluedictmain[4] == listvaluedictmain[0] and listvaluedictmain[4] == listvaluedictmain[8]) or (listvaluedictmain[4] == listvaluedictmain[2] and listvaluedictmain[4] == listvaluedictmain[6] or (listvaluedictmain[4] == listvaluedictmain[1] and listvaluedictmain[4] == listvaluedictmain[7])):
                        system("clear")
                        counter = +1
                        print(Fore.LIGHTGREEN_EX+"you win :) " +
                              Fore.LIGHTBLACK_EX)
                        main()

                    if (listvaluedictmain[0] == listvaluedictmain[1] and listvaluedictmain[0] == listvaluedictmain[2]) or (listvaluedictmain[0] == listvaluedictmain[3] and listvaluedictmain[0] == listvaluedictmain[6]) or (listvaluedictmain[8] == listvaluedictmain[5] and listvaluedictmain[8] == listvaluedictmain[2] or (listvaluedictmain[8] == listvaluedictmain[7] and listvaluedictmain[8] == listvaluedictmain[6])):
                        system("clear")
                        print(Fore.LIGHTGREEN_EX+"you win :) " +
                              Fore.LIGHTBLACK_EX)
                        counter = +1
                        main()

                    system("clear")
                    print("computer choising ... waiting ")
                    for i in listvaluedictmain:
                        if str(i).isnumeric():
                            comp()
                    else:
                        system("clear")
                        print("The result was tied")
                        counter = 1
                        main()
                    comp()

        else:
            system("clear")
            print("Just choose from the remaining numbers in the table")
            main()
    else:
        print("Just choose from the remaining numbers in the table")
        am()


def comp():

    global counter

    computerselect = choice(listvaluedictmain)

    sleep(0.05)

    for i in listvaluedictmain:

        if str(i).isnumeric():

            if computerselect == listvaluedictmain[i-1]:
                i = int(i)
                listvaluedictmain[i-1] = Fore.LIGHTRED_EX + \
                    "X"+Fore.LIGHTWHITE_EX

                if (listvaluedictmain[4] == listvaluedictmain[5] and listvaluedictmain[4] == listvaluedictmain[3]) or (listvaluedictmain[4] == listvaluedictmain[0] and listvaluedictmain[4] == listvaluedictmain[8]) or (listvaluedictmain[4] == listvaluedictmain[2] and listvaluedictmain[4] == listvaluedictmain[6] or (listvaluedictmain[4] == listvaluedictmain[1] and listvaluedictmain[4] == listvaluedictmain[7])):
                    system("clear")
                    counter = +1
                    print(Fore.LIGHTRED_EX+"computer win :( " +
                          Fore.LIGHTWHITE_EX)
                    main()

                if (listvaluedictmain[0] == listvaluedictmain[1] and listvaluedictmain[0] == listvaluedictmain[2]) or (listvaluedictmain[0] == listvaluedictmain[3] and listvaluedictmain[0] == listvaluedictmain[6]) or (listvaluedictmain[8] == listvaluedictmain[5] and listvaluedictmain[8] == listvaluedictmain[2] or (listvaluedictmain[8] == listvaluedictmain[7] and listvaluedictmain[8] == listvaluedictmain[6])):
                    system("clear")
                    print(Fore.LIGHTRED_EX+"computer win :( " +
                          Fore.LIGHTWHITE_EX)
                    counter = +1
                    main()

                system("clear")
                main()

            else:
                computerselect = choice(listvaluedictmain)

    else:
        computerselect = choice(listvaluedictmain)
        comp()


if __name__ == "__main__":
    system("clear")
    sefr()
