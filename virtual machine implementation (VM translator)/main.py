import sys , parserr ,codeWriter , os

arguments = sys.argv
output_file = ""
if os.path.isfile(arguments[1]):
    output_file = arguments[1].rsplit(".vm") + ".asm"
else :
     output_file = arguments[1] + "\\" + arguments[1].split("\\")[-1] + ".asm"   

instructions = parserr.only_instructions(arguments[1])
eq = 0
gt = 0
lt = 0
call_num = 0
fun_num = 0
codeWriter.write_init(output_file)
for instruction in instructions:
    parts = instruction.split()
    print (parts)
    instruction_type = parserr.instruction_type(parts)
    if instruction_type == "C_Arithlogical":
        eq += parserr.if_eq_inc(parts[0])
        gt += parserr.if_gt_inc(parts[0])
        lt += parserr.if_lt_inc(parts[0])
        codeWriter.write_arithlogical(parts[0], output_file, eq, gt, lt)
    elif instruction_type == "C_Push":
        codeWriter.write_push_pop(parts[0], parserr.arg1(parts), parserr.arg2(parts), parts[3], output_file)    
    elif instruction_type == "C_Pop":
        codeWriter.write_push_pop(parts[0], parserr.arg1(parts), parserr.arg2(parts), parts[3], output_file)
    elif instruction_type == "C_Label":
        codeWriter.writ_label(parts[1], output_file)
    elif instruction_type =="C_Goto":
        codeWriter.write_goto(parts[1], output_file)    
    elif instruction_type == "C_If":
        codeWriter.write_if_goto(parts[1], output_file)
    elif instruction_type == "C_Function":
        codeWriter.write_function(parts[1], parts[2], output_file)
        fun_num += 1
    elif instruction_type == "C_Call":
        codeWriter.write_call(parts[1], parts[2], call_num, output_file)
        call_num += 1
    elif instruction_type == "C_Return":
        codeWriter.write_return(output_file)            
        