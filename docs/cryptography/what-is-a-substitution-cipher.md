# Substitution Cipher

A Substitution Cipher is system of encryption where different symbols are substituted by a different alphabet. We can take the letter `A` and replace all occurrences with `F`, `B` with `J`, and so on.

This gives us a key to use with encrypting and decrypting.
<!-- 
| Original | Key |
| --- | --- |
| A | F |
| B | J |
| C | A |
| D | B |
| E | Z | 
| F | C |
| G | M |
| H | S |
| I | N |
| J | T |
| K | O |
| L | H |
| M | Q |
| N | V |
| O | R |
| P | X |
| Q | W |
| R | I |
| S | K |
| T | U |
| U | L |
| V | J |
| W | P |
| X | G |
| Y | D | 
| Z | E | -->



## Language Entropy

[xkcd (936)](https://xkcd.com/936/)

Often times, we aren't going to be given a key to the cipher. In these cases, we use a strategy from natural language processing known as language entropy. We're looking to "predict" the occurrence of a certain letter based on it's usage in the language. 

For example, knowing "vowels are used in most words" gives you a hint that reduces the computation complexity.

!!! info
    In 1948, Claude Shannon published the first paper on the entropy of the English language. Modern natural language processing algorithms still cite the original research. Read the paper [here](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf).

## Example

!!! Example "Substitution cipher without a key"

    Without the key used to create the cipher, we can only try bruteforcing the combinations using the English language.
    Using the sample below, we can use a tool like [quipqiup.com](https://quipqiup.com/) to bruteforce what the original text is.

    ```
    Rbo rpktigo vcrb bwucja wj kloj hcjd, km sktpqo, cq rbwr loklgo 
    vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr.
    ```
    ![Cryptogram Example](images/quipqiup.gif)

    Our best guess at what the original phrase is:

    ```
    The trouble with having an open mind, of course, is that people 
    will insist on coming along and trying to put things in it.
    ```

