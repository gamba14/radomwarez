'''
    A "empty stack like automata" to determine whether an
    string is accepted or not a
'''
'''
inputs:
            {[()]} SI
            {[(])} NO
            {{[[(())]]}} SI
'''
import signal
import sys
def signal_handler(signal, frame):
        print('\nYou pressed Ctrl+C!')
        sys.exit(0)

def itsBalanced(string):

    braces=[]
    brackets_open = '{(['
    opposites = {')':'(',']':'[','}':'{'}

    for char in string:
        if char in brackets_open:
            braces.append(char)
            print('Added {}'.format(char))
        else:
            try:
                if opposites[char] == braces[len(braces)-1]:
                    braces.pop()
                    print('Poped {}'.format(opposites[char]))
            except:
                return False

    if len(braces) == 0:
        return True
    else:
        return False

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print('Exit with Ctrl+C')
    while True:
        result = itsBalanced(raw_input('Check for string-> '))
        if result:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
