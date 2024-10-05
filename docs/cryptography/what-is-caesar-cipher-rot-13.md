# Caesar Cipher/ROT 13

## Caesar Cipher

The Caesar Cipher or Caesar Shift is a cipher which uses the alphabet in order to encode texts. The idea is to encode each letter with another letter in a "fixed" set of shifts. 

!!! info
    `CAESAR` encoded with a shift of 8 is `KIMAIZ` so `ABCDEFGHIJKLMNOPQRSTUVWXYZ` becomes `IJKLMNOPQRSTUVWXYZABCDEFGH`

Breaking a ciphertext is incredibly easy as there are only 25 possible "shifts" in the English alphabet. 

!!! Example "Bruteforce?"
    We can use a tool like [cyberchef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)) to do this quickly but can also print out all the combinations in Python.
    
    ``` python
    secret = "iwtgt xh cd gxvwi pcs lgdcv. iwtgth dcan ujc pcs qdgxcv.".lower()
    for i in range(0, 26):
        decrypted_string = ""
        for j in range(0, len(secret)):
            letter = ord(secret[j])
            if (letter > 122) or (letter < 97) or secret[j] == " ":
                continue
            else:
                letter += 1
                if letter > 122:
                    letter = 97
                letter = chr(letter)
                decrypted_string += str(letter)  
        secret = decrypted_string.strip()  
        print(decrypted_string)
    
    #output
    #...
    #thereisnorightandwrongtheresonlyfunandboring
    #...
    ```

## ROT13

ROT13("Rotate 13") is the same thing but a fixed shift of 13, this is a trivial cipher to bruteforce because there are only 25 shifts. 

Generally, Caesar's Cipher and ROT13 are used in conjunction of other encryption methods to make the challenge more difficult!
