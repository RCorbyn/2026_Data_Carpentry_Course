# Import test function from original script to here 

from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size
import pytest


#########
## Older test functions
#########

# # Test function 
# def test_text_to_duration_integer(): 
#     '''
#         Test that text_to_duration returns an expected ground truth 
#         value for exact hour inputs.  
#     '''
#     # initalise 
#     input_value = "10:00"
#     test_result = text_to_duration(input_value) == 10
#     print(f"text_to_duration('10:00') == 10? {test_result}") 

# def test_text_to_duration_float_irrational():
#     '''
#      Test that text_to_duration returns the expected ground truth values
#         for typical durations with a non-zero minute component. 
#     We are testing the output value is within a tolerance of the expected output
#     '''
#     input_value = "10:20"
#     # As the result will be an irrational number, we will check that the 
#     # results are within a tollerance of the expected value
#     assert abs(text_to_duration(input_value) - 10.3333) < 1e-3

# def test_text_to_duration_float():
#     '''
#     Test that text_to_duration returns an expected ground truth 
#     values with a non-zero minute component, using the assert function 
#     '''
#     input_value = "10:15"
#     assert text_to_duration(input_value) == 10.25

###################
## Functional tests
##################

# Test function 
def test_text_to_duration_integer_assert_function(): 
    '''
        Test that text_to_duration returns an expected ground truth 
        value for exact hour inputs, using the assert function
    '''
    # initalise 
    input_value = "10:00"
    # Assert that the output of the test is True
    assert text_to_duration(input_value) == 10

def test_text_to_duration_float_irrational_approx():
    '''
        Test that text_to_duration returns the expected ground truth values
        for typical durations with a non-zero minute component
    '''
    input_value = "10:20"
    # As the result will be an irrational number, we will check that the 
    # results are within a tollerance of the expected value
    assert text_to_duration(input_value) == pytest.approx(10.333333) 

############
## Multiple tests for the calculate_crew_size function
############

# def test_calculate_crew_size_singular(): 
#     '''
#         Test the calculate_crew_size function deals with string inputs for one entry
#     '''
#     input_value = "Ryan Apps;"
#     assert calculate_crew_size(input_value) == 1

# def test_calculate_crew_size_multiple(): 
#     '''
#         Test the calculate_crew_size function deals with string inputs for multiple entries
#     '''
#     input_value = "Ryan Apps; Jordan Delaney; Jack Stevens; Daisy Havers; Sara Stones;"
#     assert calculate_crew_size(input_value) == 5

# def test_calculate_crew_size_hyphonated_names(): 
#     '''
#         Test the calculate_crew_size function deals with string inputs for double-barrel 
#         and hyphonated names
#     '''
#     input_value = "Ryan Apps-Delaney; Jack Stevens Havers; Sara Stones;"
#     assert calculate_crew_size(input_value) == 3

# def  test_calculate_crew_size_null():
#     '''
#         Test the calculate_crew_size function deals with string inputs for no input
#     '''
#     input_value = ""
#     assert calculate_crew_size(input_value) == None

####################
## Parameterising the test code to run multiple tests with multiple inputs and 
## outputs without the need to re-write the function. 
####################

# A Decorator for the next function in the program. 
## This decorator is ONLY applied to the function directly 
## under the decorator, and not everywhere else. 
@pytest.mark.parametrize("input_value, expected_result",[
    ("Jordan Delaney;", 1),
    ("Marc Beck; Andrew Collins; Sophie Turner;", 3),
    ("", None) 
    ] )

def test_calculate_crew_size_parameterisation(input_value, expected_result):
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result



