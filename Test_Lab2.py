import Lab2
def test_find_min_max():
    input_arr = [1,2,3,4,5,6,7]
    ans = (1, 7)
    assert(Lab2.calc_min_max_temperature(input_arr) == ans)

def test_calc_average():
    input_arr = [1,2,3,4,5,6,7]
    ans = 4
    assert(Lab2.calc_average_temperature(input_arr) == ans)

def test_calc_median_temperature():
    input_arr = [3,5,1,4,7,3,5,4,9]
    ans = 4
    assert(Lab2.calc_median_temperature(input_arr) == ans)
