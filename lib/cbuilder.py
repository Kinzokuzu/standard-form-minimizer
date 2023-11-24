# circuit and test bench builder
from lib import boolfunc as bf

# implementation discription
def write_description(func: str):
    return("// implementation of " + func + "\n")


# inputs
def write_inputs(ins: list):
    string = "\t// inputs\n"

    for var in ins:
        string += "\tinput " + var + ";\n"

    return string


# outputs
def write_outputs(outs: list):
    string = "\t// outputs\n"

    for var in outs:
        string += "\toutput " + var + ";\n"

    return string


# components
def get_component(gate: str, out: str, ins: list):
    if len(ins) != 2:
        print("ERROR: invalid input list:", ins)
        return 1
    
    return gate + " (" + out + ", " + ins[0] + ", " + ins[1] + ")"


def write_components(rpn: list):
    # flip reverse polish notation so we can access it as
    # a binary tree
    b_tree = rpn[::-1]

    #TODO: implement creation of multiple base components


# build circuit
def build_circuit(file_name: str,
                  bool_func: bf.BooleanFunction):
    # TODO: use BooleanFunction's fields to populate file

    # concatenate inputs and outputs into one string
    ins_outs = ""
    for var in bool_func.inputs:
        ins_outs += var + ","
    for var in bool_func.outputs:
        ins_outs += var

        if var != bool_func.outputs[-1]:
            ins_outs += ','

    with open(file_name + ".v", 'w') as file:
        # basic description
        file.write(write_description(bool_func.user_function))
        # begin module
        file.write("module " + file_name + "(" + ins_outs + ");\n")
        # inputs
        file.write(write_inputs(bool_func.inputs))
        # outputs
        file.write(write_outputs(bool_func.outputs))
        # end module
        file.write("endmodule // " + file_name + '\n')
