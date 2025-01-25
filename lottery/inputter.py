# Inputter
# Justin Pizano


import sys
import pandas as pnd
import os

def inputter(opt = 'out'):
    ipt = input()
    if ipt == '':
        if opt == 'out':
            print('Are you trying to opt-out of the program?')
            print('Type "Yes" if so.')
            yn_check = 0
            yn = input()
            while yn_check == 0:
                if yn == 'Yes':
                    print('Are you sure?')
                    print('Yes/No')
                    opt_check = 0
                    while opt_check == 0:
                        opt = input()
                        if opt == 'Yes':
                            print('Opting out')
                            sys.exit()
                        elif opt == 'No':
                            print('Continuing with the program using an empty space')
                            opt_check += 1
                            yn_check += 1
                else:
                    print('Continuing with the program using an empty space')
                    yn_check += 1
        
        if opt == 'backtrack':
            print('Are you trying to backtrack?')
            print('Type "Yes" if so.')
            yn_check = 0
            yn = input()
            while yn_check == 0:
                if yn == 'Yes':
                    print('Are you sure?')
                    print('Yes/No')
                    opt_check = 0
                    while opt_check == 0:
                        opt = input()
                        if opt == 'Yes':
                            print('Backtracking')
                            return 'empty_backtrack'
                        elif opt == 'No':
                            print('Continuing with the program using an empty space')
                            opt_check += 1
                            yn_check += 1
                else:
                    print('Continuing with the program using an empty space')
                    yn_check += 1
    return(ipt)

class adv_inputters:
    def __init__(self):
        self.array_read_instructions = "Please input the list of data "
        + "columns that you would like to take data from (Separate the data"
        + " with commas as such: \'/,/\')"
    
    def basic_ask(self, question, choices = ['Yes', 'No'], 
            results = [0, 1], lister = 'options', 
            error = "You had not selected one of the choices " +
            "listed."):
        print(question)
        for choice in choices:
            print(choice + "\t||")
        answer = inputter()
        try:
            result = results[choices.index(answer)]
            return result
        except:
            class_quick_out()
            self.basic_ask(question, choices, results, lister, error)
    
    def basic_read(self, str_statement = "Please enter the " + 
                          "directory of the data file you " +
                          "would like to use", readtype = "file",
                          init_input = '', no_inputter = False):
        print(str_statement)
        if inputter:
            resulting_text = init_input + inputter()
        else:
            resulting_text = init_input
        print(resulting_text)
        if readtype == "file":
            try:
                data = pnd.read_csv(resulting_text)
                return data
            except:
                try:
                    data = pnd.read_excel(resulting_text)
                    self.data = data
                except:
                    class_quick_out("Error: File not read.")
                    self.basic_read(str_statement, "file", init_input)
        if readtype == "dir":
            try:
                os.chdir(resulting_text)
                self.directory = resulting_text
            except:
                class_quick_out("Error: Directory not read.")
                self.basic_read(str_statement, "dir", init_input)
        if readtype == "column":
            try:
                column = self.data[resulting_text]
                try:
                    self.columns.append(column)
                except:
                    self.columns = [column]
                self.current_column = column
            except:
                class_quick_out("Error: Column not found.")
                self.basic_read(str_statement, "column", init_input)
    
        
        


"""
Function to take a class object and either
run the function or exit the program.
"""
def class_quick_out(error = "Error found."):
    print(error)
    print("Type \"Exit\" if you would like to exit the" + 
          " program. To continue with the program, " +
          "enter any other input." +
          "(You may simply press \"Enter\".")
    opt = input()
    if opt == "Exit":
        sys.exit()


