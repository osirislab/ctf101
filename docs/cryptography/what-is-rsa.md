# RSA

RSA, which is an abbreviation of the author's names (Rivest–Shamir–Adleman), is a cryptosystem which allows for asymmetric encryption. Asymmetric cryptosystems are alos commonly referred to as **Public Key Cryptography** where a public key is used to encrypt data and only a secret, private key can be used to decrypt the data.

## Definitions

- The **Public Key** is made up of $(n, e)$
- The **Private Key** is made up of $(n, d)$
- The message is represented as $m$ and is converted into a number
- The encrypted message or ciphertext is represented by $c$
- $p$ and $q$ are prime numbers which make up $n$
- $e$ is the public exponent
- $n$ is the modulus and its length in bits is the bit length (i.e. 1024 bit RSA)
- $d$ is the private exponent
- The totient $\lambda(n)$ is used to compute $d$ and is equal to the $lcm(p-1, q-1)$, another definition for $\lambda(n)$ is that 

$$\lambda(pq) = lcm(\lambda(p), \lambda(q))$$

## What makes RSA viable?

If public $n$, public $e$, private $d$ are all very large numbers and a message $m$ holds true for 0 < $m$ < $n$, then we can say:

<!-- this is a bit of a hack to get no space between the modulus and the n value in Latex -->
$$ (m^e)^d \equiv m \;(\bmod\; n) $$ 

!!! note
	The triple equals sign in this case refers to [modular congruence](https://en.wikipedia.org/wiki/Modular_arithmetic) which in this case means that there exists an integer *k* such that 
	
	$$(m^e)^d = kn + m$$

RSA is viable because it is incredibly hard to find $d$ even with $m$, $n$, and $e$ because factoring large numbers is an arduous process.


## Implementation

RSA is implemented in 3 steps:

1. [Key Generation](#key-generation)
2. [Encryption](#encryption)
3. [Decryption](#decryption)

### Key Generation

We are going to follow along Wikipedia's small numbers example in order to make this idea a bit easier to understand.

!!!note
	In this example we are using *Carmichael's* totient function where 
	
	$$\lambda(n) = lcm(\lambda(p), \lambda(q))$$
	
	but *Euler's* totient function is perfectly valid to use with RSA. Euler's totient is 
	
	$$\phi(n) = (p − 1)(q − 1)$$

1. Choose two prime numbers such as: 
	* $p = 61$ and $q = 53$
2. Find $n$: 
	* $n = pq = 3233$
3. Calculate $\lambda(n) = lcm(p-1, q-1)$
	* $\lambda(3233) = lcm(60, 52) = 780$

4. Choose a public exponent such that $1 \lt e \lt \lambda(n)$ and is coprime (not a factor of) $\lambda(n)$. The standard is most cases is $65537$, but we will be using: 
	* $e = 17$
5. Calculate $d$ as the modular multiplicative inverse or in english find $d$ such that: $d * e \;(\bmod\; \lambda(n)) = 1$
	* $d * 17 (\bmod\; 780) = 1$
	* $d = 413$

Now we have a public key of $(3233, 17)$ and a private key of $(3233, 413)$

### Encryption

With the public key, $m$ can be encrypted trivially

The ciphertext is equal to $m^e (\bmod\; n)$ or:

$$c = m^{17} (\bmod\; 3233)$$

### Decryption

With the private key, $m$ can be decrypted trivially as well

The plaintext is equal to $c^d (\bmod\; n)$ or:

$$m = c^{413} (\bmod\; 3233)$$

## Exploitation

From the [RsaCtfTool README](https://github.com/RsaCtfTool/RsaCtfTool)
>
Attacks:
>
- Weak public key factorization
- Wiener's attack
- Hastad's attack (Small public exponent attack)
- Small $q (q \lt 100,000)$
- Common factor between ciphertext and modulus attack
- Fermat's factorisation for close $p$ and $q$
- Gimmicky Primes method
- Past CTF Primes method
- Self-Initializing Quadratic Sieve (SIQS) using Yafu
- Common factor attacks across multiple keys
- Small fractions method when p/q is close to a small fraction
- Boneh Durfee Method when the private exponent d is too small compared to the modulus (i.e $d \lt n^0.292$)
- Elliptic Curve Method
- Pollards $p-1$ for relatively smooth numbers
- Mersenne primes factorization
