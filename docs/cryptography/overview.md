# Cryptography

Cryptography is the reason we can use banking apps, transmit sensitive information over the web, and in general protect our privacy. However, a large part of CTFs is breaking widely used encryption schemes which are improperly implemented. The math may seem daunting, but more often than not, a simple understanding of the underlying principles will allow you to find flaws and crack the code.

The word “cryptography” technically means the art of writing codes. When it comes to digital forensics, it’s a method you can use to understand how data is constructed for your analysis.

!!! Math in Cryptography

    Most modern cryptography systems rely on one way mathematical algorithms derived from [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic). It's an ongoing arms race to create and implement better hardware and algorithms. 

    For example, the [implementation of the first RSA algorithm](https://people.csail.mit.edu/rivest/Rsapaper.pdf) is completely reliant on the "difficulty of factoring large numbers". It's a great example of security by design, and modern application developers still use similar derivatives.
    
    In August 2024, NIST released the first standards for post-quantum encryption to remediate the quantum-computing threat against legacy systems. For more information, check out this [blog post](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)!

## What is cryptography used for?

**Uses in every day software**

- Securing web traffic (passwords, communication, etc.)
- Securing copyrighted software code
- Key exchange algorithms 

**Malicious uses**

- Hiding malicious communication
- Hiding malicious code

<!--
## Challenges

### Easy

- [Crypto 1 (2011)](/challenges/2011/crypto/crypto1.md)
- [Crypto 2 (2011)](/challenges/2011/crypto/crypto2.md)
- [Crypto 3 (2011)](/challenges/2011/crypto/crypto3.md)
- [Crypto 4 (2011)](/challenges/2011/crypto/crypto4.md)
- [ECXOR](/challenges/2017/crypto/ecxor.md)
- [Another XOR](/challenges/2017/crypto/another_xor.md)
- [Sleeping Guard](/challenges/2016/crypto/Sleeping_Guard.md)
- [Katy](/challenges/2016/crypto/katy.md)
- [Notesy](/challenges/2015/crypto/notesy.md)
- [EPS](/challenges/2015/crypto/eps.md)
- [Punchout](/challenges/2015/crypto/punchout.md)
- [Feal](/challenges/2014/crypto/feal.md)
- [STFU](/challenges/2013/Crypto/stfu.md)

### Medium

- [Crypto 5 (2011)](/challenges/2011/crypto/crypto5.md)
- [Crypto 6 (2011)](/challenges/2011/crypto/crypto6.md)
- [Crypto 7 (2011)](/challenges/2011/crypto/crypto7.md)
- [Almost XOR](/challenges/2017/crypto/almost_xor.md)
- [Lupin](/challenges/2017/crypto/Lupin.md)
- [Neo](/challenges/2016/crypto/Neo.md)
- [Killer Cipher](/challenges/2016/crypto/Killer_cipher.md)
- [Check Plz](/challenges/2015/crypto/check-plz.md)
- [Psifer School](/challenges/2014/crypto/psifer_school.md)
- [Mountainsound](/challenges/2014/crypto/mountainsound_-_Stortz.md)
- [CSAW Pad](/challenges/2013/Crypto/CSAWpad.md)
- [Only This Program](/challenges/2013/Crypto/onlythisprogram.md)

### Hard

- [Crypto 8 (2011)](/challenges/2011/crypto/crypto8.md)
- [Crypto 9 (2011)](/challenges/2011/crypto/crypto9.md)
- [Crypto 10 (2011)](/challenges/2011/crypto/crypto10.md)
- [Crypto 2012](/challenges/2012/crypto/crypto1.md)
- [Side-channel](/challenges/2017/crypto/Side-channel.md)
- [Baby Crypt](/challenges/2017/crypto/baby_crypt.md)
- [Broken Box](/challenges/2016/crypto/Broken_Box.md)
- [Still Broken Box](/challenges/2016/crypto/Still_Broken_Box.md)
- [Another Broken Box](/challenges/2016/crypto/Another_Broken_Box.md)
- [Slabs of Platinum](/challenges/2015/crypto/slabs-of-platinum.md)
- [Bricks of Gold](/challenges/2015/crypto/bricks_of_gold.md)
- [CFB Sum](/challenges/2014/crypto/cfbsum.md)
- [Wieners](/challenges/2014/crypto/Wieners_-_Antoniewicz.md)
- [Slurp](/challenges/2013/Crypto/slurp.md)
-->
