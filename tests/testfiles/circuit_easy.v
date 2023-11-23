// implementation of AB'

module circuit_easy (A,B,F);
    // inputs
    input A;
    input B;

    // outputs
    output F;

    // components
    and(F,A,!B);

endmodule
