def check(symbol,production,grammar):
    if containsNull(production):
        return True
    else:
        if not isNonTerminal(production[0]):
            if symbol == production[0]:
                return True
            else:
                return False
        else:
            for p in grammar[production[0]]:
                if check(symbol,p,grammar):
                    return True
            return False

def containsNull(p):
    return "." in p

def reachNull(symbol,grammar):
    for production in grammar[symbol]:
        if production  == '.':
            return True
    return False

def parse(string,grammar):
    left = ['S']
    loopcount = 0
    againError = False
    i = 0
    try:
        while len(left)>0:
            if i == len(string):
                raise Exception
            loopcount+=1
            symbol = left.pop()
            if containsNull(symbol):
                continue
            if isNonTerminal(symbol):
                for production in grammar[symbol]:
                    if check(string[i],production,grammar):
                        left += production[::-1]
                        break
                else:
                    againError = True
                    raise Exception
            else:
                if symbol!=string[i]:
                    againError  = True
                    raise Exception
                else:
                    i+=1
    except:
        while len(left)>0 and  reachNull(left[-1],grammar):
            left.pop()
        if i==len(string) and len(left)==0:
            return True
        else:
            return False
    finally:
        return len(left)==0 and i>=len(string) and againError==False

def isNonTerminal(s):
    return ord(s)>=65 and ord(s)<=90

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
    print('Enter Number Of Strings')
    for _ in range(int(input())):
        string = input("Enter the string")
        try:
            if parse(string,d):
                print('Accepted')
            else:
                print('Not Accepted')
        except:
            print('Not Accepted')

if __name__ == "__main__":
    main()