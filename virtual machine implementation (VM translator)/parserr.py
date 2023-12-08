



def only_instructions (VM_file_path):
    VM_file = open(VM_file_path, "r")
    pure_instructions = []
    for line in VM_file:
        line = line.rstrip("\n")
        n = line.find("//")
        if n == -1 and line != "":
            pure_instructions.append(line)
        elif n > 0 :
            line = line[:n].strip()
            pure_instructions.append(line)
    return pure_instructions

def instruction_type (instruction_parts):
    if len(instruction_parts) == 1:
        return "C_Arithlogical"
    elif len(instruction_parts) == 3 and instruction_parts[0] == "push":
        return "C_Push"
    elif len(instruction_parts) == 3 and instruction_parts[0] == "pop":
        return "C_Pop"   

def arg1(instruction_parts):
    if len(instruction_parts) == 3:
        return instruction_parts[1]
    elif len(instruction_parts) == 1:
        return instruction_parts[0]

def arg2(instruction_parts):
    if len(instruction_parts) == 3:
        return int(instruction_parts[2])           
          
def if_eq_inc(instruction):
    if instruction == "eq":
        return 1
    else:
        return 0
    
def if_gt_inc(instruction):
    if instruction == "gt":
        return 1
    else:
        return 0

def if_lt_inc(instruction):
    if instruction == "lt":
        return 1
    else:
        return 0        