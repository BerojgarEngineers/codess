# test_app.py

import mathlib

def main():
    print("Testing mathlib module")

    a = 12
    b = 4

    print(f"{a} + {b} = {mathlib.add(a, b)}")
    print(f"{a} − {b} = {mathlib.subtract(a, b)}")
    print(f"{a} × {b} = {mathlib.multiply(a, b)}")
    print(f"{a} ÷ {b} = {mathlib.divide(a, b)}")

    # test divide by zero
    try:
        print("Testing divide by zero")
        mathlib.divide(a, 0)
    except Exception as e:
        print("Caught exception as expected:", e)

if __name__ == "__main__":
    main()
