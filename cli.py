# csdfs/cli.py

import argparse
from scripts.csdfs_up import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")

    args = parser.parse_args()

    if args.command == "up":
        run()

if __name__ == "__main__":
    main()
