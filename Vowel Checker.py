def main():
    print("Enter any word", end=' ')
    w=input()
    # w='Roger'
    #counter variable
    i=0
    #loop to check each letter
    for l in w:
        # condition to check whether it is a vowel
        if l in "aeiouAEIOU":
            i+=1

    print(f"The number of vowels in the given word is {i}")
    
    
main()