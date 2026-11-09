"""my-project 入口脚本。

保持最小：一个可被 import 的函数 + 一个命令行入口。
"""

from __future__ import annotations

import argparse


def greet(name: str) -> str:
    """返回一句问候语。"""
    name = name.strip() or "world"
    return f"Hello, {name}!"


def main() -> int:
    parser = argparse.ArgumentParser(description="my-project 命令行入口")
    parser.add_argument(
        "-n",
        "--name",
        default="world",
        help="要问候的名字，默认为 world",
    )
    args = parser.parse_args()

    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
