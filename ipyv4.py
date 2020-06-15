"""a set functions that make routine handling of IPv4 address easier"""


from typing import List



def get_bin (ip_address: str, subnet_mask: str = None) -> str:
  " takes IP and subnet mask(optional) in dot notation and returns them in binary" 
  

  tp_ip = tuple(ip_address.split('.'))
  oct1, oct2, oct3, oct4 = tp_ip
  bin_ip = "{:08b}.{:08b}.{:08b}.{:08b}".format(int(oct1), int(oct2), int(oct3), int(oct4))

  if subnet_mask != None: 
    tp_mask = tuple(subnet_mask.split('.'))
    octa, octb, octc, octd = tp_mask
    bin_mask = "{:08b}.{:08b}.{:08b}.{:08b}".format(int(octa), int(octb), int(octc), int(octd))
 
    res = print("\n{:17} | {:30}\n\n{:17} | {:30}\n".format(ip_address, bin_ip, subnet_mask, bin_mask))
 
  else: res = print("\n{:17} | {:30}\n".format(ip_address, bin_ip))

  return res






def get_cidr(subnet_mask: str, reverse=False) -> str:
  "return a dot-notation subnet mask as CIDR prefix notation. If reverse is set to true, get dot notation from mask passed in CIDR notation"

  if reverse==False:            # the default: get dot notation from CIDR notation
    tp_mask = tuple(subnet_mask.split('.'))
    oct1, oct2, oct3, oct4 = tp_mask
    bin_mask = "{:08b}{:08b}{:08b}{:08b}".format(int(oct1), int(oct2), int(oct3), int(oct4))

    cidr = 0

    for i in bin_mask:
      if i == '1':
        cidr += 1
      else: break

    res = print("\n{:17} : /{:<5}\n".format(subnet_mask, cidr))


  elif reverse == True:         # if a dot notation translation needs to be done from CIDR notation
    stripped = subnet_mask[1:]  # remove the slash from the CIDR notation
    #print(stripped, 'stripped')
    difference = 32 - int(stripped)  # the subnet masks identifies the 1s. This will determine how bits are left out of 32, which are NOT 1s, but 0s.
    numbers = []
    [numbers.append(1) for i in range(int(stripped))] and [numbers.append(0) for i in range(difference)]
    #print(numbers, 'numbers')
    
    oct1=oct2=oct3=oct4=None
    numbers_iter = list(zip(*([iter(numbers)]*8)))
    #print('numbers_iter', numbers_iter)
    for [w,x,y,z] in [numbers_iter]:
      #print(w,x,y,z)
      oct1 = ''.join([str(i) for i in w])
      oct2 = ''.join([str(i) for i in x])
      oct3 = ''.join([str(i) for i in y])
      oct4 = ''.join([str(i) for i in z])
      #print(oct1,oct2,oct3,oct4, sep='\n')
      
    dot_mask = "{:d}.{:d}.{:d}.{:d}".format(int(oct1, 2), int(oct2, 2), int(oct3, 2), int(oct4, 2)) #converting binary numbers (which are really strings), into an integer, using int with base 2.

    res = print("\n{:<5} : {:17}\n".format(subnet_mask, dot_mask))

    return res






def get_ip_quant(ip1: str, ip2: str) -> str:
  "return how many IP addresses there are between any two given IP addresses"


  # ip1_octets = tuple(ip1.split('.'))
  # ip2_octets = tuple(ip2.split('.'))
  
  ip1_oct1, ip1_oct2, ip1_oct3, ip1_oct4 = tuple(ip1.split('.'))
  ip2_oct1, ip2_oct2, ip2_oct3, ip2_oct4 = tuple(ip2.split('.'))
  
  bin_ip1 = "{:08b}{:08b}{:08b}{:08b}".format(int(ip1_oct1), int(ip1_oct2), int(ip1_oct3), int(ip1_oct4))
  bin_ip2 = "{:08b}{:08b}{:08b}{:08b}".format(int(ip2_oct1), int(ip2_oct2), int(ip2_oct3), int(ip2_oct4))
  
  res = '%i' % (int(bin_ip1, 2) - int(bin_ip2, 2))
  return print('\n', abs(int(res)),'\n') #abs prevents printing the - sign for negative integers








def get_oct_split(arg: str) -> List[str]:
  "split a 32-bit address in binary into its component octets and return a list of them"
  octet_list = []
  octet_list.append(arg[0:8])
  octet_list.append(arg[8:16])
  octet_list.append(arg[16:24])
  octet_list.append(arg[24:])
  
  return octet_list




