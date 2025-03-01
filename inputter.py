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


def uncomma(list):
    array = []
    while "," in list:
        index = list.index(",")
        array.append(int(list[:index].strip()))
        list = list[index + 1:]
    return array
    


class adv_inputters:
    def __init__(self):
        self.array_read_instructions = "Please input the list of data "
        self.array_read_instructions += "columns that you would like to "
        self.array_read_instructions += "take data from (Separate the data"
        self.array_read_instructions += " with commas as such: \'/,/\')"
        self.checker1 = {}
        self.checker2 = {}
        self.column_names = []
    
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
                          init_input = '', no_inputter = False,
                          excel_skip = False):
        print(str_statement)
        if not no_inputter:
            resulting_text = init_input + inputter()
        else:
            resulting_text = init_input
        print(resulting_text)
        if readtype == "file":
            try:
                data = pnd.read_csv(resulting_text)
                return data
            except:
                if excel_skip == True:
                    class_quick_out("Error: File not read.")
                    self.basic_read(str_statement, "file", init_input)
                try:
                    self.excel_sheet_reader(resulting_text)
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
                self.current_column = self.data[self.checker2[resulting_text]]
            except:
                class_quick_out("Error: Column not found.")
                self.basic_read(str_statement, "column", init_input)
        
    
    
    def checker_func(self, incrementer, column_name, checked_value):
        new_column_name = column_name
        try:
            z = 0
            for point in self.checker1:
                if new_column_name in self.checker1[point]:
                    print(new_column_name)
                    new_column_name += str(z)
                    z += 1
        except:
            pass
        try:
            self.checker1[incrementer].append(new_column_name)
        except:
            self.checker1.update({incrementer : [new_column_name]})
        self.checker2.update({new_column_name : checked_value})
        
        return new_column_name
    
    def excel_sheet_reader(self, file, incrementer = 0, checked_value = 0):
        try:
            data_sheet = pnd.read_excel(file, sheet_name = incrementer)
        except:
            return
        try:
            for column_name in data_sheet:
                self.data.append(data_sheet[column_name])
                new_column_name = self.checker_func(incrementer, column_name,
                                                    checked_value)
                self.data[len(self.data) - 1].name = new_column_name
                checked_value += 1
        except:
            try:
                print(incrementer)
                self.data = []
                for column_name in data_sheet:
                    self.data.append(data_sheet[column_name])
                    new_column_name = self.checker_func(incrementer, 
                                                        column_name, 
                                                        checked_value)
                    self.data[len(self.data) - 1].name = new_column_name
                    checked_value += 1
            except:
                pass
        incrementer += 1
        self.excel_sheet_reader(file, incrementer, checked_value)
        
    



        

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


