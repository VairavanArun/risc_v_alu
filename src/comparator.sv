`ifndef COMPARATOR
`define COMPARATOR

`include "../src/prefix_adder.sv"

module comparator (
  input logic [31:0] A,
  input logic [31:0] B,
  input logic [3:0] comparison,
  input logic a_sign, b_sign,
  output logic [31:0] Result,
  output logic ZeroFlag
);

  logic [31:0] difference_a_b;
  logic cin, sub;
  logic carry_out, overflow, negative, zero;

  assign cin = 0;
  assign sub = 1;

  // get the value of A-B
  prefixAdder adder(A, B, cin, a_sign, b_sign, sub, difference_a_b,
                     carry_out, overflow, negative, zero);
  
  always @(*) begin
    case (comparison)
      4'b0100: // Signed Less Than (SLT/BLT)
        Result = (negative ^ overflow) ? 32'b1 : 32'b0;
      4'b0101: // Signed greater Than (BGT) 
        Result = ((~zero) & (~(negative ^ overflow))) ? 32'b1 : 32'b0;
      4'b0110: // Unsigned Less Than (SLTU/BLTU)
        Result = (~carry_out) ? 32'b1 : 32'b0;
      4'b0111: // Unsigned greater than (BGTU)
        Result = ((~zero) & carry_out) ? 32'b1 : 32'b0;
      4'b1000: // Equal to (BEQ)
        Result = (zero) ? 32'b1 : 32'b0;
      4'b1001: // Not equal to (BNE)
        Result = (~zero) ? 32'b1 : 32'b0;
      default:
        Result = 32'b0; // Default operation
    endcase
  end

  assign ZeroFlag = (Result == 32'b0);

endmodule

`endif