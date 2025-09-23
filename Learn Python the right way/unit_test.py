# import package
import sys

def test(did_pass):
    """ Print result of test """
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED".format(line_num)
    print(msg)  

def test_suite():
    test(abs(17)==17)
    test(abs(-17)==17)
    test(abs(0)==0)
    test(abs(3.14)==3.14)
    test(abs(-3.14)==3.14)

test_suite()