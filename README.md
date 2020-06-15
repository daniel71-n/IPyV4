# IPyV4
A module of various ipv4-related functions 


**Some examples:**


Convert a subnet mask in CIDR notation to its dotted-decimal notation.
```
>>> get_cidr('/25', reverse=True)

/25   : 255.255.255.128  
```

Convert a dot-notation IP address and a CIDR-notation subnet mask to their binary representation:
```
>>> get_bin('192.168.0.10', '255.255.255.128')

192.168.0.10      | 11000000.10101000.00000000.00001010

255.255.255.128   | 11111111.11111111.11111111.10000000

```

Get the subnet address and the broadcast address of a particular [ IP address - subnet mask (in CIDR) ] combination. 
```
>>> get_ends('192.168.0.53', '/25')

           subnet address : 192.168.0.0                   
        broadcast address : 192.168.0.127
```

Get the 1's complement representation of an octet. Useful with negative integers. 
```
>>> get_1c(-53)
'11001010'
```

Get the 2's complement representation of an octet. Useful with negative integers. 
```
>>> get_2c('-53')
'11001011'
```

Convert an octet in binary, 2's complement representation to a decimal.
```
>>> get_2c('10011001')
'-103'

```
