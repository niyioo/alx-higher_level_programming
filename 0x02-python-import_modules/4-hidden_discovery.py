#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]
    module_names.sort()

    for name in module_names:
        print(name)
