import cocotb
import pytest
from cocotb.triggers import Timer

def get_expected_overflow(a_sign, b_sign, sub, expected_Result):
    expected_overflow = 0
    if a_sign == b_sign:
        if sub:
            expected_overflow = 0
        else:
            expected_overflow = 1
    else:
        if sub:
            expected_overflow = 1
        else:
            expected_overflow = 0 
    expected_overflow = expected_overflow & ((expected_Result >> 31) ^ a_sign)

    return expected_overflow


def print_signals(prefix_adder):
    prefix_adder.a._log.info("Value of a is: b\'" + str(prefix_adder.a.value.binstr))
    prefix_adder.b._log.info("Value of b is: b\'" + str(prefix_adder.b.value.binstr))
    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

@cocotb.test()
async def test_prefix_adder_001(prefix_adder):
    '''
    This function tests addition of 0+0
    '''
    cocotb.log.info("Testing addition of 0+0")

    prefix_adder.a._log.info("Setting value of a to 0")
    prefix_adder.a.value = 0

    prefix_adder.b._log.info("Setting value of b to 0")
    prefix_adder.b.value = 0

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(0, 0, 0, 0)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == 0
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 1 


@cocotb.test()
async def test_prefix_adder_002(prefix_adder):
    '''
    This function tests addition of 0+1
    '''
    cocotb.log.info("Testing addition of 0+1")

    prefix_adder.a._log.info("Setting value of a to 0")
    prefix_adder.a.value = 0

    prefix_adder.b._log.info("Setting value of b to 1")
    prefix_adder.b.value = 1

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 1)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == 1
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0 


@cocotb.test()
async def test_prefix_adder_003(prefix_adder):
    '''
    This function tests addition of 1+1
    '''
    cocotb.log.info("Testing addition of 1+1")

    prefix_adder.a._log.info("Setting value of a to 1")
    prefix_adder.a.value = 1

    prefix_adder.b._log.info("Setting value of b to 1")
    prefix_adder.b.value = 1

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 2)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == 2
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0 


@cocotb.test()
async def test_prefix_adder_004(prefix_adder):
    '''
    This function tests addition of 15+15
    '''
    cocotb.log.info("Testing addition of 15+15")

    prefix_adder.a._log.info("Setting value of a to 15")
    prefix_adder.a.value = 15

    prefix_adder.b._log.info("Setting value of b to 15")
    prefix_adder.b.value = 15

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 30)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == 30
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0 


@cocotb.test()
async def test_prefix_adder_005(prefix_adder):
    '''
    This function tests addition of 255+255
    '''
    cocotb.log.info("Testing addition of 255+255")

    prefix_adder.a._log.info("Setting value of a to 255")
    prefix_adder.a.value = 255

    prefix_adder.b._log.info("Setting value of b to 255")
    prefix_adder.b.value = 255

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 255 + 255)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == (255 + 255)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0


@cocotb.test()
async def test_prefix_adder_006(prefix_adder):
    '''
    This function tests addition of 511+511
    '''
    cocotb.log.info("Testing addition of 511+511")

    prefix_adder.a._log.info("Setting value of a to 511")
    prefix_adder.a.value = 511

    prefix_adder.b._log.info("Setting value of b to 511")
    prefix_adder.b.value = 511

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 511 + 511)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == (511 + 511)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0

@cocotb.test()
async def test_prefix_adder_007(prefix_adder):
    '''
    This function tests addition of 65535+65535
    '''
    cocotb.log.info("Testing addition of 65535+65535")

    prefix_adder.a._log.info("Setting value of a to 65535")
    prefix_adder.a.value = 65535

    prefix_adder.b._log.info("Setting value of b to 65535")
    prefix_adder.b.value = 65535

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = 65535 + 65535)

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    assert prefix_adder.Result.value.integer == (65535 + 65535)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.ZeroFlag.value.integer == 0


