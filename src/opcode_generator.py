def get_predefined_code(input_string):
    predefined_codes = {
        # "code" : "op sx nx ix sy ny iy",
        "addi" : "0 0 0 0 1 0 0",
        "slti" : "5 0 0 0 1 1 1",
        "sltui": "7 0 0 0 1 1 1",
        "andi" : "11 0 0 0 1 0 0",
        "ori"  : "12 0 0 0 1 0 0",
        "xori" : "13 0 0 0 1 0 0",
        "slli" : "2 0 0 0 1 0 0",
        "srli" : "3 0 0 0 1 0 0",
        "srai" : "4 0 0 0 1 0 0",
        "add"  : "0 0 0 0 0 0 0",
        "slt"  : "5 0 0 0 0 1 1",
        "sltu" : "7 0 0 0 0 1 1",
        "and"  : "11 0 0 0 0 0 0",
        "or"   : "12 0 0 0 0 0 0",
        "xor"  : "13 0 0 0 0 0 0",
        "sll"  : "2 0 0 0 0 0 0",
        "srl"  : "3 0 0 0 0 0 0",
        "sra"  : "4 0 0 0 0 0 0",
        "sub"  : "1 0 0 0 0 1 1",
        "beq"  : "9 0 0 0 0 1 1",
        "bne"  : "10 0 0 0 0 1 1",
        "blt"  : "5 0 0 0 0 1 1",
        "bltu" : "7 0 0 0 0 1 1",
        "bge"  : "6 0 0 0 0 1 1",
        "bgeu" : "8 0 0 0 0 1 1",
    }

    # Convert the input string to lowercase for case-insensitive matching
    input_string = input_string.lower()

    # Check if the input string has a predefined code
    if input_string in predefined_codes:
        return predefined_codes[input_string]
    else:
        return "Code not found for input: {}".format(input_string)

# Example usage:
user_input = input("Enter an opcode: ")
result = get_predefined_code(user_input)
print(result)