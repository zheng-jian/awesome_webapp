def a(app):
    print(app)
    def b(re):
        print(re)
    return b

ss = a('hehe')
ss('haha')
