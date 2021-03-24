"""Prompts user to press any key to exit which will terminate the program."""

import sys
import termios
import tty


def exit_program():
    """Prompts user to press any key to exit which will terminate the program.
    """
    stdinFileDesc = sys.stdin.fileno()
    oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc)
    print('Press any key to exit...')
    tty.setraw(stdinFileDesc)
    sys.stdin.read(1)
    termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr)
    sys.exit()
