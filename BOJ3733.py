while True:
    try:
        p, s = map(int, input().split())
    except EOFError :
        break
    else:
        print(s // (p + 1))