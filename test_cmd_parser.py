import unittest
from cmd_parser import exec_cmd


class TestSuit(unittest.TestCase):
    def setUp(self):
        pass

    def test_int(self):
        s = 'add 2 3'
        self.assertEqual(exec_cmd(s), 5)


def test_extra_parameters():
    """a nose testcase"""
    s = 'add 2 3 4'
    # print(exec(s))
    assert exec_cmd(s) == "add() takes 2 positional arguments but 3 were given"


def test_unknown_command():
    """a nose testcase"""
    s = 'mult 2 3'
    # print(exec(s))
    assert exec_cmd(s) == "Unknown command"


def test_sub():
    """a nose testcase"""
    s = 'sub 2 3'
    # print(exec(s))
    assert exec_cmd(s) == -1


def test_str_parameters():
    """a nose testcase"""
    s = 'add 2a 3b'
    # print(exec(s))
    assert exec_cmd(s) == "invalid literal for int() with base 10: '2a'"


def test_error_value_type():
    s = 'add 2.3 2.5'
    # print(exec_cmd(s))
    assert (exec_cmd(s) == "invalid literal for int() with base 10: '2.3'")


def test_error_value_type2():
    s = 'sub a 2.5'
    # print(exec_cmd(s))
    assert (exec_cmd(s) == "Invalid parameter(s)")


def test_default_param():
    """a nose testcase"""
    s = 'sub 2'
    # print(exec(s))
    assert exec_cmd(s) == 2


def test_kwargs():
    """a nose testcase"""
    s = 'sub y=2 x=3'
    # print(exec(s))
    assert exec_cmd(s) == 1


if __name__ == '__main__':
    unittest.main()