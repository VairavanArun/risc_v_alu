import cocotb
import pytest
from cocotb.triggers import Timer

@cocotb.test()
async def test_comparator_001(comparator):
    '''
    This function tests signed less than opcode when
    a and b are both negative
    a is positive, b is negative
    a is negative, b is positive
    a and b, both are positive
    '''
    result = []
    a = [-10, 9, -8, 7]
    b = [-11, -10, 9, 8]
    expected_result = [0, 0, 1, 1]

    for (a_in, b_in) in zip(a,b):
        comparator.opcode.value = 4
        comparator.A.value = a_in
        negative_bin = ((~b_in) + 1) % (int(pow(2,32)))
        comparator.B.value = negative_bin
        a_sign = 1 if a_in < 0 else 0
        b_sign = 1 if b_in < 0 else 0
        comparator.a_sign.value = a_sign
        comparator.b_sign.value = b_sign

        await Timer(1, "ns") 

        comparator.A._log.info("Setting of A to " + str(comparator.A.value.binstr) + "(" + str(a_in) + ")")
        comparator.B._log.info("Setting of B to " + str(comparator.B.value.binstr) + "(" + str(b_in) + ")")
        comparator.a_sign._log.info("Setting of a_sign to " + str(comparator.a_sign.value.binstr))
        comparator.b_sign._log.info("Setting of b_sign to " + str(comparator.b_sign.value.binstr))

        comparator.carry_out._log.info("Carry out = " + str(comparator.carry_out.value.binstr))
        comparator.overflow._log.info("Overflow = " + str(comparator.overflow.value.binstr))
        comparator.negative._log.info("Negative = " + str(comparator.negative.value.binstr))
        comparator.zero._log.info("Zero = " +str(comparator.zero.value.binstr))
        comparator.Result._log.info("Result = " + str(comparator.Result.value.binstr))
        result.append(comparator.Result.value.integer)

    for (result_out, exp_res) in zip(result, expected_result):
        assert result_out == exp_res

@cocotb.test()
async def test_comparator_002(comparator):
    '''
    This function tests signed greater than opcode when
    a and b are both negative
    a is positive, b is negative
    a is negative, b is positive
    a and b, both are positive
    '''
    result = []
    a = [-10, 9, -8, 7]
    b = [-11, -10, 9, 8]
    expected_result = [1, 1, 0, 0]

    for (a_in, b_in) in zip(a,b):
        comparator.opcode.value = 5
        comparator.A.value = a_in
        negative_bin = ((~b_in) + 1) % (int(pow(2,32)))
        comparator.B.value = negative_bin
        a_sign = 1 if a_in < 0 else 0
        b_sign = 1 if b_in < 0 else 0
        comparator.a_sign.value = a_sign
        comparator.b_sign.value = b_sign

        await Timer(1, "ns") 

        comparator.A._log.info("Setting of A to " + str(comparator.A.value.binstr) + "(" + str(a_in) + ")")
        comparator.B._log.info("Setting of B to " + str(comparator.B.value.binstr) + "(" + str(b_in) + ")")

        comparator.Result._log.info("Result = " + str(comparator.Result.value.binstr))
        result.append(comparator.Result.value.integer)

    for (result_out, exp_res) in zip(result, expected_result):
        assert result_out == exp_res


@cocotb.test()
async def test_comparator_003(comparator):
    '''
    This function tests unsigned less than opcode when
    a and b are both negative
    a is positive, b is negative
    a is negative, b is positive
    a and b, both are positive
    '''
    result = []
    a = [i for i in range(0,10)]
    b = [i for i in range(11,21)]
    expected_result = 1

    for (a_in, b_in) in zip(a,b):
        comparator.opcode.value = 6
        comparator.A.value = a_in
        negative_bin = ((~b_in) + 1) % (int(pow(2,32)))
        comparator.B.value = negative_bin
        a_sign = 1 if a_in < 0 else 0
        b_sign = 1 if b_in < 0 else 0
        comparator.a_sign.value = a_sign
        comparator.b_sign.value = b_sign

        await Timer(1, "ns") 

        comparator.A._log.info("Setting of A to " + str(comparator.A.value.binstr) + "(" + str(a_in) + ")")
        comparator.B._log.info("Setting of B to " + str(comparator.B.value.binstr) + "(" + str(b_in) + ")")
        comparator.a_sign._log.info("Setting of a_sign to " + str(comparator.a_sign.value.binstr))
        comparator.b_sign._log.info("Setting of b_sign to " + str(comparator.b_sign.value.binstr))

        comparator.Result._log.info("Result = " + str(comparator.Result.value.binstr))
        result.append(comparator.Result.value.integer)

    for result_out in result:
        assert result_out == expected_result


@cocotb.test()
async def test_comparator_004(comparator):
    '''
    This function tests unsigned greater than opcode when
    a and b are both negative
    a is positive, b is negative
    a is negative, b is positive
    a and b, both are positive
    '''
    result = []
    a = [i for i in range(0,10)]
    b = [i for i in range(11,21)]
    expected_result = 0

    for (a_in, b_in) in zip(a,b):
        comparator.opcode.value = 7
        comparator.A.value = a_in
        negative_bin = ((~b_in) + 1) % (int(pow(2,32)))
        comparator.B.value = negative_bin
        a_sign = 1 if a_in < 0 else 0
        b_sign = 1 if b_in < 0 else 0
        comparator.a_sign.value = a_sign
        comparator.b_sign.value = b_sign

        await Timer(1, "ns") 

        comparator.A._log.info("Setting of A to " + str(comparator.A.value.binstr) + "(" + str(a_in) + ")")
        comparator.B._log.info("Setting of B to " + str(comparator.B.value.binstr) + "(" + str(b_in) + ")")

        comparator.Result._log.info("Result = " + str(comparator.Result.value.binstr))
        result.append(comparator.Result.value.integer)

    for result_out in result:
        assert result_out == expected_result