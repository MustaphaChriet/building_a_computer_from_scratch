


def write_arithlogical(arithlogical_instruction, output_file_path, eq, gt, lt):
    assembly_instructions = {"add" : "//    add\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n",
                            "sub" : "//    sub\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n",
                            "neg" : "//    neg\n@SP\nA=M\nA=A-1\nM=-M\n",
                            "eq" : f"//    eq\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@eq.true{eq}\nD;JEQ\nD=0\n@eq.false{eq}\n0;JMP\n(eq.true{eq})\nD=-1\n(eq.false{eq})\n@SP\nA=M-1\nM=D\n",
                            "gt" : f"//    gt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@gt.true{gt}\nD;JGT\nD=0\n@gt.false{gt}\n0;JMP\n(gt.true{gt})\nD=-1\n(gt.false{gt})\n@SP\nA=M-1\nM=D\n",
                            "lt" : f"//    lt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@lt.true{lt}\nD;JLT\nD=0\n@lt.false{lt}\n0;JMP\n(lt.true{lt})\nD=-1\n(lt.false{lt})\n@SP\nA=M-1\nM=D\n",
                            "and" : "//    and\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M\n",
                            "or" : "//    or\n@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M\n",
                            "not" : "//    not\n@SP\nA=M\nA=A-1\nM=!M\n"}
    asm_file = open(output_file_path, "a")
    asm_file.write(assembly_instructions[arithlogical_instruction])
    asm_file.close()

def write_push_pop(push_or_pop, arg1, arg2, output_file_path): 
    i = arg2  
    this_or_that = thisThat(i)
    file_name = output_file_path.split("\\")[-1].rstrip(".asm")
    segments_push_assembly_instructions = {"local" : f"// push local {i}\n@{i}\nD=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "argument" : f"// push argument {i}\n@{i}\nD=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "this" : f"// push this {i}\n@{i}\nD=A\n@THIS\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "that" : f"// push that {i}\n@{i}\nD=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "constant" : f"// push constant {i}\n@{i}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "temp" : f"// push temp {i}\n@{i}\nD=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "pointer" : f"// push pointer {i}\n@{this_or_that}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n",
                                        "static" : f"// push static {i}\n@{file_name}.{i}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"} 
    
    segments_pop_assembly_instructions = {"local" : f"// pop local {i}\n@LCL\nD=M\n@{i}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
                                       "argument" : f"// pop argument {i}\n@ARG\nD=M\n@{i}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
                                       "this" : f"// pop this {i}\n@THIS\nD=M\n@{i}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
                                       "that" : f"// pop that {i}\n@THAT\nD=M\n@{i}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
                                       "temp" : f"// pop temp {i}\n@{i}\nD=A\n@5\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n",
                                       "pointer" : f"// pop pointer {i}\n@SP\nAM=M-1\nD=M\n@{this_or_that}\nM=D\n",
                                       "static" : f"// pop static {i}\n@SP\nAM=M-1\nD=M\n@{file_name}.{i}\nM=D\n"}
    asm_file = open(output_file_path, "a")
    if push_or_pop == "push":
        asm_file.write(segments_push_assembly_instructions[arg1])
        asm_file.close()
    elif push_or_pop == "pop":
        asm_file.write(segments_pop_assembly_instructions[arg1])
        asm_file.close()    

def thisThat(a):
    if a == 0 :
        returned = "THIS"
        return returned
    elif a == 1 :
        returned = "THAT"
        return returned