@cocotb.test()
async def test_prefix_adder_008(prefix_adder):
    '''
    This function tests addition of 2^32 - 1 + 2^32 - 1
    '''
    cocotb.log.info("Testing addition of 2^32 - 1 + 2^32 - 1")

    prefix_adder.a._log.info("Setting value of a to 2^32 - 1")
    prefix_adder.a.value = int(pow(2,32)) - 1

    prefix_adder.b._log.info("Setting value of b to 2^32 - 1")
    prefix_adder.b.value = int(pow(2,32)) - 1

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 1
    prefix_adder.b_sign.value = 1
    prefix_adder.opcode.value = 0


    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (int(pow(2,32)) - 1 + int(pow(2,32)) - 1) % (int(pow(2,32)))
    expected_carry = (int(pow(2,32)) - 1 + int(pow(2,32)) - 1) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 1, b_sign = 1, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_009(prefix_adder):
    '''
    This function tests addition of 2863311530 and 2863311530
    2863311530 = b'10101010101010101010101010101010
    '''
    cocotb.log.info("Testing addition of 2863311530 + 2863311530")

    a = 2863311530
    b = 2863311530

    prefix_adder.a._log.info("Setting value of a to 2863311530")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 2863311530")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 1
    prefix_adder.b_sign.value =  1
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 1, b_sign = 1, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_010(prefix_adder):
    '''
    This function tests addition of 1431655765 and 1431655765
    1431655765 = b'01010101010101010101010101010101
    '''
    cocotb.log.info("Testing addition of 1431655765 + 1431655765")

    a = 1431655765
    b = 1431655765

    prefix_adder.a._log.info("Setting value of a to 1431655765")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 1431655765")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 0, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag

@cocotb.test()
async def test_prefix_adder_011(prefix_adder):
    '''
    This function tests addition of 2^32 - 1  and 1431655765
    1431655765 = b'01010101010101010101010101010101
    2863311530 = b'10101010101010101010101010101010
    '''
    cocotb.log.info("Testing addition of 2863311530 + 1431655765")

    a = 1431655765
    b = 2863311530

    prefix_adder.a._log.info("Setting value of a to 1431655765")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 2863311530")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 0
    prefix_adder.b_sign.value =  1
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 0, b_sign = 1, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_012(prefix_adder):
    '''
    This function tests addition of 2^32 - 1  and 2863311530
    2^32 - 1 = b'11111111111111111111111111111111
    2863311530 = b'10101010101010101010101010101011
    '''
    cocotb.log.info("Testing addition of 2^32 - 1 + 1431655765")

    a = int(pow(2,32)) - 1
    b = 2863311530

    prefix_adder.a._log.info("Setting value of a to 2^32 - 1")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 2863311530")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 1
    prefix_adder.b_sign.value =  1
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 1, b_sign = 1, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag

@cocotb.test()
async def test_prefix_adder_013(prefix_adder):
    '''
    This function tests addition of 2^32 - 1  and 1431655765
    2^32 - 1 = b'11111111111111111111111111111111
    1431655765 = b'01010101010101010101010101010101
    '''
    cocotb.log.info("Testing addition of 2^32 - 1 + 1431655765")

    a = int(pow(2,32)) - 1
    b = 1431655765

    prefix_adder.a._log.info("Setting value of a to 2^32 - 1")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 1431655765")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0
    prefix_adder.a_sign.value = 1
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 1, b_sign = 0, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag

@cocotb.test()
async def test_prefix_adder_014(prefix_adder):
    '''
    This function tests addition of 2^32 - 1  and 0 and cin = 1
    2^32 - 1 = b'11111111111111111111111111111111
    '''
    cocotb.log.info("Testing addition of 2^32 - 1 + 1")

    a = int(pow(2,32)) - 1
    b = 0
    cin = 1

    prefix_adder.a._log.info("Setting value of a to 2^32 - 1")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 0")
    prefix_adder.b.value = b

    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = 1
    prefix_adder.b_sign.value =  0
    prefix_adder.opcode.value =  0

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is: b\'" + str(prefix_adder.Result.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b + cin) % (int(pow(2,32)))
    expected_carry = (a + b + cin) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign = 1, b_sign = 0, sub = 0, expected_Result = expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag

