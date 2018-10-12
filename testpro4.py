def increment(a):
    print(a,'in func')
    print(id(a))
    a=a+1
    print(id(a))
    print(a,'in func')

def main():
    a=10
    print(a,'in main')
    print(id(a))
    increment(a)
    print(a,'in main')
    print(id(a))
if __name__ == '__main__':
    main()