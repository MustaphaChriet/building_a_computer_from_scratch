import os 



def only_instructions (VM_prog_path):
    pure_instructions = []
    if os.path.isfile(VM_prog_path):
        VM_file = open(VM_prog_path, "r")
        file_name = VM_prog_path.split("\\")[-1].rstrip(".vm")
        for line in VM_file:
            line = line.rstrip("\n")
            n = line.find("//")
            if n == -1 and line != "":
                pure_instructions.append(line + " " + file_name)
            elif n > 0 :
                line = line[:n].strip()
                pure_instructions.append(line + " " + file_name)
    elif os.path.isdir(VM_prog_path):
        file_num = os.listdir(VM_prog_path)
        for line in file_num:
            file_name = line.rstrip(".vm")
            if line[-3:] == ".vm":
                VM_file = open(VM_prog_path + "\\" + line, "r")
                for line in VM_file:
                    line = line.rstrip("\n")
                    n = line.find("//")
                    if n == -1 and line != "":
                        pure_instructions.append(line + " " + file_name)
                    elif n > 0 :
                        line = line[:n].strip()
                        pure_instructions.append(line + " " + file_name)
    return pure_instructions

def instruction_type (instruction):
    if len(instruction) == 2 and len(instruction[0]) <= 3:
        return "C_Arithlogical"
    elif  instruction[0] == "push":
        return "C_Push"
    elif  instruction[0] == "pop":
        return "C_Pop"   
    elif instruction[0] == "label":
        return "C_Label"
    elif instruction[0] == "goto":
        return "C_Goto"
    elif instruction[0] == "if-goto":
        return "C_If"
    elif instruction[0] == "function":
        return "C_Function"
    elif instruction[0] == "call":
        return "C_Call"
    elif instruction[0] == "return":
        return "C_Return"

def arg1(instruction_parts):
    if len(instruction_parts) == 4 and (instruction_parts[0] == "push" or instruction_parts[0] == "pop") :
        return instruction_parts[1]
    elif len(instruction_parts) == 2 and len(instruction_parts[0]) <= 3:
        return instruction_parts[0]

def arg2(instruction_parts):
    if len(instruction_parts) == 4 and (instruction_parts[0] == "push" or instruction_parts[0] == "pop"):
        return int(instruction_parts[2])           
          
def if_eq_inc(instruction):
    if instruction[0] == "eq":
        return 1
    else:
        return 0
    
def if_gt_inc(instruction):
    if instruction[0] == "gt":
        return 1
    else:
        return 0

def if_lt_inc(instruction):
    if instruction[0] == "lt":
        return 1
    else:
        return 0        
    