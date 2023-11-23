# circuit and test bench builder
from lib import boolfunc as bf

# implementation discription
def write_description(func: str):
    return("// implementatoin of" + func + "\n")


# inputs
def write_inputs(ins: list):
    string = "// inputs\n"

    for var in ins:
        string += "input" + var + ";\n"

    return string


# outputs
def write_outputs(outs: list):
    string = "// ouputs\n"

    for var in outs:
        string += "output" + var + "\n"

    return string


# components
def write_components():
    pass


# build circuit
def build_circuit(file_name: str,
                  bool_func: bf.BooleanFunction):
    # TODO: use BooleanFunction's fields to populate file

    # concatenate inputs and outputs into one string
    ins_outs = ""
    for var in bool_func.inputs:
        ins_outs += var + ","
    for var in bool_func.outputs:
        ins_outs += var + ","

    with open(file_name, 'w') as file:
        # begin module
        file.write("module" + file_name + "(" + ins_outs + ")\n")
        # inputs
        file.write(write_inputs(bool_func.inputs))
        # outputs
        file.write(write_outputs(bool_func.outputs))
