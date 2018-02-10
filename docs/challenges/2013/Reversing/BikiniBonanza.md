# BikiniBonanza
## Author

## Points
150
## Category
Reversing
## Description

## Flag
`key(0920303251BABE89911ECEAD17FEBF30)`
## Solution
```
Hour:           1
MD5:            cfdf804ce0c601f97c3dc7c2026e44fd

Hour:           2
MD5:            d96090e563ea15b7c440684727b0fecf

Hour:           3
MD5:            8fd9b04487552379d6c48cef0d63cc82

Hour:           4
MD5:            f9a66fa6113821d352bebfaa6a7f1977

Hour:           5
MD5:            88a4c0cfa9e937d3d16a5d51f3ecd8b3

Hour:           6
MD5:            c2a0150a72390a2263964f07b88a13b1

Hour:           7
MD5:            ca88f85fdba05e5cb6307b93a1dc727f

Hour:           8
MD5:            5de1575b8e12b0d2eabb773bbfa10701

Hour:           9
MD5:            784c334c79a378fd62b0e156247c97b6

Hour:           10
MD5:            269d731cd5180a91ed6edda26dfe4c28

Hour:           11
MD5:            095b965fe1f52d30464ad0ce099f9b5f

Hour:           12
MD5:            bebf06d90d6f9652476d244470c66bec

Hour:           13
MD5:            10a9c866379106bc43b138e16cd58ba2

Hour:           14
MD5:            91d69e2c6e97f98d4ee096590e978a2d

Hour:           15
MD5:            6dbf3a8df194bf573f46086c9acd3828

Hour:           16
MD5:            aef0cbdcd943997e7bca5dd711e6f580

Hour:           17
MD5:            ca88f85fdba05e5cb6307b93a1dc727f

Hour:           18
MD5:            e139dc68a502e59913af688af225e2a2

Hour:           19
MD5:            374a03db139b5a43a21377d9410b34d7

Hour:           20
MD5:            83ff9d84ce21b77f217637d16e519b4f

Hour:           21
MD5:            bdc511d175460bafb2d1930d5155753f

Hour:           22
MD5:            18ddd65bc857a2332841521a3c83de5e

Hour:           23
MD5:            8436d9b870f35ada28918a00fbde944e

Hour:           24
MD5:            8bf731eed0da5507004f831477a48241
```
## Setup
Distribute `bikinibonanza.exe`
## Notes
.NET Reversing with slight obfuscation.
XOR input with a static string and md5 that along with the hour of the day. If the result is a certain hash the key is outputted.