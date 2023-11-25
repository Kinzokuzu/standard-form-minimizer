// https://saiankit.medium.com/how-to-simulate-verilog-models-on-macos-5a6f821b2c4f

`timescale 1ns / 1ns
// import the main code into the testbench
`include "sample.v"

module sample_tb;

// inputs as registers
reg A;
reg B;
reg C;

// outputs as wires
wire D;
wire E;

sample uut(A,B,C,D,E);

initial begin
    // name of the graph file that gets generated after we run
    $dumpfile("sample_tb.vcd");
    $dumpvars(0,sample_tb);

    A = 0;
    B = 0;
    C = 0;
    #10

    A = 0;
    B = 0;
    C = 1;
    #10

    A = 0;
    B = 1;
    C = 0;
    #10

    A = 0;
    B = 1;
    C = 1;
    #10

    $display("Test complete");
end

endmodule
