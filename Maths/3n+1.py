def main():
    def n22(a):# a = initial number
        c = 0
        l = [a]
        while a != 1:
            if a % 2 == 0:#if even divide it by 2
                a = a // 2
            elif a % 2 == 1:#if odd 3n+1
                a = 3*a +1
            c += 1#counter
            l += [a]

        return l , c
    print(n22(34))
    print(n22(96)[0][-1])# = a
    print("It took {0} steps.".format(n22(13)[1]))#optional finish

if __name__ == '__main__':
    main()
