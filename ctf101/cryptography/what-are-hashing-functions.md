# Hashing Functions

Hashing functions are one way functions which theoretically provide a unique output for every input.

There are many different hashing functions and each is generally better suited for a different purpose. Some examples of hashing functions are MD5, SHA-1, SHA-2, SHA-256, SHA-512, bcrypt, scrypt, and PBKDF2.

Hashing functions are very useful in the validation of data. For example, websites usually store a hash of a user's password so that if they are hacked, the hacker doesn't get the user's original password.

When the user tries to login, they still provide their password as normal, however the website will "hash" it and compare it with the hash that it has saved.

For example the following code demonstrates how to perform an MD5 hash in Python:

```python
import hashlib
print(hashlib.md5('this_is_a_password').hexdigest())
```

The above code equates to the following:

`MD5(this_is_a_password)` -> `5f4dcc3b5aa765d61d8327deb882cf99`

From this output you can see that the original input (`this_is_a_password`) is no longer recognizeable after going through the MD5 hashing function.

An astute reader might notice something special. There is an infinite amount of data but an MD5 hash is only comprised up of 32 hexadecimal characters (or 128 bits). Thus, because of the pigeon hole principle, there must be two inputs which result in the same output. This is known as a hash collision. In cryptographic calculations, hash collisions are generally considered a bad thing. This is because having two inputs that yield the same hash can have security implications.

!!! note
    What if you downloaded two programs, one program is malicious and one program is safe. On top of that, they both have the same MD5 hash! Now how do we know which program is safe to use?

MD5, SHA-1, and other hashes once considered secure have now been found to have collissions and as such shouldn't be used for operations that require security.