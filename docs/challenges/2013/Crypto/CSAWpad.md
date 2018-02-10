# CSAWpad
## Author

## Points
200
## Category
Crypto
## Description
We recovered these texts, and sample program from the great nation of Astorkia's new communication system.  Included is the file we recovered, as well as the texts.
## Flag
`And yes the nsa can read this to`
## Solution
`csawpad-solve.py`
You do backwards pruning via candidates from what the ciphertext outputs, it's not too hard. 
Removed from the bottom of the program is this, if you want to change the plain texts, add or remove q's, and change the key however you'd like. Should be solvable where you have more than 2 ciphertexts, however 3 is the lower bound i'd give, 4 is kindof challenging where 8 is pretty easy,
q1="The difference between stupidity and genius is that genius has its limits- Albert Einstein"
q2="Go to Heaven for the climate, Hell for the company- Mark Twain"
q3="I am not a member of any organized political party. I am a Democrat- Will Rogers"
q4="My definition of an intellectual is someone who can listen to the William Tell Overture without thinking of the Lone Ranger- Billy Connolly"
q5="Republicans want less government for the same reason criminals want less cops- Anonymous"
q6="If there are no stupid questions, then what kind of questions do stupid people ask? Do they get smart just in time to ask questions?- Scott Adams"
q7="And now, in the interest of equal time, here is a message from the National Institute of Pancakes: It reads, and I quote, 'Fuck waffles.'- George Carlin"
key="MY key for you is {And yes the nsa can read this to}"
```
plainTexts=[q1,q2,q3,q4,q5,q6,q7,key]
pad=os.urandom(max(map(len,plainTexts)))

cTexts=map(hexlify,map(lambda x: encrypt(pad,x),plainTexts))
hPad=hexlify(pad)
from pprint import pprint
pprint(cTexts)
pprint(hPad)
```
The pad used to generate it was:
`79e49c82d5dd2b45f6c6b92778712b9b4b0f023ef801695594b9a0e17146f1470b86a88b9cae010b03475dea4400c2892660ea693f97af1d62650d62356dd769c3f182b4e4fd20163498a4dd4dc0399804c3057dd5b05df79af8ea447c69dc0e5ded0d4751fae2eb50407c96d4aef7fd95058e5d84b726bc2c2b6e9cef2a57d5ebef7db9b84c574e7293350bb1df77d79c5cccd8ca8f91ef`
## Setup
Distribute `csawpad.py`