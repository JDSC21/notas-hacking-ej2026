#!/usr/bin/env python3

from typing import Dict


def derive_password() -> str:
    positions: Dict[int, str] = {
        0: "d",
        1: "3",
        2: "5",
        3: "c",
        4: "r",
        5: "4",
        6: "m",
        7: "b",
        8: "l",
        9: "3",
        10: "_",
        11: "t",
        12: "H",
        13: "3",
        14: "_",
        15: "c",
        16: "H",
        17: "4",
        18: "r",
        19: "4",
        20: "c",
        21: "T",
        22: "3",
        23: "r",
        24: "5",
        25: "_",
        26: "a",
        27: "4",
        28: "d",
        29: "7",
        30: "3",
        31: "6",
    }

    return "".join(positions[i] for i in range(32))


def main() -> None:
    password = derive_password()
    print(password)
    print(f"picoCTF{{{password}}}")


if __name__ == "__main__":
    main()
