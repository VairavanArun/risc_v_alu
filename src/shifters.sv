`ifndef  SHIFTERS
`define SHIFTERS
module shift (
  input logic [31:0] A,
  input logic [31:0] B,
  input logic [3:0] operation,
  output logic [31:0] Result,
  output logic ZeroFlag
);

  always @(*) begin
    case (operation)
      4'b0001: // Logical left shift
        Result = A << B;
      4'b0010: // Logical right shift 
        Result = A >> B;
      4'b011: // Arithmetic right shift
        Result = A >>> B;
      default:
        Result = 32'b0; // Default operation
    endcase
  end

  assign ZeroFlag = (Result == 32'b0);

endmodule
`endif
