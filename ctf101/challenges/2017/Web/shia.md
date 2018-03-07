# Shia Labeouf-off!
## Author

## Points
150
## Category
Web
## Description
Do it
Just do it

Don't let your dreams be dreams
Yesterday you said tomorrow
So just do it
Make your dreams come true
Just do it

Some people dream of success
While you're gonna wake up and work hard at it
Nothing is impossible

You should get to the point
Where anyone else would quit
And you're not going to stop there
No, what are you waiting for?

Do it
Just do it
Yes you can
Just do it
If you're tired of starting over
Stop giving up

Pick 1:
* http://web.chal.csaw.io:5487
* http://web.chal.csaw.io:5488
* http://web.chal.csaw.io:5489
* http://web.chal.csaw.io:5490

## Flag
`flag{wow_much_t3mplate}`
## Solution
Go to /polls/3/ to cause a "Our infrastructure can't support that many Shias!" exception.
Scroll down to the "checknum" function call and view the source code, note the "getme" and "listme" funcs.
Go to /ad-lib/ and type `{% debug %}` and notice `mrpoopy`
Go back and send `{{ mrpoopy|listme }}` notice `__flag__`
Go back and send `{{ mrpoopy|getme:"__flag__" }}` 
Note: because it is an underscore, you can't just do `{{ mrpoopy.__flag__ }}`

## Setup
Website runs on port 8000