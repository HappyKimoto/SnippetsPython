def double_num(x: int) -> int:
    result = x + x
    return result

def main():
    x = 5
    y = double_num(x)
    # breakpoint()
    x = 8
    y = double_num(x)
    # breakpoint()
    print(x, y)


if __name__ == '__main__':
    main()
