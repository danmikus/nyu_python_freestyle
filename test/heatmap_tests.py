import sys
import os

sys.path.append(os.path.join('..', 'heatlib'))
from heat import *

def test_check_date_format_1():
    cf_1 = check_date_format("2017-08-06")
    assert cf_1 == True

def test_check_date_format_2():
    cf_2 = check_date_format("2017/08/06")
    assert cf_2 == "ERROR: Make sure you use '-' to partition date"

def test_check_date_format_3():
    cf_3 = check_date_format("08-06-2016")
    assert cf_3 == "ERROR: Make sure the year is formatted correctly"

def test_check_date_format_4():
    cf_4 = check_date_format("207-08-06")
    assert cf_4 == "ERROR: Make sure the year is formatted correctly"

def test_check_date_format_5():
    cf_5 = check_date_format("201ds7-08-06")
    assert cf_5 == "ERROR: Please only enter numbers"

def test_check_date_format_6():
    cf_6 = check_date_format("2017-13-06")
    assert cf_6 == "ERROR: Make sure the month is formatted correctly"

def test_check_date_format_7():
    cf_7 = check_date_format("2017-8-06")
    assert cf_7 == "ERROR: Make sure the month is formatted correctly"

def test_check_date_format_8():
    cf_8 = check_date_format("2017-08-06d")
    assert cf_8 == "ERROR: Please only enter numbers"

def test_check_date_format_9():
    cf_9 = check_date_format("2017-08-32")
    assert cf_9 == "ERROR: Make sure the day is formatted correctly"

def test_format_time_10():
    ft_10 = format_time("2017-08-06")
    assert ft_10 == {"beginning" : "2017-08-06T00:00:00", "end" : "2017-08-06T23:59:59"}

def test_get_city_data_11():
    cd_11 = get_city_data("2017-08-06T00:00:00", "2017-08-06T23:59:59")
    assert len(cd_11) > 5
