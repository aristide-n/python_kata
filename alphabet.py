__author__ = 'Aristide'

keymap = [None,"vtfrq","ftk","wzbg","rs",None,"fir","p","lo","p"]

def main():
    num = raw_input("Enter a Number: " )
    combinations ("", num)

def combinations(prefix, num):
    if (len(num) is 0):
        print prefix
    else:
        digit = int(num[0] + '')
        key_letters = keymap[digit]

        if key_letters is not None:
            for l in key_letters:
                combinations(prefix + l, num[1:])
        else:
            combinations(prefix, num[1:])

if __name__ == "__main__":
    main()
