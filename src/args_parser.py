"""Parses arguments for when running program as a module."""

import argparse
import os


def args_parser():
    """Parses arguments for running program as a module."""

    argsParser = argparse.ArgumentParser(
        description='Parse through your emails and collect a list of \
            unsubscribe links and output them into a CSV, XLSX (Excel) or JSON'
    )
    email = argsParser.add_mutually_exclusive_group()
    email.add_argument(
        '-e',
        '--email',
        action='store',
        help='Email address',
    )
    email.add_argument(
        '-c',
        '--email-env',
        action='store',
        help='Name of environment variable containing the email address'
    )
    email.add_argument(
        '-d',
        '--email-file',
        action='store',
        help='Path to file containing email address.'
    )

    password = argsParser.add_mutually_exclusive_group()
    password.add_argument(
        '-p',
        '--password-env',
        action='store',
        help='Name of environment variable containing password.'
    )
    password.add_argument(
        '-f',
        '--password-file',
        action='store',
        help='Path to file containing password.'
    )
    argsParser.add_argument(
        '-t',
        '--filetype',
        action='store',
        choices=['csv', 'xlsx', 'json'],
        help='Output file type.'
    )
    argsParser.add_argument(
        '-o',
        '--output-directory',
        action='store',
        help='Directory of where the file should be stored.'
    )
    argsParser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help="Output full error messages."
    )

    return argsParser.parse_args()
