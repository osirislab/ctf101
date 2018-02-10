# Saturn
## Author
Crowell
## Points
300
## Category
Pwn
## Description

## Flag
`flag{greetings_to_pure_digital}`
## Solution
`solution.rb`
## Setup

## Notes
This challenge represents a flawed Challenge-Response Authentication scheme (CRA). The premise of this challenge is that the attacker is attempting to access a resource protected by CRA. The attacker has gained access to the binary that handles the CRA, but is missing a .so file which contains the algorithm to generate the challenges and responses!
CRA typically works, in a secure system, based on one-way functions.
eg.)
```
Challenge = "AAAAAAAA"
Response = HMAC-SHA1(secret-key, "AAAAAAAA")
```
In this case the attacker can not know how to generate proper responses, nor can the attacker even know what the algorithm used for responses is.
The system contains the same vulnerability as Pure-Digital's One-Time-Use
"saturn" Camcorder.
Because the Challenges and Expected Responses are contiguous in memory, and index of the requested challenge is not checked, the attacker can view the expected responses.
The memory is laid out like so.
```
[ch0|ch1|ch2|ch3|ch4|ch5|ch6|ch7|re0|re1|re2|re3|re4|re5|re6|re7]
[-----------challenges----------|------------responses----------]
```
And the attack is like so.
```
Attacker: What is challenge #8?
Server: Challenge #8 is [re0]
Attacker: The response for Challenge #0 is [re0]
```
^^-- Repeat for all challenges.

Once the attacker is authenticated, the "read the key" function can be called.
See "solution.rb" for a solution written in ruby.