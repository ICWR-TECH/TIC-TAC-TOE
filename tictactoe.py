print("""
##########################
# TIC TAC TOE - PYTHON   #
# Afrizal F.A - R&D ICWR #
##########################
""")

import random

class tictactoe:

    def print_board(self):

        board = "{}|{}|{}\n".format(self.board_values['q'], self.board_values['w'], self.board_values['e'])
        board += "_ _ _\n"
        board += "{}|{}|{}\n".format(self.board_values['a'], self.board_values['s'], self.board_values['d'])
        board += "_ _ _\n"
        board += "{}|{}|{}\n".format(self.board_values['z'], self.board_values['x'], self.board_values['c'])
        return board

    def pick_bot(self):

        pick = random.randint(0, len(self.number_board) - 1)

        if self.board_values[self.number_board[pick]] == ' ':

            self.board_values[self.number_board[pick]] = 'x'

        else:

            self.automation_bot()

    def automation_bot(self):

        if self.board_values['s'] == ' ':

            self.board_values['s'] = 'x'

        elif self.board_values[self.value] == 'x' or self.board_values[self.value] == 'o':

            self.pick_bot()

        else:

            self.pick_bot()

    def validation(self):

        try:

            self.automation_bot()
            print(self.print_board())

        except:

            print(self.print_board())
            print("[*] End Game!")
            exit()

        if self.board_values['q'] == "o" and self.board_values['w'] == "o" and self.board_values['e'] == 'o':

            print("[+] You Win!")
            exit()

        elif self.board_values['a'] == "o" and self.board_values['s'] == "o" and self.board_values['d'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['z'] == "o" and self.board_values['x'] == "o" and self.board_values['c'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['q'] == "o" and self.board_values['a'] == "o" and self.board_values['z'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['w'] == "o" and self.board_values['s'] == "o" and self.board_values['x'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['e'] == "o" and self.board_values['d'] == "o" and self.board_values['c'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['q'] == "o" and self.board_values['s'] == "o" and self.board_values['c'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['z'] == "o" and self.board_values['s'] == "o" and self.board_values['e'] == "o":

            print("[+] You Win!")
            exit()

        elif self.board_values['q'] == "x" and self.board_values['w'] == "x" and self.board_values['e'] == 'x':

            print("[-] You Lose!")
            exit()

        elif self.board_values['a'] == "x" and self.board_values['s'] == "x" and self.board_values['d'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['z'] == "x" and self.board_values['x'] == "x" and self.board_values['c'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['q'] == "x" and self.board_values['a'] == "x" and self.board_values['z'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['w'] == "x" and self.board_values['s'] == "x" and self.board_values['x'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['e'] == "x" and self.board_values['d'] == "x" and self.board_values['c'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['q'] == "x" and self.board_values['s'] == "x" and self.board_values['c'] == "x":

            print("[-] You Lose!")
            exit()

        elif self.board_values['z'] == "x" and self.board_values['s'] == "x" and self.board_values['e'] == "x":

            print("[-] You Lose!")
            exit()

    def __init__(self):

        self.board_values = {
            "q": ' ', "w": ' ', "e": ' ',
            "a": ' ', "s": ' ', "d": ' ',
            "z": ' ', "x": ' ', "c": ' '
        }

        self.number_board = [
            "q", "w", "e",
            "a", "s", "d",
            "z", "x", "c"
        ]

        while(True):

            self.value = input("[*] Value -> ")
            self.value = self.value.lower()

            print("\n")

            if self.value != '' and self.value in "q w e a s d z x c":

                if self.board_values[self.value] == ' ':

                    self.board_values[self.value] = "o"
                    self.validation()

                else:

                    print("[-] Try Again!")

            else:

                print("[-] Input not valid!")

if __name__ == "__main__":

    tictactoe()
