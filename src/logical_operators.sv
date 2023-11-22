`ifndef LOGICAL
`define LOGICAL
module logical_operator (
  input logic [31:0] A,
  input logic [31:0] B,
  input logic [3:0] operation,
  output logic [31:0] Result,
  output logic ZeroFlag
);

  always @(*) begin
    case (operation)
      4'b1011: // bitwise AND
        Result = A & B;
      4'b1100: // bitwise OR 
        Result = A | B;
      4'b1101: // Bitwise XOR
        Result = A ^ B;
      default:
        Result = 32'b0; // Default operation
    endcase
  end

  assign ZeroFlag = (Result == 32'b0);

endmodule
`endif