#!/usr/bin/env python3

from typing import Optional


def main(argv: Optional[list[str]] = None) -> int:
    """Main function.

    Parameters
    ----------
    argv : list or str, or None, default = None
        Arguments passed to 'argparse' or downstream functions.

    Returns
    -------
    int
        Exit status (zero is success).
    """

    print("Hello there!")

    return 0
