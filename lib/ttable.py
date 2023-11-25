# truth table implementation
def print_table(table):
    for row in table:
        print(" ".join(map(str, row)))


def generate_table(inputs, outputs, minterms=[]):
    # generate table header
    header = []
    for element in inputs:
        header.append(element)

    header.append('|')
    
    for element in outputs:
        header.append(element)

    # number of needed columns is given by len(header)
    # number of needed rows (minus header) is given by 2**len(inputs)

    table = [header]

    for i in range(2**len(inputs)):
        # use built-in bin() to generate input states
        base_state = bin(i)[2::]
        # give our state the correct number of bits
        state = '0'*(len(inputs) - len(base_state)) + base_state + '|0' 
        # turn our state into an array and append to table 
        table.append( [char for char in state] )

    # TODO: implement outputs
    if minterms:
        pass

    return table
