`ifndef ADDER
`define ADDER
/* This file contains the system verilog implementation of 32 bit
Parallel Prefix adder. Parallel prefix adder is an improvement of
look ahead adder where the carry from one bit to other bit is calculated
on the fly.*/

/*
 * This function does the and operation of 2 one bit operands
 * [in] a 1-Bit operand
 * [in] b 1-Bit operand
 * [out] out 1-Bit Result of a & b
 */
module and2(input logic a, input logic b, output logic out);
    assign out = a & b;
endmodule 

/*
 * This function does the OR operation of 2 one bit operands
 * [in] a 1-Bit operand
 * [in] b 1-Bit operand
 * [out] out 1-Bit Result of a | b
 */
module or2(input logic a, input logic b, output logic out);
    assign out = a | b;
endmodule


/*
 * This function does the XOR operation of 2 one bit operands
 * [in] a 1-Bit operand
 * [in] b 1-Bit operand
 * [out] out 1-Bit Result of a ^ b
 */
module xor2(input logic a, input logic b, output logic out);
    assign out = a ^ b;
endmodule


/*
 * This function does the XOR operation of 3 one bit operands
 * [in] a 1-Bit operand
 * [in] b 1-Bit operand
 * [in] c 1-Bit operand 
 * [out] out 1-Bit Result of a ^ b ^ c
 */
module xor3(input logic a, input logic b, input logic c, output logic out);
    logic temp;
    xor2 xora_b(a, b, temp);
    xor2 xora_b_c(temp, c, out);
endmodule

/*
 * This function generates the propogate and generate term
 * [in] x 1-Bit operand
 * [in] y 1-Bit operand
 * [out] p 1-Bit propogate term
 * [out] g 1-Bit generate term
 */
module propagate_generate(input logic x, y, output logic p,g);
    or2 prop(x, y, p);
    and2 gen(x, y, g);
endmodule

/*
 * This function generates the carry that needs to be forwarded to
 * the next full adder in the sequence
 * Gij = Gik + G(k-1)j & Pi:k
 * Pij = Pik & P(k-1)j
 * [in] pik   1-Bit operand(Pik)
 * [in] pk_1j 1-Bit operand(P(k-1)j)
 * [in] gik   1-Bit operand(Gik)
 * [in] gk_1j 1-Bit operand(G(k-1)j)
 * [out] pij 1-Bit propogate term generated from combining i:k and 
 *           k-1:j
 * [out] gij 1-Bit generate term genearted from combining i:k and 
 *           k-1:j
 */
module carry(input logic pik, pk_1j, gik, gk_1j, output logic pij, gij);
    logic temp;
    and2 prop_ij(pik, pk_1j, pij);
    and2 temp_gen(gk_1j, pik, temp);
    or2 gen_ij(gik, temp, gij);
endmodule 

/*
 * This function calculates the sum output of the full adder
 * [in] x 1-Bit operand of Full adder
 * [in] y 1-Bit operand of Full adder
 * [in] g 1-Bit operand of Full adder(Generate term calculated)
 * [out] sum 1-Bit sum output of full adder
 */
module sum(input logic x, y, g, output logic sum);
    xor3 sum_fa(x, y, g, sum);
endmodule


/*
 * This function implements the Parallel prefix adder
 * [in] a 32-Bit input operand to the prefix adder
 * [in] b 32-Bit input operand to the prefix adder
 * [in] cin 1-Bit carry input to the prefix adder
 * [in] a_sign 1-Bit actual sign of the operand a 
 * [in] b_sign 1-Bit actual sign of the operand b
 * [in] sub 1-Bit indicating whether the adder is performing addition or
 *          2's complement subtraction.
 *          sub = 0: addition
 *          sub = 1: 2's complement subtraction
 * [out] sum 32-Bit sum calculated
 * [out] carry_out 1-Bit flag indicating whether carry is generated
 * [out] overflow 1-Bit flag indicating whether overflow happened
 * [out] negative 1-Bit flag indicating whether the Result is negative
 * [out] ZeroFlag 1-Bit flag indicating whether the output is zero
 */