def get_binary_octet(arg: int) -> str:
  "convert a decimal integer to a binary octet"
  return "{:08b}".format(int(arg))





###########################################################
##################################################################
def get_1c(arg: str) -> str:
    """ get the 1's complement representation for the argument value passed. I.e. e.g. pass -32 and get -32 in binary. The function only handles octets. This means the maximum negative value is -127 and the maximum positive value is 127. You can't get the 1's complement representation for -400, for example, because it doesn't fit in a 1's complement octet: 1 bit is reserved for the sign, leaving 2**7 total values, making the maximum 127 on both sides, since with 1's compliment we have a '0' and a '-0'

If a decimal is passed, the value returned is the argument's 1's complement binary representation.
If passed a binary octet, the function assumes it represents a 1's complement value, and it will try to return the decimal value that the argument is supposed to represent 
"""
    num = None
    #try: 
    if len(str(arg)) == 8:   #this means the argument is a binary value - a binary octet
        if arg[0] == '-':
            return print("Invalid input. Incorrect format for negative binary integers. They're not supposed to start with a '-' sign, but be in 1's complement format.")
        elif arg[0] == '1':  #if the leftmost bit is 1, it's a negative number 
            if int(arg[1:], base=2) > 127:#the maximum negative value
                return print("invalid value: the maximum negative value in a 1's complement octet is 127. The value passed is too big and its 1's complement value does not fit in an octet")
            elif int(arg[1:], base=2) <= 127: #this is 128 because -127 is 100000000, which would really be 128 if it were positive.It's a valid value, though.
                num = arg
        #elif arg[0] == '0':  #else, if it's a positive number
            #if int(arg, base=2) > 127:  #the maximum positive value is 127
                #return print("127 is the highest value for which the correposnding 1's complement will fit in an octet.")

        else:   # if it's a positive value
          if int(arg, base=2)<=127:
            num = arg
          #else:
            #return print("invalid value. The maximum positive value in a 1's complement octet is 127")


        res = ''
        if num[0] == '1':       # if it's a negative number
          if int(num, base=2) == 128:  # is the value is 128, ie 100000000, which is actually valid but would mess up the rules
            res = '-' + '127'          # 100000000 looks like 128, but it's actually 127 with the bits flipped. Just imagine the 0s were 1s and 1s were 0s, there would be 1 zero and 7 1s, which would amount to 127.
            return res

          else:                 # if the value isn't 128, then the leftmost bit shouldn't be considered (only ued for the sign), and the total value is given by the other seven bits to the right. It can only be < 128. If it's >, an exception will have already been raised per the conditionals above
            res = '-'
            temp = '-' + str(int(num[1:], base=2))  # this would return the binary number just as if it were positive.
            for i in num:
              if i == '0':
                res+='1'
              if i == '1':
                res+= '0'
            return int(res, base=2)
                        
        elif num[0] == '0':     # if it's a positive number
          res = str(int(num, base=2))
          return res




    ## if (arg) < 255:  #if it's not 8 digits (well, characters, since it's passed as a string), it's a decimal number eg 42, or 255. if it's larger than 255, it's an invalid value since it doesn't fit in an octet - 2**8
    else:  #if the length of the input isn't 8, it means it's not an octet in binary, and can therefore only be a decimal < abs(-128) (negatives) or <127 (positives)
        negative = None #make a note of whether the value is negative or not.
        negative = True if str(arg)[0] == '-' else False
        #print(negative)

        if negative == True:
            if abs(int(arg)) > 127:
                return print("invalid value. Negative values > 127 don't fit in a 2's complement octet")
            else:   #if it's <= 127
                #return print(get_binary_octet(abs(int(arg))))
                num = '1' + get_binary_octet(abs(int(arg)))[1:] #the first bit has to be on, since it's a negative value


        elif negative == False:
             if (abs(int(arg)) > 127): #the maximum positive value is 127, as for negative values
                 return print("invalid value. Positive values > 127 don't fit in a 2's complement octet")

             else:  #if abs(int(arg)) <= 127
                 num = get_binary_octet(abs(int(arg)))
   # except:
        #return print('invalid innut')
   
   
    #else:  #if there's no exception
        #res = ''
   
    
    if negative == False:
     res = num
     return res

    elif negative == True:
     res = '1' # leftmost bit is 1, the number is negative 
     for bit in num[1:]:  #leaving the first bit alone, as it's already been set to one to carry the negative sign #one's complement is simply a reversal of the bits from 0 to 1 and 1 to 0. The complement flips the values on their head; in this particular case it's that more simple because we know the how many bits we're dealing with: 8.
       if bit == '0':
         res+='1'
       elif bit == '1':
         res+='0'
     return res




