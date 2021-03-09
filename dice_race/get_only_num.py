def get_only_num(s):
    print()
    p = False
    u = 0
    while True :
        u = input(s)
        try :
            u = int(u)
            p = True
            break
        except :
            print("다시 입력해주세요.")
            continue
    if p :
        return u