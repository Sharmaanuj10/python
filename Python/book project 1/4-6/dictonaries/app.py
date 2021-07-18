phone=input( "Enter the number : ")

count={

    '1':'one',

    '2':'two',

    '3':'three',

    '4':'four',

    '5':'five',

    '6':'six',

    '7':'seven',

    '8':'eight',

    '9':'nine',

    '0':'zero'

}

output=""

for digit in phone:

    output+=count.get(digit, "")  + ' ' #<---- is here for spacing only or add space after digits
    # or output = output + count.get(digit, "") + ' '

print(output)

#finished code