def get_2c(arg: str) -> str:
  """
   return the 2's complement representation for the argument passed in.
   If the argument is a decimal, the function will return its two's complement representation in binary.
   If the argument is a binary octet, the function will try to return the decimal value that the argument value is supposed to represent. 
   
    The argument passed in should be enclosed in quotation marks. 

   Since only 7 bits are available, the leftmost one carrying the sign, the maximum positive value is 127, and the maximum negative one 128 (since with 2's complement, there's no -0 as with 1's complement. What this means is that trying to get the two's complement representation for, say, -200 will return an error, since that requires more bits than the ones available in an octet"""
  value = str(arg)

  if len(arg) == 8:             # if the argument passed is a binary octet
    if not value[0] == '1':
      #print('not negative')
      res = int(value, base=2)
      return res

    elif value[0] == '1':            # it's a negative number
      #print('negative')
      if int(value, base=2) == 128:  # if it's 100000000, it means it's -128, so return that
        res = '-' + str(int(value, base=2))
        #print(res)
        return res

      else:
        num = int(value[1:], base=2)  # disregarding the leftmost bit, which is only there to carry the sign
        res = int(num)
        res = '-' + str((2**7)-res)
        return res



  else:
      
    if not value[0] == '-':       # if the number is positive
      if int(value) > 127:
        return print('invalid input. The maximum positive value is 127')
      else:
        res = get_binary_octet(value)
        return res


    elif value[0] == '-':
      max_neg_value = 2**8

      if abs(int(value)) > 128:        # 2's complement doesn't have a -0 like 1's complement, so negative values go up to (or 'down' to, rather) (-)128, unlike positive values, which only go to 127, since counting starts at 0 on that side.
        return print('invalid input. The maximum negative value is -128')

      try:
        complement = max_neg_value - abs(int(value))
        #print('complement', complement)
        res = get_binary_octet(complement)
        #print('res', res)
        res = '1'+res[1:]           # making sure the first bit is 1, since the number is negative
        return res
      except:
        print('error: invalid input. The number has to be < 128, and a decimal')




      


  

def get_ends(ip_address: str, cidr_prefix: str) -> str:
  "return the subnet/network address and the broadcast address given an IP address and a netmask in CIDR notation"
  
  ip_binary = ''.join([get_binary_octet(i) for i in tuple(ip_address.split('.'))])
     
  cidr_value = int(cidr_prefix.lstrip('/'))  # remove the slash '/' chacracter from the cidr prefix, so as to get an integer-convertible value
  

  
  #translating the cidr notation into binary
  
  #step 1: get all the "1's" specified by the value ontained above (e.g. /24 = 24 bits turned on)
  cidr_bin_list = []
  [cidr_bin_list.append('1') for i in range(cidr_value)]

  #step 2: right-fill the value obtained above with 0's in a 32-character-wide field, using the string format method
  cidr_bin_string = "{:0<32}".format(''.join(cidr_bin_list))  # if there are /24 bits turned on, 8 characters remain, and they'll all be 0's
  
  #split the 32-bit netmask value obtained above into octets 
  mask_o1, mask_o2, mask_o3, mask_o4 = get_oct_split(cidr_bin_string)
  

  
  #the subnet address is all 0's, obtained by doing a bitwise AND operation on an ip address and its given netmask
  subnet_address = ''

  host_bits = ip_binary[cidr_value:]
  all_host_bits_off = host_bits.replace('1', '0')  # turn off all bits on the host side
  
  subnet_address_binary = ip_binary[:cidr_value] + all_host_bits_off
  subnet_address_binary_octets = get_oct_split(subnet_address_binary)
  subnet_address = '.'.join([str(int(i, 2)) for i in subnet_address_binary_octets])



  # the broadcast address is all 1's
  broadcast_address = ''

  all_host_bits_on = host_bits.replace('0', '1')  # turn on all bits on the host side
   
  broadcast_address_binary = ip_binary[:cidr_value] + all_host_bits_on
 
  broadcast_address_binary_octets = get_oct_split(broadcast_address_binary)
  broadcast_address = '.'.join([str(int(i, 2)) for i in broadcast_address_binary_octets])

  res = print("\n{0:>25} : {1:<30}\n{2:>25} : {3:}\n".format("subnet address", subnet_address, "broadcast address", broadcast_address))
  return res