module prefixAdder(input logic [31:0] a,b,
                   input logic cin, a_sign, b_sign,
                   input logic [3:0] opcode,
                   output logic [31:0] Result,
                   output logic carry_out, overflow, negative, ZeroFlag);
    logic p[31:0], g[31:0];
    logic pij[31:0], gij[31:0];
    logic sub;

    // calculate the propogate and generate bits for each bit
    generate
    genvar i;
    for (i = 0; i < 32; i = i + 1) 
        propagate_generate pro_gen(a[i], b[i], p[i], g[i]); 
    endgenerate

    assign pij[0] = 0;
    assign gij[0] = 0;

    assign sub = (opcode == 0) ? 0:1;

    // N = 32, there are 5 levels in the prefix adder

    // level 1
    logic g2_1, g4_3, g6_5, g8_7, g10_9, g12_11, g14_13;
    logic g16_15, g18_17, g20_19, g22_21, g24_23, g26_25;
    logic g28_27, g30_29;

    logic p2_1, p4_3, p6_5, p8_7, p10_9, p12_11, p14_13;
    logic p16_15, p18_17, p20_19, p22_21, p24_23, p26_25;
    logic p28_27, p30_29;

    carry c0(p[0], 1'b0, g[0], cin, pij[1], gij[1]);
    carry c1(p[2], p[1], g[2], g[1], p2_1, g2_1);
    carry c2(p[4], p[3], g[4], g[3], p4_3, g4_3);
    carry c3(p[6], p[5], g[6], g[5], p6_5, g6_5);
    carry c4(p[8], p[7], g[8], g[7], p8_7, g8_7);
    carry c5(p[10], p[9], g[10], g[9], p10_9, g10_9);
    carry c6(p[12], p[11], g[12], g[11], p12_11, g12_11);
    carry c7(p[14], p[13], g[14], g[13], p14_13, g14_13);
    carry c8(p[16], p[15], g[16], g[15], p16_15, g16_15);
    carry c9(p[18], p[17], g[18], g[17], p18_17, g18_17);
    carry c10(p[20], p[19], g[20], g[19], p20_19, g20_19);
    carry c11(p[22], p[21], g[22], g[21], p22_21, g22_21);
    carry c12(p[24], p[23], g[24], g[23], p24_23, g24_23);
    carry c13(p[26], p[25], g[26], g[25], p26_25, g26_25);
    carry c14(p[28], p[27], g[28], g[27], p28_27, g28_27);
    carry c15(p[30], p[29], g[30], g[29], p30_29, g30_29);

    // level 2
    logic g5_3, g6_3, g9_7, g10_7, g13_11, g14_11, g17_15, g18_15;
    logic g21_19, g22_19, g25_23, g26_23, g29_27, g30_27;

    logic p5_3, p6_3, p9_7, p10_7, p13_11, p14_11, p17_15, p18_15;
    logic p21_19, p22_19, p25_23, p26_23, p29_27, p30_27;

    carry c16(p[1], pij[1], g[1], gij[1], pij[2], gij[2]);
    carry c17(p2_1, pij[1], g2_1, gij[1], pij[3], gij[3]);
    carry c18(p[5], p4_3, g[5], g4_3, p5_3, g5_3);
    carry c19(p6_5, p4_3, g6_5, g4_3, p6_3, g6_3);
    carry c20(p[9], p8_7, g[9], g8_7, p9_7, g9_7);
    carry c21(p10_9, p8_7, g10_9, g8_7, p10_7, g10_7);
    carry c22(p[13], p12_11, g[13], g12_11, p13_11, g13_11);
    carry c23(p14_13, p12_11, g14_13, g12_11, p14_11, g14_11);
    carry c24(p[17], p16_15, g[17], g16_15, p17_15, g17_15);
    carry c25(p18_17, p16_15, g18_17, g16_15, p18_15, g18_15);
    carry c26(p[21], p20_19, g[21], g20_19, p21_19, g21_19);
    carry c27(p22_21, p20_19, g22_21, g20_19, p22_19, g22_19);
    carry c28(p[25], p24_23, g[25], g24_23, p25_23, g25_23);
    carry c29(p26_25, p24_23, g26_25, g24_23, p26_23, g26_23);
    carry c30(p[29], p28_27, g[29], g28_27, p29_27, g29_27);
    carry c31(p30_29, p28_27, g30_29, g28_27, p30_27, g30_27);

    // level 3
    logic g11_7, g12_7, g13_7, g14_7;
    logic g19_15, g20_15, g21_15, g22_15;
    logic g27_23, g28_23, g29_23, g30_23;

    logic p11_7, p12_7, p13_7, p14_7;
    logic p19_15, p20_15, p21_15, p22_15;
    logic p27_23, p28_23, p29_23, p30_23;

    carry c32(p[3], pij[3], g[3], gij[3], pij[4], gij[4]);
    carry c33(p4_3, pij[3], g4_3, gij[3], pij[5], gij[5]);
    carry c34(p5_3, pij[3], g5_3, gij[3], pij[6], gij[6]);
    carry c35(p6_3, pij[3], g6_3, gij[3], pij[7], gij[7]);

    carry c36(p[11], p10_7, g[11], g10_7, p11_7, g11_7);
    carry c37(p12_11, p10_7, g12_11, g10_7, p12_7, g12_7);
    carry c38(p13_11, p10_7, g13_11, g10_7, p13_7, g13_7);
    carry c39(p14_11, p10_7, g14_11, g10_7, p14_7, g14_7);

    carry c40(p[19], p18_15, g[19], g18_15, p19_15, g19_15);
    carry c41(p20_19, p18_15, g20_19, g18_15, p20_15, g20_15);
    carry c42(p21_19, p18_15, g21_19, g18_15, p21_15, g21_15);
    carry c43(p22_19, p18_15, g22_19, g18_15, p22_15, g22_15);

    carry c44(p[27], p26_23, g[27], g26_23, p27_23, g27_23);
    carry c45(p28_27, p26_23, g28_27, g26_23, p28_23, g28_23);
    carry c46(p29_27, p26_23, g29_27, g26_23, p29_23, g29_23);
    carry c47(p30_27, p26_23, g30_27, g26_23, p30_23, g30_23);

    //level 4
    logic g23_15, g24_15, g26_15, g27_15, g28_15, g29_15, g30_15;
    logic p23_15, p24_15, p26_15, p27_15, p28_15, p29_15, p30_15;

    carry c48(p[7], pij[7], g[7], gij[7], pij[8], gij[8]);
    carry c49(p8_7, pij[7], g8_7, gij[7], pij[9], gij[9]);
    carry c50(p9_7, pij[7], g9_7, gij[7], pij[10], gij[10]);
    carry c51(p10_7, pij[7], g10_7, gij[7], pij[11], gij[11]);
    carry c52(p11_7, pij[7], g11_7, gij[7], pij[12], gij[12]);
    carry c53(p12_7, pij[7], g12_7, gij[7], pij[13], gij[13]);
    carry c54(p13_7, pij[7], g13_7, gij[7], pij[14], gij[14]);
    carry c55(p14_7, pij[7], g14_7, gij[7], pij[15], gij[15]);

    carry c56(p[23], p22_15, g[23], g22_15, p23_15, g23_15);
    carry c57(p24_23, p22_15, g24_23, g22_15, p24_15, g24_15);
    carry c58(p25_23, p22_15, g25_23, g22_15, p25_15, g25_15);
    carry c59(p26_23, p22_15, g26_23, g22_15, p26_15, g26_15);
    carry c60(p27_23, p22_15, g27_23, g22_15, p27_15, g27_15);
    carry c61(p28_23, p22_15, g28_23, g22_15, p28_15, g28_15);
    carry c62(p29_23, p22_15, g29_23, g22_15, p29_15, g29_15);
    carry c63(p30_23, p22_15, g30_23, g22_15, p30_15, g30_15);

    // level 5
    carry c64(p[15], pij[15], g[15], gij[15], pij[16], gij[16]);
    carry c65(p16_15, pij[15], g16_15, gij[15], pij[17], gij[17]);
    carry c66(p17_15, pij[15], g17_15, gij[15], pij[18], gij[18]);
    carry c67(p18_15, pij[15], g18_15, gij[15], pij[19], gij[19]);
    carry c68(p19_15, pij[15], g19_15, gij[15], pij[20], gij[20]);
    carry c69(p20_15, pij[15], g20_15, gij[15], pij[21], gij[21]);
    carry c70(p21_15, pij[15], g21_15, gij[15], pij[22], gij[22]);
    carry c71(p22_15, pij[15], g22_15, gij[15], pij[23], gij[23]);
    carry c72(p23_15, pij[15], g23_15, gij[15], pij[24], gij[24]);
    carry c73(p24_15, pij[15], g24_15, gij[15], pij[25], gij[25]);
    carry c74(p25_15, pij[15], g25_15, gij[15], pij[26], gij[26]);
    carry c75(p26_15, pij[15], g26_15, gij[15], pij[27], gij[27]);
    carry c76(p27_15, pij[15], g27_15, gij[15], pij[28], gij[28]);
    carry c77(p28_15, pij[15], g28_15, gij[15], pij[29], gij[29]);
    carry c78(p29_15, pij[15], g29_15, gij[15], pij[30], gij[30]);
    carry c79(p30_15, pij[15], g30_15, gij[15], pij[31], gij[31]);

    sum s0(a[0], b[0], cin, Result[0]);

    generate
        genvar j;
        for (j = 1; j <= 31; j++)
            sum si(a[j], b[j], gij[j], Result[j]);
    endgenerate

    assign carry_out = (a[31] & b[31]) | (b[31] & gij[31]) | (gij[31] & a[31]);
    assign overflow = (~(a_sign ^ b_sign ^ sub)) & (Result[31] ^ a_sign);
    assign ZeroFlag = (Result == 32'b0) ? 1'b1 : 1'b0;
    assign negative = (Result[31] == 1'b1) ? 1'b1 : 1'b0;

endmodule

`endif


