# Import test function from original script to here 

from eva_data_analysis import text_to_duration

# Test function 
def test_text_to_duration_integer(): 
    # initalise 
    input_value = "10:00"
    test_result = text_to_duration(input_value) == 10
    print(f"text_to_duration('10:00') == 10? {test_result}") 


# Test function 
def test_text_to_duration_integer_assert_function(): 
    # initalise 
    input_value = "10:00"
    # Assert that the output of the test is True
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float_irrational():
    input_value = "10:20"
    assert abs(text_to_duration(input_value) - 10.3333) < 1e-3

def test_text_to_duration_float():
    input_value = "10:15"
    assert text_to_duration(input_value) == 10.25

test_text_to_duration_integer_assert_function()
test_text_to_duration_float()