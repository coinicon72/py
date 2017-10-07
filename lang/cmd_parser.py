"""
a command line parser

use regex to find all legal opts
all opts separated by space

supported opt:
cmd x y       # position opts
cmd 'x y'     # ??
cmd x=y a=b   # keyword opts,
cmd x='y z'   # keyword opt with quote

position opts should place before keyword opts
"""
import re

cmds = {}


def cmd(func):
    """decorator to expose(register) any command"""
    func_name = func.__name__
    if func_name in cmds.keys():
        raise ValueError("Command already exist.")

    def wrapper(*args, **kwargs):
        try:
            r = func(*args, **kwargs)
        except Exception as e:
            return str(e)
        else:
            return r

    cmds[func_name] = wrapper

    return wrapper


@cmd
def add(x, y):
    """x, y should be int"""
    x = int(x)
    y = int(y)

    return x + y


@cmd
def sub(x, y=0):
    """x, y should be numeric"""
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return "Invalid parameter(s)"

    return x - y


def _exec(str, *args, **kwargs):
    c = cmds.get(str)
    if c is None:
        return "Unknown command"
    else:
        return c(*args, **kwargs)


def _parse_args(p):
    """
    generator to extra arg from regex-result of the command line
    arg only can be before any kwarg
    """
    for i in p:
        if len(i[0]) > 0:
            return  # encounter kwarg
        else:
            yield i[2]


def exec_cmd(str):
    # c = str.split()
    # p = re.findall("(((?:')\w+(?:')|\w+?)=('.+?'|[^' ]+))", str)
    p = re.findall("(\w+?)=('.+?'|[^' ]+)|([^ ]+)", str)
    args = [x for x in _parse_args(p)]
    c = args[0]
    args = args[1:]
    kws = {x[0]: x[1].replace("'", "") for x in p if len(x[0]) > 0}
    return _exec(c, *args, **kws)
