def normal(x1x2):
    return (x1x2[0]**2 + x1x2[1]**2)**(1/2)


def gradient(x1x2):
    return [20*(5*x1x2[0]-x1x2[1])**3 + 2*(x1x2[0]-2) + 1, -4*(5*x1x2[0] - x1x2[1])**3 - 2]


def neg_gradient(x1x2):
    return [-1*(20*(5*x1x2[0] - x1x2[1])**3 + 2*(x1x2[0] - 2) + 1), -1*(-4*(5*x1x2[0] - x1x2[1])**3 - 2)]


def func(x1x2):
    return (5*x1x2[0]-x1x2[1])**4 + (x1x2[0] - 2)**2 + x1x2[0] - 2*x1x2[1] + 12


def bisection(x1x2, a, b, eps, d):
    x1 = x1x2[0]
    x2 = x1x2[1]
    d1 = d[0]
    d2 = d[1]

    while b-a>=eps:
        x = (a+b)/2
        new_x1 = x1 + x*d1
        new_x2 = x2 + x*d2
        new_x1x2 = [new_x1, new_x2]
        new_x1x2_eps = [new_x1 + eps, new_x2 + eps]

        if func(new_x1x2_eps) <= func(new_x1x2):
            a=x
        else:
            b=x

    return x


def steepest_descent(eps):
    k = 0
    x1x2 = [6.35,33.01]
    while normal(gradient(x1x2)) >= eps:
        d = neg_gradient(x1x2)
        alpha = bisection(x1x2, -5, 12, eps**2, d)
        x1x2_new = [x1x2[0] + alpha*d[0], x1x2[1] + alpha*d[1]]
        x1x2 = x1x2_new
        k = k+1
        print("x(k): ", x1x2)
        print("f(x(k)): ", func(x1x2))
        print("iteration k: ", k)

    print("normal of gradient: ", normal(gradient(x1x2)))
    print("normal is smaller than epsilon")

    return x1x2


if __name__ == '__main__':
    result = steepest_descent(0.00001)
    print("result: ", result)
    print("value of the resulting point in function f: ", func(result))
