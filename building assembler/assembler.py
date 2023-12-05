import sys

# the first pass
    
    # symbol table
symbol_table = {"R0":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14":14, "R15":15, "SCREEN":16384, "KBD":24576, "SP":0, "LCL":1, "ARC":2, "THIS":3, "THAT":4}    

arguments = sys.argv
assembly_file = open(arguments[1], "r")
    #  ignoring all comments and whide spaces and adding branching symbols the symbol table
instruction_num = 0    
for line in assembly_file:
    line = line.rstrip("\n")
    n = line.find("//")
    if n > 0:
        line = line[:n].strip()
        if line[0] == "(":
            symbol_table[line.rstrip(")").lstrip("(")] = instruction_num
        else:
            instruction_num += 1
    elif n == -1 and line != "":
        if line[0] == "(":
            symbol_table[line.rstrip(")").lstrip("(")] = instruction_num
        else:    
            instruction_num += 1
# the second pass
    # adding variable symbols to the symbol table
variable_address = 16 
assembly_file = open(arguments[1], "r") 
for line in assembly_file:
    line = line.strip("\n")
    n = line.find("//")
    if n > 0 and line[0] == "@":
        line = line[:n].strip().lstrip("@") 
        if not line.isnumeric() and line not in symbol_table:
            symbol_table[line] = variable_address 
            variable_address += 1
    elif n == -1 and line != "":
        if line[0] == "@":
            line = line.lstrip("@")
            if not line.isnumeric() and line not in symbol_table:
                symbol_table[line] = variable_address
                variable_address += 1

