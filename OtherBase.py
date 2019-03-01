'''
Other Basic knowledge: Encode/Decode, Format, Traverse, Numerical Operation
'''
'''
Encode/Decode: 1. DEFINE: translate 'str' to machine code(010101).
               2. PROTOCOL: Unicode(2 byte), ASCII(1 byte), UTF-8(1 byte for English, 3 byte for Chinese)
               3. Using:    Save in memory using 'Unicode'
                            Transmit using 'UTF-8': For Sender, 'ABC'.encode('utf-8') # b'ABC'
                                                    For Receiver, b'ABC'.decode('utf-8')
'''

'''
Format:  1. %:   %d int, %f float, %s str, %x 0xff
                 e. g. 'hi, %s, you have %.2f dollars' % ('John', 100.234)
         2. format
                 e. g. 'hi, {0}, you have {1:.2f} dollars'.format('John',100.234) 
'''

'''
Traverse: for x in:
          while:
          break
          continue:
'''

'''
Numerical Operation: +, -, *, /, //, %, **
'''

'''
Others: 1. eval('str'):  #  return value of 'str' as Expression 
        2. enumerate(Seq):  #  return (index, value)
        3. locals():  # return local variables
        4. globals():  # return global variables
        5. 'str'.strip(char) # return 'str', strip 'char'
        6. input('str'): # return <class 'str'>
        7. sum(iterable): # return sum 
        8. Num: abs(), max(), hex()
        9. Data Transform: int(), float(), str(), bool()
'''