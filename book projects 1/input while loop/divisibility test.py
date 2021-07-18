divisor = int(input("Enter the number : "))
qutoinet = int(input("Enter from whom to check the divisiblity test : "))

# sorry i dont know the spelling of the those😶
remainder = divisor%qutoinet

if remainder == 0:
    print(f'{divisor} is divisible by {qutoinet}')

else:
    print(f'\n\t{divisor} is not divisible by {qutoinet} ')
    print(f'\n\t{remainder} is the remainder left :( ')