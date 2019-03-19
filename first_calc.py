def containsNull(p):
    return "." in p

def reachNull(symbol,grammar):
    for production in grammar[symbol]:
        if production  == '.':
            return True
    return False

def isNonTerminal(s):
    return ord(s)>=65 and ord(s)<=90

def getFirst(left,productions,d,first,first_set):
    l = []
    for i in productions:
        if isNonTerminal(i[0]):
            if i[0] in first_set:
                l += first[i[0]]
            else:
                l += getFirst(i[0],d[i[0]],d,first,first_set)
                first_set.add(i[0])
        else:
            l.append(i[0])
    return l


def main():
    n = int(input('Enter Number Of Productions'))
    productions = []
    for _ in range(n):
        productions.append(input('Enter Production'+str(_+1)))
    d = dict()
    for i in productions:
        left,right = i.split("=")
        right = right.split('|')
        d[left] = right
    print(d)

    first = dict()
    first_set = set()
    
    for i in d:
        first[i] = set(getFirst(i,d[i],d,first,first_set))
        first_set.add(i)

    print(first)    

if __name__ == "__main__":
    main()