#=====
def shift_cipher_encode(string, n):
   temp = ""
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   new = ""
   for elem in range( len(string)):
       if(string[elem] == " "):
           new += " "
       elif(string[elem].isalpha() == True):
           if(string[elem].isupper()):
               alphabet = alphabet.upper()
           elif(string[elem].islower()):
               alphabet = alphabet.lower()
           temp = alphabet[((alphabet.index(string[elem]) + n) % 26)]
           new += temp
       else:
           new += string[elem]
   return new



def shift_cipher_decode(string, n):
   temp = ""
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   new = ""
   for elem in range( len(string)):
       if(string[elem] == " "):
           new += " "
       elif(string[elem].isalpha() == True):
           if(string[elem].isupper()):
               alphabet = alphabet.upper()
           elif(string[elem].islower()):
               alphabet = alphabet.lower()
           temp = alphabet[((alphabet.index(string[elem]) - n) % 26)]
           new += temp
       else:
           new += string[elem]
   return new





# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run

# Wmfauw ak yjwsl! :)
print(shift_cipher_encode("Eunice is great! :)", 18))
# Qobkbny sc qbokd dyy!!!
print(shift_cipher_encode("Gerardo is great too!!!", 10))
# Gjwsfwit nx fqxt lwjfy! :I
print(shift_cipher_encode("Bernardo is also great! :D", 5))
# WYWM229 cm nby vymn wfumm un WMOFV
print(shift_cipher_encode("CECS229 is the best class at CSULB", 20))

# This is the 2nd lab.
print(shift_cipher_decode("Qefp fp qeb 2ka ixy.", 23))
# ThErE r m@ny m0rE Labs 2 come!
print(shift_cipher_decode("KyViV i d@ep d0iV Crsj 2 tfdv!", 17))
# s0 B prepared!
print(shift_cipher_decode("y0 H vxkvgxkj!", 6))
# pineapples
print(shift_cipher_decode("buzqmbbxqe", 12))