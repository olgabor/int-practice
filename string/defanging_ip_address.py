# -----------------------------------------------------------
#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

# -----------------------------------------------------------
address = "1.1.1.1"
address1 = "255.100.50.0"

def defangIPaddr(address):
    
    # new = address.replace('.', '[.]') # replace version 
    new = address.split('.')
    return '[.]'.join(new) 

print(defangIPaddr(address))
print(defangIPaddr(address1))