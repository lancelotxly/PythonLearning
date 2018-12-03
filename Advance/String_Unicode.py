'''
'str' denotes by 'Unicode' -->'UTF-8'--> 'bytes'
       'BA%*$#@'  is a string,
        |__where 'B' is a char, which is denoted by some 'Unicode identifier' e.g. 'U+xxxx'
                                                             |__ where these 'Unicode' must be encoded to 'bytes', and 'utf-8' is a method.
String: except some methods of Sequence.
        also has: s1 = s.join(iterable)  # joint 'for i in iterable' by 's', where 'i' must be str and 'len(iterable)>1'
                  list = s.split('a',[n])  # split string by 'a' n-times, each time will save the flanks of 'a' into list.
                  s1 = s.strip('a')  # search 's' and strip 'a' until the first not 'a' str
                  index = s.find('sub_str',[beg=0,end=len(s)]) # search 's' to find 'substr', if find out return the beg index of 'substr' or not return '-1'
                  s1 = s.replace('str','new_str',[n]) # replace 'str' of 's' into 'new_str' by n-times
                  s1 = s.casefold()  # 'ABJC%$##' --> 'abjc%$##'
                  s1 = s.upper()
                  s1 = s.lower()
                  judgement:
                        s.startswith('a',[beg=0,end=len(s)])  # whether 's' starts with 'a'
                        s.endswith('a',[beg=0,end=len(s)])   # whether 's' ends with 'a'
                        s.strisalnum()  # whether 's' composed by str and num
                        s.isalpha()     # whether 's' only includes str
                        s.isdight()     # whether 's' only includes num

bytes and bytearray: 1. definition
                        b = bytes(s/memoryview/array, encoding='utf-8') or b'\xa9'
                        b_array = bytearray(b)  # mutable
                    2. operations same to str and
                       bytes.fromhex('31 4B CE A9') # translate hexadecimal to bytes

encode and decode: open(encoding=), str.encode(encoding=), bytes.encode(encoding=)

UnicodeError:   UnicodeEncodeError    # str --> bytes, don't have corresponding code to 'Unicode'
                UnicodeDecodeError    # bytes --> str
                                      # solve:   errors = ignore/replace(?)/xmlcharrefreplace(xml)
                SyntaxError           # module.py includes some data which are not 'utf-8'
                                      # solve:  # coding: utf-8

Unicode 'Sandwich': to deal with .file
                    1. bytes --> str, as soon as possible
                    2. operate str
                    3. str --> bytes, as late as possible

                    with open('filename','r/w/rb/wb', encoding='utf-8', errors='ignore/replace/xmlcharrefreplace') as fp:
                          fp.read([size])/.readline()  # where fp is a 'TextIOWrapper' in 'r/w'; and for 'rb/wb' fp is a 'BufferedReader'

Unicode normalize: unicodedata.normalize('NFC/NFD',str)
                   # where NFC (Normalization Form Combing) which recombine the Unicode based on the smallest digits
                    and NFD (Normalization Form Diversity) which diversities the combination Unicode into basic Unicode and the additions.
'''
from unicodedata import normalize, combining

def shave_marks(txt):
   norm_txt = normalize('NFD',txt)
   shaved = ''.join(c for c in norm_txt if not combining(c))
   return normalize('NFC',shaved)

order = '''Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.'''
shaved = shave_marks(order)
print(shaved)