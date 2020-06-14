
def avg(lx, ly):
    return (lx+ly)//2

def KMultip(x, y):
    n = avg(len(str(x)),len(str(y)))

    if(n <= 1):
        return x*y

    exp = 10 ** (n // 2)

    a = x // exp
    b = x % exp
    c = y // exp
    d = y % exp

    ac = KMultip(a,c)
    bd = KMultip(b,d)
    ad_bc = KMultip(a+b, c+d) - ac - bd

    return ac*(exp**2) + ad_bc*exp + bd



if __name__ == '__main__':
    x = int(input())
    y = int(input())

    print(KMultip(x,y))