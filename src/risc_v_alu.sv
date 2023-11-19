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
                  output logic [31:0] out);

    logic [31:0] negatedx, incrementedx, sign_extendedx;
    logic [31:0] negatedy, incrementedy, sign_extendedy;
    logic carry_in, a_sign, b_sign;
    logic carry_out, overflow, negative, zero;


    always @(*) begin
        if (nx == 1) begin
            negatedx = ~x;
        end else begin
            negatedx = x;
        end

        if (ix == 1) begin
            incrementedx = negatedx + 1;
        end else begin
            incrementedx = negatedx;
        end

        if (sx == 1) begin
            sign_extendedx = { {30{incrementedx[11]}}, incrementedx[11:0] };
        end else begin
            sign_extendedx = negatedx;
        end
    end

endmodule
