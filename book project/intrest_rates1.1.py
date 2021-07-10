
print("\nfor simple intrest type '1' for compund type '2'")

# firstly take all the input that we need from user to execute

type_of_intrest = input("Intest type:")
type_of_intrest= type_of_intrest.rstrip()

principal =float( input("Principal: "))
time = float(input("Time period: "))
intrest_rate = float(input("Intest rate: "))


if {type_of_intrest == 2} :
     
    intrest_amount = 1+(intrest_rate/100)

    #its is to calulate other wise it going to mash with each other
    amount = principal*(intrest_amount**time)
    print(amount)
    
    # its quite complex to read out but after a time you can easily understand
    

else:

    print(principal*intrest_rate*time/100)
    # this is simple intrest formula
    # to make code short i directly use else statment


#compund intrest is equal {Amount=p*(1+r/100)**t}
# p = principal 
#r= rate of intrest
# t= time period