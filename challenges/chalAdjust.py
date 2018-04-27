import os
import shutil

dictOfLinks = {
        # Forensics
        "wireshark":"[Wireshark](/forensics/what-is-wireshark/)",
        "file formats":"[File Formats](/forensics/what-are-file-formats/)",
        "metadata":"[Metadata](/forensics/what-is-metadata/)",
        "steg":"[Steganography](/forensics/what-is-steganography/)",
        "disk imaging":"[Disk Imaging](/forensics/what-is-disk-imaging/)",
        "memory forensics":"[Memory Forensics](/forensics/what-is-memory-forensics/)",
        "hex editors":"[Hex Editors](/forensics/what-are-hex-editors/)",
        # Crypto
        "xor":"[XOR](/cryptography/what-is-xor/)",
        "substitution":"[Substitution Ciphers](/cryptography/what-is-a-substitution-cipher/)",
        "caesar":"[Caesar Ciphers](/cryptography/what-is-caesar-cipher-rot-13/)",
        "vigenere":"[Vigenere Ciphers](/cryptography/what-is-a-vigenere-cipher/)",
        "hashing":"[Hashing Functions](/cryptography/what-are-hashing-functions/)",
        "block":"[Block Ciphers](/cryptography/what-are-block-ciphers/)",
        "stream":"[Stream Ciphers](/cryptography/what-are-stream-ciphers/)",
        "rsa":"[RSA](/cryptography/what-is-rsa/)",
        # Web
        "sqli":"[SQL Injection](/web-exploitation/sql-injection/what-is-sql-injection/)",
        "commandi":"[Command Injection](/web-exploitation/command-injection/what-is-command-injection/)",
        "dirtrav":"[Directory Traversal](/web-exploitation/directory-traversal/what-is-directory-traversal/)",
        "csrf":"[Cross Site Request Forgery](/web-exploitation/cross-site-request-forgery/what-is-cross-site-request-forgery/)",
        "xss":"[Cross Site Scripting](/web-exploitation/cross-site-scripting/what-is-cross-site-scripting/)",
        "ssrf":"[Server Side Request Forgery](/web-exploitation/server-side-request-forgery/what-is-server-side-request-forgery/)",
        "php":"[PHP](/web-exploitation/php/what-is-php/)",
        # Reverse Engineering
        "asm":"[Assembly/Machine Code](/reverse-engineering/what-is-assembly-machine-code/)",
        "c":"[The C Programming Language](/reverse-engineering/what-is-c/)",
        "disass":"[Dissassemblers](/reverse-engineering/what-are-disassemblers/)",
        "gdb":"[Debuggers](/reverse-engineering/what-is-gdb/)",
        "decomp":"[Decompilers](/reverse-engineering/what-are-decompilers/)",
        # Binary Exploitation
        "reg":"[Registers](/binary-exploitation/what-are-registers/)",
        "stack":"[The Stack](/binary-exploitation/what-is-the-stack/)",
        "calling":"[Calling Conventions](/binary-exploitation/what-are-calling-conventions/)",
        "got":"[Global Offset Table](/binary-exploitation/what-is-the-got/)",
        "buff":"[Buffers](/binary-exploitation/what-are-buffers/)",
        "buffover":"[Buffer Overflow](/binary-exploitation/buffer-overflow/)",
        "rop":"[Return Oriented Programming](/binary-exploitation/return-oriented-programming/)",
        "nx":"[No eXecute](/binary-exploitation/no-execute/)",
        "aslr":"[ASLR](/binary-exploitation/address-space-layout-randomization/)",
        "relro":"[RELRO](/binary-exploitation/relocation-read-only/)",
        "canary":"[Stack Cookies/Canaries](/binary-exploitation/stack-canaries/)",
        "heap":"[The Heap](/binary-exploitation/what-is-the-heap/)",
        "heapex":"[Heap Exploits](/binary-exploitation/heap-exploitation/)",
        "fsv":"[Format String Vulnerability](/binary-exploitation/what-is-a-format-string-vulnerability/)"
        }


def copy_rename(old_file_name, new_file_name, src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file,dst_dir)    
    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)

rootDir = '.'

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

def hasBeenEdited(fileContents):
    for line in fileContents:
        if "Points" in line:
            return False
    return True

def editFile(fileToEdit):
    toProcess = open(fileToEdit, 'r')
    toWrite = []
    fileLines = toProcess.readlines()
    toProcess.close()
    if hasBeenEdited(fileLines):
        print "Has Been Edited"
        return
    for line in fileLines:
        print line
    for line in fileLines:
        toWrite.append(line)
    # Process Title/Author Stuff
    authInd = 0
    for i in range(len(toWrite)):
        if "## Author" in toWrite[i]:
            authInd = i
            break
    if toWrite[authInd + 1].strip() == "":
        toWrite.pop(authInd)
        toWrite.pop(authInd)
    elif authInd == 0:
        pass
    else:
        toWrite[authInd] = "\nBy " + toWrite[authInd+1] + "\n\n\n"
        toWrite.pop(authInd+1)

    # Process Points
    authInd = 0
    for i in range(len(toWrite)):
        if "## Points" in toWrite[i]:
            authInd = i
            break
    toWrite.pop(authInd)
    toWrite.pop(authInd)
    
    # Process Category
    authInd = 0
    for i in range(len(toWrite)):
        if "## Category" in toWrite[i]:
            authInd = i
            break
    toWrite.pop(authInd)
    toWrite.pop(authInd)
    # Process Description
    authInd = 0
    for i in range(len(toWrite)):
        if "## Description" in toWrite[i]:
            authInd = i
            break
    toWrite.pop(authInd)
    """
    for i in range(authInd, len(toWrite)):
        if "## Topics" in toWrite[i]:
            break
        toWrite[i] = "> " + toWrite[i]
    """
    for line in toWrite:
        print line,
    toProcess = open(fileToEdit, 'w')
    toProcess.write("".join(toWrite))
    toProcess.close()

baseDir = '.'
for dirName, subdirList, fileList in walklevel(rootDir, 3):
    if dirName.count("/") == 2:
        #print('Found directory: %s' % dirName)
        #print dirName
        year = dirName.split("/")[1][:4]
        #print year
        category = dirName.split("/")[2]
        #print category
        #newName = dirName.split("/")[3].replace(" ", "_")
        #print newName
        dest = baseDir + '/' + year + '/' + category + '/'
        #print dest
        for fileA in fileList:
            print dest + fileA
            print "-"*60
            editFile(dest+fileA)
        try:
            #copy_rename("README.md", newName + ".md", dirName, dest)
            pass
        except IOError:
            pass
