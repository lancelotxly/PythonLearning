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