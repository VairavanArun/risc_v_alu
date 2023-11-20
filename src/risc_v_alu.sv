/* This file contains the implementation of RISC-V ALU using system verilog
 * The architecture of the RISC-V AlU is as follows
 *  nx ix sx ny iy sy opcode(4 bits)
 *   |  | |  |  |  |  | | | |
 *  --------------------------
 * |                           \
 * |                            \________
 * |                            /
 * |                           /
 *  --------------------------
 * nx - negate x
 * ix - increment x
 * sx - sign extend x
 * ny - negate y
 * iy - increment y
 * sy - sign extend y
 * opcode - 4 bits operation code
 */

`include "../src/prefix_adder.sv"
`include "../src/comparator.sv"
`include "../src/shifters.sv"

module RISC_V_ALU(input logic [31:0] x,y,
                  input logic nx, ix, sx,
                  input logic ny, iy, sy,
                  input logic [3:0] opcode,
                  output logic [31:0] out,
                  output logic ZeroFlag);

    logic [31:0] negatedx, incrementedx, sign_extendedx;
    logic [31:0] negatedy, incrementedy, sign_extendedy;
    logic [31:0] logical_out, shift_out, prefix_out, comparator_out;
    logic carry_in, x_sign, y_sign;
    logic carry_out, overflow, negative, zero_prefix, zero_logic, zero_comparator, zero_shift;



        /* X operations */
        assign sign_extendedx = (sx == 1) ? ({ {30{x[11]}}, x[11:0] }):
                                            (x);
        
        assign x_sign = sign_extendedx[31];
        
        assign negatedx = (nx == 1) ? (~sign_extendedx):
                                        (sign_extendedx);


        assign incrementedx = (ix == 1) ? (negatedx + 1):
                                            (negatedx);

        
        /* Y operations */
        assign sign_extendedy = (sy == 1) ? ({ {30{y[11]}}, y[11:0] }):
                                            (y);

        assign y_sign = sign_extendedy[31];

        assign negatedy = (ny == 1) ? (~sign_extendedy):
                                        (sign_extendedy);


        assign incrementedy = (iy == 1) ? (negatedy + 1):
                                            (negatedy);


        logical_operator sub_inst1(
            .A(incrementedx),
            .B(incrementedy),
            .operation(opcode),
            .Result(logical_out),
            .ZeroFlag(zero_logic)
            );
        shift sub_inst2(
            .A(incrementedx),
            .B(incrementedy),
            .operation(opcode),
            .Result(shift_out),
            .ZeroFlag(zero_shift)
            );
        comparator sub_inst3(
            .A(incrementedx),
            .B(incrementedy),
            .operation(opcode),
            .a_sign(x_sign),
            .b_sign(y_sign),
            .Result(comparator_out),
            .ZeroFlag(zero_comparator)
            );

        prefixAdder sub_inst4(
            .a(incrementedx),
            .b(incrementedy),
            .cin(1'b0),
            .a_sign(x_sign),
            .b_sign(y_sign),
            .opcode(opcode),
            .Result(prefix_out),
            .carry_out(carry_out),
            .overflow(overflow),
            .negative(negative),
            .ZeroFlag(zero_prefix)
            );

    always @(*) begin
        if (opcode == 0 || opcode == 1) begin
            out = prefix_out;
        end
        else if (opcode >= 2 && opcode <= 4) begin
            out = shift_out;
        end
        else if (opcode >= 5 && opcode <= 10) begin
            out = comparator_out;
        end
        else if (opcode >= 11 && opcode <= 13) begin
            out = logical_out;
        end
    end

endmodule
