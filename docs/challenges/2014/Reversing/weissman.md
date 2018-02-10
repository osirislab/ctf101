# Weissman
## Author
Stortz
## Points

## Category
Reversing
## Description
Extract the key!
## Flag
`flag{I know how long it'd take me, and I can prove it}`
## Solution

## Setup
Distribute `weissman.csawlz-cab77581f57c13b04177058f5d2660f7`
## Notes
Weissman implements a custom lz-inspired compression algorithm. The algorithm is fairly naive and barely compresses at all, but it should be possible to reverse engineer from the compressed file and a few example uncompressed sources.

The weissman.csawlz file has 3 files compressed in it:
  * key.jpg - a picture with the key text on it
  * hash.html - a page about hashes
  * pg28885.txt - Alice in Wonderland from Project Gutenburg

With the two public sources, it should be possible to rebuild the compression algorithm.

The algorithm is naive and hash-based. It hashes the first 4 bytes of every literal stream (of max 9 characters) and adds those to a hash table. If that stream is encountered again, it emits a backreference to the last stream. Reverse engineering the hash algorithm isn't entirely neccisary, if you ignore it the resulting key.jpg is corrupted but still readable.

Hint:
```
typedef struct _hdr {
	uint8_t magic[8];
	uint32_t version;
	uint32_t num_files;
} hdr;

typedef struct _entry {
	uint32_t magic;
	uint32_t compressed_size;
	uint32_t uncompressed_size;
	uint8_t filename[32];
} entry;
```