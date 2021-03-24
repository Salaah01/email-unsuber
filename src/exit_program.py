"""Prompts user to press any key to exit which will terminate the program."""

import platform
import sys



class ExitProgram:
    """Prompts user to press any key to exit which will terminate the program.
    """
    def __init__(self):
        getattr(self, f'_{platform.system().lower()}')()

    @staticmethod
    def _linux():
        """Linux specific exit script."""
        import termios
        import tty
        stdinFileDesc = sys.stdin.fileno()
        oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc)
        print('Press any key to exit...')
        tty.setraw(stdinFileDesc)
        sys.stdin.read(1)
        termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr)
        sys.exit()

    @staticmethod
    def _windows():
        import msvcrt
        print('Press any key to exit...')
        while True:
            if msvcrt.kbhit():
                sys.exit()
