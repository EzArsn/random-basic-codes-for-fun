def main():
    print("Enter the text you want to alter the case \t",end='')
    org=input()
    #org="Thanks a lot"
    alt=""
    o=True
    for c in org:
        if o:
            alt=alt+c.lower()
        else:
            alt=alt+c.upper()
        o=not o

    print(alt)
    
    
    # mystring="Thanks"
    # newstring=""
    # odd=True
    # for c in mystring:
    #     if odd:
    #         newstring = newstring + c.lower()
    #     else:
    #         newstring = newstring + c.upper()
    #     odd = not odd
    # print(newstring)
main()