#Part 2 Celsius to Fahrenheit

name = input ('What is your name?:')
country = input ('What is your country?:')
temperature_cel = int(input ('What is the current temperature in Celsius?:'))
temperature_fa = int((9/5)*temperature_cel +32)
print ('Hello',name, 'The temperature in Celsius is', temperature_fa, 'degrees Fahrenheit in' , country)
