def a(num):
    bb = 0
    print('this is num : %s' % num)
    def b(ber):
        print('this is ber : %s' % ber)
        return ber
    return b

getattr(a,'__doc__')