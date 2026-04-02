def reverse_in( x):
        rev = 0
        i = abs(x)
        while i :
            rev = i%10 +rev *10
            i //=10

        if x<0:
            return rev*(-1)

        return rev

print(reverse_in(1534236469))


def reverse( x):
        rev = int(str(abs(x))[::-1])
        if x<0:
            rev = -rev

        if -2 ** 31 > rev or rev > 2 ** 31- 1:
            return 0

        return rev