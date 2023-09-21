# Author: Kinzo

# gets variables from a passed function in the form F([variables]) = sum([terms])
def getVariables(function: str) -> list[str]:
    v_list = []
    # TODO: implement checks for variables
    for v in function:
        v_list.append(v)

    return v_list

# gets term subscripts from a passed function who's terms are in a list (see above function form)
def getTermSubscripts(function: str) -> list[int]:
    term_subs = []
    # TODO: implement checks for terms & subscripts
    for t in function:
        term_subs.append(int(t))

    return term_subs

# returns binary representaion of intergers passed from num_list
def getBinaryList(num_list: list[int], bits: int) -> list[str]:
    binary_list = []

    curr_binary_num = ""
    for n in num_list:
        # ignore "0b"
        curr_binary_num = bin(n)[2::]
        # preppend the appropriate # of '0's given bits
        binary_list.append('0'*(bits - len(curr_binary_num)) + curr_binary_num)


    return binary_list

# returns the appropriate minterm given a list of variables and the term subscript in binary
def getMinterm(var_list: list[str], binary_subscript: str) -> str:
    minterm = ""

    r_binary_num = binary_subscript[::-1]
    end_of_binary_num = False
    for i in range(len(var_list)):
        # ingore all characters after the 'b' in binary number string
        if not end_of_binary_num and r_binary_num[i] == 'b':
            end_of_binary_num = True
        # apppend appropriate true or complimented term
        if not end_of_binary_num and r_binary_num[i] == '1':
            minterm += var_list[i]
        else:
            minterm += var_list[i] + '\''

    return minterm

# returns the standard representation of a sum of products function given its variables and minterm subscripts
def getStandardRepresentation(var_list: list[str], subscript_list: list[int]) -> str:
    variable_count = len(var_list)
    function = "F("

    # append variables
    for i in range(variable_count):
        function += var_list[i]
        # close parentheses
        if i == variable_count-1:
            function += ')'
        else:
            function += ','

    # append '='
    function += " = "

    # append terms
    binary_list = getBinaryList(subscript_list, variable_count)
    for i in range(len(subscript_list)):
        function += getMinterm(var_list, binary_list[i])

        if i != len(subscript_list)-1:
            function += ' + '

    return function

# returns the number of 1's in a binary number
def getOnes(num: str) -> int:
    count = 0
    for i in num:
        if i == '1':
            count += 1

    return count

# returns whether two boolean numbers can be groups (differ by 1 bit)
def compare(x: str, y: str) -> bool:
    differences = 0
    for i in range(len(x)):
        # handle cases where '-' is not in the same place
        if x[i] == '-' and y[i] != '-':
            return False
        if x[i] != '-' and y[i] == '-':
            return False

        if x[i] != y[i]:
            differences += 1

    return differences == 1

# groups binary numbers together
def reduce(x: str, y: str) -> str:
    result = ""
    for i in range(len(x)):
        if x[i] == y[i]:
            result += x[i]
        else:
            result += '-'

    return result

# returns an inital group table given a list of variables (bit cout) and minterm subscripts
def getInitialGroupTable(var_list: list[str], subscript_list: list[int]) -> dict:
    groups = {}
    minterms = getBinaryList(subscript_list, len(var_list))

    for term in minterms:
        ones_count = getOnes(term)
        
        # place term in appropriate group
        if ones_count in groups.keys():
            groups[ones_count].append(term)
        else:
            groups[ones_count] = [term]

    return groups

# attempts to reduces a table once, returns the reduced group and the number of terms reduced
def reduceGroupTable(initial_group_table: dict):
    new_group_table = {}

    # create a list of all minterms
    minterms = []
    for group in initial_group_table.values():
        for term in group:
            minterms.append(term)

    changes = 0 # keeps track of number of terms reduced
    for i in range(len(minterms)-1):
        curr_term = minterms[i]

        for j in range(i, len(minterms)): # we only need to check "higher" minterms
            next_term = minterms[j]

            # check if curr_term and next_term differ by 1 bit
            if compare(curr_term, next_term):
                changes += 1
                new_term = reduce(curr_term, next_term) # place proper '-'s
                new_term_ones = getOnes(new_term) 

                # place in proper grouping
                if new_term_ones in new_group_table.keys():
                    new_group_table[new_term_ones].append(new_term)
                else:
                    new_group_table[new_term_ones] = [new_term]
    
    if changes == 0:
        new_group_table = initial_group_table

    return new_group_table, changes


def getGroupTable(var_list: list[str], subscript_list: list[int]) -> dict:
    group_table = getInitialGroupTable(var_list, subscript_list)
    changes = -1

    while changes != 0:
        group_table, changes = reduceGroupTable(group_table)

    # TODO: Ensure that there are no repeated terms
    return group_table
