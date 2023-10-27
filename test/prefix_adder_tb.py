import cocotb
import pytest
from cocotb.triggers import Timer


def print_signals(prefix_adder):
    prefix_adder.a._log.info("Value of a is: b\'" + str(prefix_adder.a.value.binstr))
    prefix_adder.b._log.info("Value of b is: b\'" + str(prefix_adder.b.value.binstr))
    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == 0
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 1 


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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == 1
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0 


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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == 2
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0 


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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == 30
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0 


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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == (255 + 255)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0


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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == (511 + 511)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0

@cocotb.test()
async def test_prefix_adder_006(prefix_adder):
    '''
    This function tests addition of 65535+65535
    '''
    cocotb.log.info("Testing addition of 65535+65535")

    prefix_adder.a._log.info("Setting value of a to 65535")
    prefix_adder.a.value = 65535

    prefix_adder.b._log.info("Setting value of b to 65535")
    prefix_adder.b.value = 65535

    prefix_adder.cin.value = 0

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    assert prefix_adder.sum.value.integer == (65535 + 65535)
    assert prefix_adder.carry_out.value.integer == 0
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == 0
    assert prefix_adder.zero.value.integer == 0


@cocotb.test()
async def test_prefix_adder_007(prefix_adder):
    '''
    This function tests addition of 2^32 - 1 + 2^32 - 1
    '''
    cocotb.log.info("Testing addition of 2^32 - 1 + 2^32 - 1")

    prefix_adder.a._log.info("Setting value of a to 2^32 - 1")
    prefix_adder.a.value = int(pow(2,32)) - 1

    prefix_adder.b._log.info("Setting value of b to 2^32 - 1")
    prefix_adder.b.value = int(pow(2,32)) - 1

    prefix_adder.cin.value = 0

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    expected_sum = (int(pow(2,32)) - 1 + int(pow(2,32)) - 1) % (int(pow(2,32)))
    expected_carry = (int(pow(2,32)) - 1 + int(pow(2,32)) - 1) // (int(pow(2,32)))
    expected_negative = expected_sum >> 31
    expected_zero = 1 if expected_sum == 0 else 0

    assert prefix_adder.sum.value.integer == expected_sum
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.zero.value.integer == expected_zero


@cocotb.test()
async def test_prefix_adder_008(prefix_adder):
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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    expected_sum = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_sum >> 31
    expected_zero = 1 if expected_sum == 0 else 0

    assert prefix_adder.sum.value.integer == expected_sum
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.zero.value.integer == expected_zero


@cocotb.test()
async def test_prefix_adder_009(prefix_adder):
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

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    expected_sum = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_sum >> 31
    expected_zero = 1 if expected_sum == 0 else 0

    assert prefix_adder.sum.value.integer == expected_sum
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.zero.value.integer == expected_zero

@cocotb.test()
async def test_prefix_adder_010(prefix_adder):
    '''
    This function tests addition of 2863311530 and 1431655765
    2863311530 = b'10101010101010101010101010101010
    1431655765 = b'01010101010101010101010101010101
    '''
    cocotb.log.info("Testing addition of 2863311530 + 1431655765")

    a = 2863311530
    b = 1431655765

    prefix_adder.a._log.info("Setting value of a to 2863311530")
    prefix_adder.a.value = a

    prefix_adder.b._log.info("Setting value of b to 1431655765")
    prefix_adder.b.value = b

    prefix_adder.cin.value = 0

    await Timer(1, units='ns')

    prefix_adder.sum._log.info("Value of sum is: b\'" + str(prefix_adder.sum.value.binstr))
    prefix_adder.carry_out._log.info("Value of Carry out is: b\'" + str(prefix_adder.carry_out.value.binstr))
    prefix_adder.overflow._log.info("Value of Overflow flag is: b\'" + str(prefix_adder.overflow.value.binstr))
    prefix_adder.negative._log.info("Value of Negative flag is: b\'" + str(prefix_adder.negative.value.binstr))
    prefix_adder.zero._log.info("Value of Zero is: b\'" + str(prefix_adder.zero.value.binstr))

    expected_sum = (a + b) % (int(pow(2,32)))
    expected_carry = (a + b) // (int(pow(2,32)))
    expected_negative = expected_sum >> 31
    expected_zero = 1 if expected_sum == 0 else 0

    assert prefix_adder.sum.value.integer == expected_sum
    assert prefix_adder.carry_out.value.integer == expected_carry
    assert prefix_adder.overflow.value.integer == 0
    assert prefix_adder.negative.value.integer == expected_negative
    assert prefix_adder.zero.value.integer == expected_zero
