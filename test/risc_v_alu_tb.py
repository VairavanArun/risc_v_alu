import cocotb
import pytest
from cocotb.triggers import Timer

def get_predefined_code(input_string):
    predefined_codes = {
        # "code" : "op sx nx ix sy ny iy",
        "addi" : {"op": 0, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "slti" : {"op": 5, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 1, "iy": 1},
        "sltui": {"op": 7, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 1, "iy": 1},
        "andi" : {"op": 11, "sx":0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "ori"  : {"op": 12, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "xori" : {"op": 13, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "slli" : {"op": 2, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "srli" : {"op": 3, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "srai" : {"op": 4, "sx": 0, "nx": 0, "ix": 0, "sy": 1, "ny": 0, "iy": 0},
        "add"  : {"op": 0, "sx": 0, "nx": 0, "ix": 0, "sy":0, "ny": 0, "iy": 0},
        "slt"  : {"op": 5, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "sltu" : {"op": 7, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "and"  : {"op": 11, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "or"   : {"op": 12, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "xor"  : {"op": 13, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "sll"  : {"op": 2, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "srl"  : {"op": 3, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "sra"  : {"op": 4, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 0, "iy": 0},
        "sub"  : {"op": 1, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "beq"  : {"op": 9, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "bne"  : {"op": 10, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "blt"  : {"op": 5, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "bltu" : {"op": 7, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "bge"  : {"op": 6, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
        "bgeu" : {"op": 8, "sx": 0, "nx": 0, "ix": 0, "sy": 0, "ny": 1, "iy": 1},
    }

    return predefined_codes[input_string]

def decode_instructions(instr_file):
    '''
    This function reads the file that contains the program and decodes the instruction
    to opcode, destination register, source register 1 and 2
    '''
    decoded_instructions = []

    #open the file containing the instructions
    with open(instr_file, "r") as program:
        #read all the lines in the instruction file
        instructions = program.readlines()

        for instr in instructions:
            #each line in the instruction file should be of the following format
            #<instruction> rd,rs1,rs2
            instr_split = instr.split()

            opcode = instr_split[0]

            reg_split = instr_split[1].split(",")
            source_reg1 = reg_split[1]
            source_reg2 = reg_split[2]

            if opcode in ["beq", "bne", "blt", "bltu", "bge", "bgeu"]:
                source_reg1 = reg_split[0]
                source_reg2 = reg_split[1]

            decoded_instructions.append({"opcode": opcode, "rs1": source_reg1, "rs2": source_reg2})


    return decoded_instructions

def find_is_reg_or_immediate(source):
    '''
    This function finds whether the source is a register or immediate value
    param[in] source    Source register string
    param[out] True     Source is a register
    param[out] False    Source is an immediate value
    '''
    registers = ["x0", "x1", "x2", "x3", "x4",
                 "x5", "x6", "x7", "x8", "x9",
                 "x10", "x11", "x12", "x13", "x14",
                 "x15", "x16", "x17", "x18", "x19",
                 "x20", "x21", "x22", "x23", "x24",
                 "x25", "x26", "x27", "x28", "x29", "x30", "x31"]
    
    if "x" in source:
        if source in registers:
            return True
        else:
            assert 0, "Invalid source register" + "source register is " + source
    else:
        if any(char.isalpha() for char in source):
            assert 0, "Invalid source register" + "source register is " + source
        else:
            return False
 
def get_source_values(instruction, reg_file):
    '''
    This function reads the register value from the register dump file.
    param[in] instruction: Decoded instructions in the form of dictionary with keys
                           opcode, rs1 and rs2
    param[in] reg_file: Name of the file containing the register dump
    param[out] instruction: Decoded instructions received as input, where rs1 and rs2
                            are replaced by their values
    '''

    register_location = {
        "x0": 0, "x1": 1, "x2": 2, "x3": 3, "x4": 4,
        "x5": 5, "x6": 6, "x7": 8, "x8": 8, "x9": 9,
        "x10": 10, "x11":11, "x12": 12, "x13": 13, "x14": 14,
        "x15": 15, "x16": 16, "x17": 17, "x18": 18, "x19": 19,
        "x20": 20, "x21": 21, "x22": 22, "x23": 23, "x24": 24,
        "x25": 25, "x26": 26, "x27": 27, "x28": 28, "x29": 29,
        "x30": 30, "x31": 31
    }
    
    with open(reg_file, "r") as reg_data:
        data = reg_data.readlines()
        
        for instr in instruction:
            if find_is_reg_or_immediate(instr["rs1"]):
                instr["rs1"] = int(data[register_location[instr["rs1"]]])
            else:
                instr["rs1"] = int(instr["rs1"])
            
            if find_is_reg_or_immediate(instr["rs2"]):
                instr["rs2"] = int(data[register_location[instr["rs2"]]])
            else:
                instr["rs2"] = int(instr["rs2"])

    return instruction


def get_alu_input(instr_file, register_data):
    '''
    This funcion reads the instruction files and generates the inputs to be sent to the ALU

    param[in] instr_file    Path to the file contatining the instructions to be sent to ALU
    param[in] register_data  Path to the file containing the register input

    param[out] alu_input    Dictionary contatining the inputs to be sent to the ALU with the
                            following keys: 
                                1. op
                                2. sx
                                3. nx
                                4. ix
                                5. xy
                                6. ny
                                7. iy
                                8. rs1
                                9. rs2
    '''
    #decode the instructions
    decoded_instructions = decode_instructions(instr_file)
    #get source register values
    decoded_instructions = get_source_values(decoded_instructions, register_data)

    alu_input = []

    for instr in decoded_instructions:
        alu_input.append(instr | get_predefined_code(instr["opcode"]))

    return alu_input


def log_alu_parameters(risc_v_alu):
    '''
    This function logs the value of all the wires in risc_v_alu module
    '''
    risc_v_alu.x._log.info("Value of X: " + hex(risc_v_alu.x.value.integer))
    risc_v_alu.sx._log.info("Value of sx: " + hex(risc_v_alu.sx.value.integer))
    risc_v_alu.nx._log.info("Value of nx: " + hex(risc_v_alu.nx.value.integer))
    risc_v_alu.ix._log.info("Value of ix: " + hex(risc_v_alu.ix.value.integer))
    risc_v_alu.y._log.info("Value of Y: " + hex(risc_v_alu.x.value.integer))
    risc_v_alu.sign_extendedx._log.info("Value of sign extended x: " + hex(risc_v_alu.sign_extendedx.value.integer))
    risc_v_alu.negatedx._log.info("Value of negated X: " + hex(risc_v_alu.negatedx.value.integer))
    risc_v_alu.incrementedx._log.info("Value of incremented X: " + hex(risc_v_alu.incrementedx.value.integer))
    risc_v_alu.sy._log.info("Value of sy: " + hex(risc_v_alu.sy.value.integer))
    risc_v_alu.ny._log.info("Value of ny: " + hex(risc_v_alu.ny.value.integer))
    risc_v_alu.iy._log.info("Value of iy: " + hex(risc_v_alu.iy.value.integer))
    risc_v_alu.sign_extendedy._log.info("Value of sign extended y: " + hex(risc_v_alu.sign_extendedy.value.integer))
    risc_v_alu.negatedy._log.info("Value of negated Y: " + hex(risc_v_alu.negatedy.value.integer))
    risc_v_alu.incrementedy._log.info("Value of incremented Y: " + hex(risc_v_alu.incrementedy.value.integer))
    risc_v_alu.logical_out._log.info("Output of logical operation block: " + hex(risc_v_alu.logical_out.value.integer))
    risc_v_alu.shift_out._log.info("Output of Shift operation block: " + hex(risc_v_alu.shift_out.value.integer))
    risc_v_alu.prefix_out._log.info("Output of Adder operation block: " + hex(risc_v_alu.prefix_out.value.integer))
    risc_v_alu.comparator_out._log.info("Output of Comparator operation block: " + hex(risc_v_alu.comparator_out.value.integer))
    risc_v_alu.out._log.info("Output of ALU: " + hex(risc_v_alu.out.value.integer))





def get_expected_output(alu_input):
    '''
    This function returns the expected output for the instruction under test

    param[in] alu_input     Dictionary returned by get_alu_input function

    param[out] alu_input    Input dictionary appended with expected output
    '''
    expected_output = 0
    rs1 = 0
    rs2 = 0
    
    for input in alu_input:
        rs1 = input["rs1"]
        rs2 = input["rs2"] 

        opcode = input["opcode"]

        match opcode:
            case "addi" : 
                expected_output = rs1 + rs2
            case "slti" : 
                expected_output = (1 if rs1 < rs2 else 0)
            case "sltui": 
                if rs2 < 0:
                    #convert negative number to positive number
                    rs2 = int(pow(2,32)) - abs(rs2)
                expected_output = (1 if rs1 < rs2 else 0)
            case "andi" : 
                expected_output = rs1 & rs2
            case "ori"  : 
                expected_output = rs1 | rs2
            case "xori" : 
                expected_output = rs1 ^ rs2
            case "slli" : 
                expected_output = rs1 << rs2
            case "srli" : 
                expected_output = rs1 >> rs2
            case "srai" : 
                expected_output = (input["rs1"] >> rs2) & 0xFFFFFFFF
            case "add"  : 
                expected_output = rs1 + rs2
            case "slt"  : 
                expected_output = (1 if rs1 < rs2 else 0)
            case "sltu" : 
                if rs2 < 0:
                    #convert negative number to positive number
                    rs2 = int(pow(2,32)) - abs(rs2)
                expected_output = (1 if rs1 < rs2 else 0)
            case "and"  : 
                expected_output = rs1 & rs2
            case "or"   : 
                expected_output = rs1 | rs2
            case "xor"  : 
                expected_output = rs1 ^ rs2
            case "sll"  : 
                expected_output = rs1 << rs2
            case "srl"  : 
                expected_output = rs1 >> rs2
            case "sra"  : 
                expected_output = (input["rs1"] >> rs2) & 0xFFFFFFFF
            case "sub"  : 
                expected_output = rs1 - rs2
            case "beq"  : 
                expected_output = (1 if rs1 == rs2 else 0)
            case "bne"  : 
                expected_output = (1 if rs1 != rs2 else 0)
            case "blt"  : 
                expected_output = (1 if rs1 < rs2 else 0)
            case "bltu" : 
                if rs2 < 0:
                    #convert negative number to positive number
                    rs2 = int(pow(2,32)) - abs(rs2)
                expected_output = (1 if rs1 < rs2 else 0)
            case "bge"  : 
                expected_output = (1 if rs1 > rs2 else 0)
            case "bgeu" : 
                if rs2 < 0:
                    #convert negative number to positive number
                    rs2 = int(pow(2,32)) - abs(rs2)
                expected_output = (1 if rs1 > rs2 else 0)

        input["expected_output"] = (expected_output % (int(pow(2,32))))
    
    return alu_input

@cocotb.test()
async def test_alu_001(risc_v_alu):
    '''
    This funciton tests pre-processing of input x in the ALU
    '''
    x = -2
    #convert to 12 bit number, -2 = FFE
    x = x & 0xFFF

    #set input variables
    risc_v_alu.x.value = x
    risc_v_alu.y.value = 0
    risc_v_alu.nx.value = 1
    risc_v_alu.ix.value = 1
    risc_v_alu.sx.value = 1

    await Timer(1, units='ns')

    risc_v_alu.x._log.info("Value of X: " + hex(risc_v_alu.x.value.integer))
    risc_v_alu.sx._log.info("Value of sx: " + hex(risc_v_alu.sx.value.integer))
    risc_v_alu.nx._log.info("Value of nx: " + hex(risc_v_alu.nx.value.integer))
    risc_v_alu.ix._log.info("Value of ix: " + hex(risc_v_alu.ix.value.integer))
    risc_v_alu.sign_extendedx._log.info("Value of sign extended x: " + hex(risc_v_alu.sign_extendedx.value.integer))
    risc_v_alu.negatedx._log.info("Value of negated X: " + hex(risc_v_alu.negatedx.value.integer))
    risc_v_alu.incrementedx._log.info("Value of incremented X: " + hex(risc_v_alu.incrementedx.value.integer))

    assert risc_v_alu.negatedx == 0x01
    assert risc_v_alu.sign_extendedx == 0xFFFFFFFE
    assert risc_v_alu.incrementedx == 2

    x = 2
    #convert to 12 bit number, -2 = FFE
    x = x & 0xFFF

    #set input variables
    risc_v_alu.x.value = x
    risc_v_alu.y.value = 0
    risc_v_alu.nx.value = 1
    risc_v_alu.ix.value = 1
    risc_v_alu.sx.value = 1

    await Timer(1, units='ns')

    risc_v_alu.x._log.info("Value of X: " + hex(risc_v_alu.x.value.integer))
    risc_v_alu.sx._log.info("Value of sx: " + hex(risc_v_alu.sx.value.integer))
    risc_v_alu.nx._log.info("Value of nx: " + hex(risc_v_alu.nx.value.integer))
    risc_v_alu.ix._log.info("Value of ix: " + hex(risc_v_alu.ix.value.integer))
    risc_v_alu.sign_extendedx._log.info("Value of sign extended x: " + hex(risc_v_alu.sign_extendedx.value.integer))
    risc_v_alu.negatedx._log.info("Value of negated X: " + hex(risc_v_alu.negatedx.value.integer))
    risc_v_alu.incrementedx._log.info("Value of incremented X: " + hex(risc_v_alu.incrementedx.value.integer))

    assert risc_v_alu.negatedx == 0xFFFFFFFD
    assert risc_v_alu.sign_extendedx == 2
    assert risc_v_alu.incrementedx == 0xFFFFFFFE

@cocotb.test()
async def test_alu_002(risc_v_alu):
    '''
    This funciton tests pre-processing of input y in the ALU
    '''
    y = -2
    #convert to 12 bit number, -2 = FFE
    y = y & 0xFFF

    #set input variables
    risc_v_alu.y.value = y
    risc_v_alu.x.value = 0
    risc_v_alu.ny.value = 1
    risc_v_alu.iy.value = 1
    risc_v_alu.sy.value = 1

    await Timer(1, units='ns')

    risc_v_alu.y._log.info("Value of y: " + hex(risc_v_alu.y.value.integer))
    risc_v_alu.sy._log.info("Value of sy: " + hex(risc_v_alu.sy.value.integer))
    risc_v_alu.ny._log.info("Value of ny: " + hex(risc_v_alu.ny.value.integer))
    risc_v_alu.iy._log.info("Value of iy: " + hex(risc_v_alu.iy.value.integer))
    risc_v_alu.sign_extendedy._log.info("Value of sign extended y: " + hex(risc_v_alu.sign_extendedy.value.integer))
    risc_v_alu.negatedy._log.info("Value of negated y: " + hex(risc_v_alu.negatedy.value.integer))
    risc_v_alu.incrementedy._log.info("Value of incremented Y: " + hex(risc_v_alu.incrementedy.value.integer))

    assert risc_v_alu.negatedy == 0x01
    assert risc_v_alu.sign_extendedy == 0xFFFFFFFE
    assert risc_v_alu.incrementedy == 2

    y = 2
    #convert to 12 bit number, -2 = FFE
    y = y & 0xFFF

    #set input variables
    risc_v_alu.y.value = y
    risc_v_alu.x.value = 0
    risc_v_alu.ny.value = 1
    risc_v_alu.iy.value = 1
    risc_v_alu.sy.value = 1

    await Timer(1, units='ns')

    risc_v_alu.y._log.info("Value of Y: " + hex(risc_v_alu.x.value.integer))
    risc_v_alu.sy._log.info("Value of sy: " + hex(risc_v_alu.sy.value.integer))
    risc_v_alu.ny._log.info("Value of ny: " + hex(risc_v_alu.ny.value.integer))
    risc_v_alu.iy._log.info("Value of iy: " + hex(risc_v_alu.iy.value.integer))
    risc_v_alu.sign_extendedy._log.info("Value of sign extended y: " + hex(risc_v_alu.sign_extendedy.value.integer))
    risc_v_alu.negatedy._log.info("Value of negated Y: " + hex(risc_v_alu.negatedy.value.integer))
    risc_v_alu.incrementedy._log.info("Value of incremented Y: " + hex(risc_v_alu.incrementedy.value.integer))

    assert risc_v_alu.negatedy == 0xFFFFFFFD
    assert risc_v_alu.sign_extendedy == 2
    assert risc_v_alu.incrementedy == 0xFFFFFFFE


@cocotb.test()
async def test_risc_v_alu_003(risc_v_alu):
    '''
    This function tests the entire working of RISC V ALU
    '''
    alu_input = get_alu_input("risc_v_alu_test.txt", "register_data.txt")
    alu_input = get_expected_output(alu_input)

    for input in alu_input:
        risc_v_alu._log.info("Instruction under test: " + str(input))

        risc_v_alu.x.value = input["rs1"]
        risc_v_alu.y.value = input["rs2"]
        risc_v_alu.sx.value = input["sx"]
        risc_v_alu.nx.value = input["nx"]
        risc_v_alu.ix.value = input["ix"]
        risc_v_alu.sy.value = input["sy"]
        risc_v_alu.ny.value = input["ny"]
        risc_v_alu.iy.value = input["iy"]
        risc_v_alu.opcode.value = input["op"]

        await Timer(1, units='ns')

        log_alu_parameters(risc_v_alu)

        #check output of ALU with the desired output
        assert risc_v_alu.out.value == input["expected_output"]


