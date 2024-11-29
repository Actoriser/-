import hashlib
import itertools

def crack(hash):
   
    for pin_tuple in itertools.product("0123456789", repeat=5):
        pin = ''.join(pin_tuple)  
        
        if hashlib.md5(pin.encode()).hexdigest() == hash:
            return pin