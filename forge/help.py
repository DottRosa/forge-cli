"""This file is responsible for the help section of the CLI"""

import argparse

# https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Forge
LOGO = r"""
███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                     
"""


class HelpParser(argparse.ArgumentParser):
    """Custom help function for the parser"""

    def print_help(self, file=None):
        print("\033[91m")
        print(LOGO)
        print("\033[0m ")
        super().print_help()
