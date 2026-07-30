def main(n: int):
    res = 0
    for i in range(n + 1):
        res = res + i  
    return f"Result: {res}"

print(
    main(2)
)

print(
    main(3)
)

print(
    main(4)
)
