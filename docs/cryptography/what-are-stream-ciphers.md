# Stream Ciphers

A Stream Cipher is used for symmetric key cryptography, or when the same key is used to encrypt and decrypt data. Stream Ciphers encrypt pseudorandom sequences with bits of plaintext in order to generate ciphertext, usually with XOR. A good way to think about Stream Ciphers is to think of them as generating one-time pads from a given state. 


## Definitions

- A **keystream** is a sequence of pseudorandom digits which extend to the length of the plaintext in order to uniquely encrypt each character based on the corresponding digit in the keystream

## One Time Pads

A *one time pad* is an encryption mechanism whereby the entire plaintext is XOR'd with a random sequence of numbers in order to generate a random ciphertext. The advantage of the one time pad is that it offers an immense amount of security BUT in order for it to be useful, the randomly generated key must be distributed on a separate secure channel, meaning that one time pads have little use in modern day cryptographic applications on the internet. Stream ciphers extend upon this idea by using a key, usually 128 bit in length, in order to seed a pseudorandom *keystream* which is used to encrypt the text.

## Types of Stream Ciphers

### Synchronous Stream Ciphers

A Synchronous Stream Cipher generates a keystream based on internal states *not* related to the plaintext or ciphertext. This means that the stream is generated pseudorandomly outside of the context of what is being encrypted. A *binary additive stream cipher* is the term used for a stream cipher which XOR's the bits with the bits of the plaintext. Encryption and decryption require that the synchronus state cipher be in the same state, otherwise the message cannot be decrypted. 

### Self-synchronizing Stream Ciphers

A Self-synchronizing Stream Cipher, also known as an asynchronous stream cipher or ciphertext autokey (CTAK), is a stream cipher which uses the previous *N* digits in order to compute the keystream used for the next *N* characters.

!!!note
	Seems a lot like block ciphers doesn't it? That's because block cipher feedback mode (CFB) is an example of a self-synchronizing stream ciphers.

## Stream Cipher Vulnerabilities

### Key Reuse

The key tenet of using stream ciphers securely is to **NEVER** repeat key use because of the communative property of XOR. If C~1~ and C~2~ have been XOR'd with a key K, retrieving that key K is trivial because C~1~ XOR C~2~ = P~1~ XOR P~2~ and having an english language based XOR means that cryptoanalysis tools such as a character frequency analysis will work well due to the low entropy of the english language.

### Bit-flipping Attack

Another key tenet of using stream ciphers securely is considering that just because a message has been decrypted, it does not mean the message has not been tampered with. Because decryption is based on state, if an attacker knows the layout of the plaintext, a Man in the Middle (MITM) attack can flip a bit during transit altering the underlying ciphertext. If a ciphertext decrypts to 'Transfer $1000', then a middleman can flip a single bit in order for the ciphertext to decrypt to 'Transfer $9000' because changing a single character in the ciphertext does not affect the state in a synchronus stream cipher.