@cocotb.test()
async def test_prefix_adder_015(prefix_adder):
    '''
    This function tests addition of 0 and -1 and the setting of overflow flag
    '''
    a = 0
    b = -1
    cin = 0
    sub = 0
    a_sign = 0
    b_sign = 1

    cocotb.log.info("Testing addition of 0 and -1")
    prefix_adder.a._log.info("Setting value of a to 0")
    prefix_adder.a.value = 0

    prefix_adder.a._log.info("Setting value of b to -1")
    prefix_adder.b.value = -1
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b + cin) % (int(pow(2,32)))
    expected_carry = abs((a + b + cin)) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_016(prefix_adder):
    '''
    This function tests subtraction of 0 and -1 and the setting of overflow flag
    '''
    a = 0
    b = -1
    negative_b = (~b) + 1
    cin = 0
    sub = 1
    a_sign = 0
    b_sign = 1

    cocotb.log.info("Testing subtraction of 0 and -1")
    prefix_adder.a._log.info("Setting value of a to 0")
    prefix_adder.a.value = 0

    prefix_adder.a._log.info("Setting value of b to -1")
    prefix_adder.b.value = negative_b
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a - b + cin) % (int(pow(2,32)))
    expected_carry = abs((a - b + cin)) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_017(prefix_adder):
    '''
    This function tests addition of -1 and 0 and the setting of overflow flag
    '''
    a = -1
    b = 0
    cin = 0
    sub = 0
    a_sign = 1
    b_sign = 0

    cocotb.log.info("Testing addition of -1 and 0")
    prefix_adder.a._log.info("Setting value of a to -1")
    prefix_adder.a.value = a

    prefix_adder.a._log.info("Setting value of b to 0")
    prefix_adder.b.value = b
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b + cin) % (int(pow(2,32)))
    expected_carry = abs((a + b + cin)) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_018(prefix_adder):
    '''
    This function tests subtraction of -1 and 0 and the setting of overflow flag
    '''
    a = -1
    b = 0
    negative_b = (~b) + 1
    cin = 0
    sub = 1
    a_sign = 1
    b_sign = 0

    cocotb.log.info("Testing subtraction of -1 and 0")
    prefix_adder.a._log.info("Setting value of a to -1")
    prefix_adder.a.value = a

    prefix_adder.a._log.info("Setting value of b to 0")
    prefix_adder.b.value = negative_b
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a - b + cin) % (int(pow(2,32)))
    expected_carry = abs((a - b + cin)) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_019(prefix_adder):
    '''
    This function tests addition of -1 and -1 and the setting of overflow flag
    '''
    a = -1
    b = -1
    cin = 0
    sub = 0
    a_sign = 1
    b_sign = 1

    cocotb.log.info("Testing addition of -1 and -1")
    prefix_adder.a._log.info("Setting value of a to -1")
    prefix_adder.a.value = a

    prefix_adder.a._log.info("Setting value of b to -1")
    prefix_adder.b.value = b
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a + b + cin) % (int(pow(2,32)))
    expected_carry = 1
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag


@cocotb.test()
async def test_prefix_adder_020(prefix_adder):
    '''
    This function tests subtraction of -1 and -1 and the setting of overflow flag
    '''
    a = -1
    b = 0
    negative_b = (~b) + 1
    cin = 0
    sub = 1
    a_sign = 1
    b_sign = 1

    cocotb.log.info("Testing subtraction of -1 and -1")
    prefix_adder.a._log.info("Setting value of a to -1")
    prefix_adder.a.value = a

    prefix_adder.a._log.info("Setting value of b to -1")
    prefix_adder.b.value = negative_b
    
    prefix_adder.cin.value = cin
    prefix_adder.a_sign.value = a_sign
    prefix_adder.b_sign.value = b_sign
    prefix_adder.opcode.value =  sub

    await Timer(1, units='ns')

    prefix_adder.Result._log.info("Value of Result is:" + str(prefix_adder.Result.value.integer) + "(b\'" + str(prefix_adder.Result.value.binstr) + ")")
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.ZeroFlag._log.info("Value of ZeroFlag is: b\'" + str(prefix_adder.ZeroFlag.value.binstr))

    expected_Result = (a - b + cin) % (int(pow(2,32)))
    expected_carry = abs((a - b + cin)) // (int(pow(2,32)))
    expected_negative = expected_Result >> 31
    expected_ZeroFlag = 1 if expected_Result == 0 else 0
    expected_overflow = get_expected_overflow(a_sign, b_sign, sub, expected_Result)

    assert prefix_adder.Result.value.integer == expected_Result
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == expected_overflow
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.ZeroFlag.value.integer == expected_ZeroFlag
