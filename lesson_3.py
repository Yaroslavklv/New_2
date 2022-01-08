first_number = int(input("enter a three-digit integer"))

additional_number=0
additional_number=additional_number*10+first_number%10
first_number=first_number//10
additional_number=additional_number*10+first_number%10
first_number=first_number//10
additional_number=additional_number*10+first_number
print(additional_number)
