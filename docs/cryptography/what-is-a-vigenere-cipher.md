# Vigenere Cipher

## Vigenere Cipher
A Vigenere Cipher is an extended [Caesar Cipher](./what-is-caesar-cipher-rot-13.md) where a message is encrypted using various Caesar shifted alphabets. A `key` is used to determine how many shifts each letter receives. It adds an additional layer of complexity that relies on the shared
key instead of a predetermined shift length.

!!! Example
    We'll use the following table can be used to encode a message:
    ![Vigenere Square](images/vigenere-square.png)

    ## Encryption
    Plaintext: `SUPERSECRET`<br>
    KEY: `CODE`

    1. `CODE` gets padded to the length of `SUPERSECRET` so the key becomes `CODECODECOD`.
    2. For each letter in `SUPERSECRET` we use the table to get the Alphabet to use, in this instance row `C` and column `S`.
    3. The ciphertext's first letter then becomes `U`.
    4. We eventually get `UISITGHGTSW`.

    ## Decryption

    1. Go to the row of the key, in this case `C` 
    2. Find the letter of the cipher text in this row, in this case `U`
    3. The column is the first letter of the decrypted ciphertext, so we get `S`
    4. After repeating this process we get back to `SUPERSECRET`

## Cryptanalysis
The key part of breaking a Vigenere Cipher is (not a pun) the key itself. Because it repeats, it's vulnerable to brute forcing the rotation by figuring out what the length of the key is. After, frequency analysis or key elimination is used to reverse the secret. We're not going to cover it here, but check out the footnotes for more![^2]

Online cipher solvers automatically use these steps!

!!! info
    For more information on how to determine the key length, check out this video on the [Kasiski Examination](https://www.youtube.com/watch?v=asRbswE2hFY).


[^1]:https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis
[^2]:https://www.youtube.com/watch?v=LaWp_Kq0cKs