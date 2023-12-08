import sys , parserr ,codeWriter

arguments = sys.argv

instructions = parserr.only_instructions(arguments[1])
eq = 0
gt = 0
lt = 0
for instruction in instructions:
    parts = instruction.split()
    instruction_type = parserr.instruction_type(parts)
    if instruction_type == "C_Arithlogical":
        eq += parserr.if_eq_inc(instruction)
        gt += parserr.if_gt_inc(instruction)
        lt += parserr.if_lt_inc(instruction)
        codeWriter.write_arithlogical(instruction, arguments[1].rstrip("vm") + "asm", eq, gt, lt)
    elif instruction_type == "C_Push":
        codeWriter.write_push_pop(parts[0], parserr.arg1(parts), parserr.arg2(parts),arguments[1].rstrip("vm") + "asm")    
    elif instruction_type == "C_Pop":
        codeWriter.write_push_pop(parts[0], parserr.arg1(parts), parserr.arg2(parts),arguments[1].rstrip("vm") + "asm")