import v_circuit_builder/boolfunc as bf

def test_class_BooleanFunction() -> bool:
    # TODO: implement this test
    return False

def test_convert_to_boolean_function1() -> bool:
    user_string = "F = AB\' + A\'B" # standard form

    result = bf.convert_to_boolean_function(user_string)

    if result.outputs != ['F']: return False
    if result.inputs != ['A','B']: return False
    if result._rpn != ["or","and","and","A","!B","!A","B"]:
        return False
    
    return True
