# Alexander Taylor
## Author
Taylor
## Points
100
## Category
Recon
## Description
[https://www.google.com/search?&q=Alexander+Taylor](https://www.google.com/search?&q=Alexander+Taylor)
## Flag
`key{SPECIFICATIONS SUBJECT TO CHANGE WITHOUT NOTICE}`
## Solution
Realizing the image is worth looking at is a shot in the dark, but running strings on it or opening it in a hex editor should be a good enough hint that it's relevant. Parsing it as a PNG will reveal a number of chunks:
```
{"len"=>13, "type"=>"IHDR",
"data"=>"\x00\x00\x02\\\x00\x00\x01\x91\b\x02\x00\x00\x00",
"crc"=>1071708688}
{"len"=>43, "type"=>"tEXt", "data"=>"These aren't the chunks you're
looking for.", "crc"=>4229084457}
{"len"=>31, "type"=>"tEXt", "data"=>"You can go about your business.",
"crc"=>2127808360}
{"len"=>11, "type"=>"tEXt", "data"=>"Move along.", "crc"=>1260382793}
{"len"=>9, "type"=>"pHYs", "data"=>"\x00\x00.#\x00\x00.#\x01",
"crc"=>2024095606}
{"len"=>4, "type"=>"xORk", "data"=>"CSAW", "crc"=>217755783}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>1031027273}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>3009545151}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>1140890600}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>1527760996}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>4077746357}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>2634656386}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>3840852968}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>3781954558}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>235526}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>4151359583}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>460405057}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>2544949804}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>3782591050}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>1114296000}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>371779127}
{"len"=>16384, "type"=>"IDAT", "data"=>"...", "crc"=>2343741011}
{"len"=>11681, "type"=>"IDAT", "data"=>"...", "crc"=>854150729}
{"len"=>52, "type"=>"kTXt",
"data"=>"(68,\x10\x03\x04\x14\n\x15\b\x14\x02\a\b\x18\r\x00a\x04\x16\x11\v\x12\x00\aa\x03\fs\x02\x1F\x02\x1D\x06\x12c\x04\b\x03\v\x1C\x14\x03c\x1D\x0E\x03\n\x10\x04*",
"crc"=>1636805825}
{"len"=>0, "type"=>"IEND", "data"=>"", "crc"=>2923585666}
```
The "xORk" (xor key) and "kTXt" (key text) chunks are not in the spec. Solving the challenge simply involves taking the xor key and xoring it with the key text.
## Setup
Distribute `ataylor.png`