# this assembler is devoleped for a selfbuild computer
# this assembler was created by Mustapha Chriet
# pass the path of the assembly file (xxx.asm) that you want to convert to machine code as a parameter when you run the app
# you will find the machin code file (xxx.hack) in the same directry with the assembly file

import sys

# the first pass
    
    # symbol table
symbol_table = {"R0":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8, "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14":14, "R15":15, "SCREEN":16384, "KBD":24576, "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4}    

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

# the decoder
decodeing_comp = {"0" : "0101010", "1" : "0111111", "-1" : "0111010", "D" : "0001100", "A" : "0110000", "!D" : "0001101", "!A" : "0110001", "-D" : "0001111", "-A" : "0110011", "D+1" : "0011111", "A+1" : "0110111", "D-1" : "0001110", "A-1" : "0110010", "D+A" : "0000010", "D-A" : "0010011", "A-D" : "0000111", "D&A" : "0000000", "D|A" : "0010101", "M" : "1110000", "!M" : "1110001", "-M" : "1110011", "M+1" : "1110111", "M-1" : "1110010", "D+M" : "1000010", "D-M" : "1010011", "M-D" : "1000111", "D&M" : "1000000", "D|M" : "1010101" }
decodeing_dest = { "M" : "001", "D" : "010", "MD" : "011", "A" : "100", "AM" : "101", "AD" : "110", "AMD" : "111"}
decodeing_jump = { "JGT" : "001", "JEQ" : "010", "JGE" : "011", "JLT" : "100", "JNE" : "101", "JLE" : "110", "JMP": "111"}
assembly_file = open(arguments[1], "r")
machineCodeFile = open(arguments[1].rstrip("asm") + "hack", "a")
for line in assembly_file:
    line = line.strip("\n")
    n = line.find("//")
    if n > 0 and line[0] != "(":
        if line[0] == "@":
            line = line[:n].strip().lstrip("@")
            if line.isnumeric():
                binary_instru = "0" + bin(int(line))[2:].zfill(15) + "\n"
                machineCodeFile.write(binary_instru)
            else:
                binary_instru = "0" + bin(symbol_table[line])[2:].zfill(15) + "\n"
                machineCodeFile.write(binary_instru)
        else: 
                ind_of_eq = line.find("=")
                ind_of_semi = line.find(";")
                if ind_of_eq > 0 and ind_of_semi > 0 :
                    binary_instru = "111" + decodeing_comp[line[ind_of_eq + 1 : ind_of_semi]] + decodeing_dest[line[:ind_of_eq]] + decodeing_jump[line[ind_of_semi + 1 :]] + "\n"
                    machineCodeFile.write(binary_instru)
                elif ind_of_eq == -1 and ind_of_semi > 0 :
                    binary_instru = "111" + decodeing_comp[line[: ind_of_semi]] + "000" + decodeing_jump[line[ind_of_semi + 1 :]] + "\n"
                    machineCodeFile.write(binary_instru)
                elif ind_of_eq > 0 and ind_of_semi == -1 :
                    binary_instru = "111" + decodeing_comp[line[ind_of_eq + 1 :]] + decodeing_dest[line[:ind_of_eq]] + "000" + "\n"
                    machineCodeFile.write(binary_instru)       
    elif n == -1 and line != "" and line[0] !="(":
        if line[0] == "@":
            line = line.strip("@")
            if line.isnumeric():
                binary_instru = "0" + bin(int(line))[2:].zfill(15) + "\n"
                machineCodeFile.write(binary_instru)
            else:
                binary_instru = "0" + bin(symbol_table[line])[2:].zfill(15) + "\n"
                machineCodeFile.write(binary_instru)    
        else:
            ind_of_eq = line.find("=")
            ind_of_semi = line.find(";")
            if ind_of_eq > 0 and ind_of_semi > 0 :
                binary_instru = "111" + decodeing_comp[line[ind_of_eq + 1 : ind_of_semi]] + decodeing_dest[line[:ind_of_eq]] + decodeing_jump[line[ind_of_semi + 1 :]] + "\n"
                machineCodeFile.write(binary_instru)
            elif ind_of_eq == -1 and ind_of_semi > 0 :
                binary_instru = "111" + decodeing_comp[line[: ind_of_semi]] + "000" + decodeing_jump[line[ind_of_semi + 1 :]] + "\n"
                machineCodeFile.write(binary_instru)
            elif ind_of_eq > 0 and ind_of_semi == -1 :
                binary_instru = "111" + decodeing_comp[line[ind_of_eq + 1 :]] + decodeing_dest[line[:ind_of_eq]] + "000" + "\n"
                machineCodeFile.write(binary_instru)   
machineCodeFile.close()
assembly_file.close()  
print ("File converted")  