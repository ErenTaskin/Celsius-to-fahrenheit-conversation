def c_to_f():
 print('Celcius to fahrenheit or fahrenheit to celcius?(c to f or f to c)')
 x = input()   
 if x == 'c to f':
    print('How much celcius?')
    c = float(input())
    f = float(c * 9/5 + 32)
    print('%s celcius is %s fahrenheit.'% (c, f))
 elif x == 'f to c':
    print('How much fahrenheit?')
    f1 = float(input())
    c1 = float(5/9 * (f1-32))
    print('%s fahrenheit is %s celcius.'% (f1, c1))
 else:
    c_to_f()

 input('Press ENTER to exit')

c_to_f()
