"""
Test goes here

"""
from main import power

def test_power():
    '''
    Test function for basic multiplication.
    '''
    
    power_10 = power(10)
    assert power_10(2) == 100

    power_5 = power(5)
    assert power_5(2) = 32

    power_negative_1 = power(-1)
    assert power_negative_1(2) == 0.5