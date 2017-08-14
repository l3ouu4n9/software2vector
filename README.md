# Entropy : 
### Usage :
* python entropy.py INPUT_FILE1 INPUT_FILE2 ......
* python entropy_binary.py INPUT_FILE1 INPUT_FILE2 ......
* python entropy2.py INPUT_FILE

### Description :
* Get the entropy into a 256-value vector.

**NOTE :**
Need a file named filetype.py for entropy.py and entropy_binary.py, and it's in a folder named Filetype.
INPUT_FILE must be .bytes file for entropy.py and entropy2.py.
INPUT_FILE must be PE file and not UPX packed for entropy_binary.py.

# Section : 
### Usage :
* python section.py INPUT_FILE
* python section_asm.py INPUT_FILE

### Description :
* Disassemble section content, and output as a 24-value vector.

**NOTE :**
INPUT_FILE must be a PE file for section.py
INPUT_FILE must be a .asm file for section_asm.py

# API : 
### Usage : 
* python api.py INPUT_FILE1 INPUT_FILE2 ......
* python api_binary.py INPUT_FILE1 INPUT_FILE2 ......

### Description : 
* Get the frequency of API functions in the file and output as a 796-value vector.

**NOTE :**
INPUT_FILE must be .asm file for api.py.
INPUT_FILE must be PE file and not UPX packed for api_binary.py.
Need a file named filetype.py for both, and it's in a folder named Filetype.

# Img :
### Usage :
* python img1.py INPUT_FILE
* python img2.py INPUT_FILE

### Description :
* Get the image features through a .bytes file.

**NOTE :**
INPUT_FILE must be .bytes file.

# PEheader : 
### Usage :
* python header.py INPUT_FILE1 INPUT_FILE2 ......

### Description :
* Get the PEheader 256-value vector.

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.
INPUT_FILE must be PE file and not UPX packed.

# ImportTable : 
### Usage :
* python iat.py INPUT_FILE1 INPUT_FILE2 ......

### Description :
* Get PE file's import table in 256-value vector.

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.
INPUT_FILE must be PE file and not UPX packed.

# Register : 
### Usage :
* python register.py INPUT_FILE

### Description :
* Get the frequency of x86 registers. Output a 29-value vector for MODE 0, 37-value vector for MODE 1.
* register.py : main program
* register_obj : the list of x86 registers for MODE 0
* register_ida : the list of x86 registers for MODE 1
* TWO VERSION:
MODE 0: objdump ver. (Input: binary) (PE)
MODE 1: asm file ver. (Input: asm file)

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.

# OpCode : 
### Usage :
* python opcode.py INPUT_FILE

### Description :
* Get the frequency of the first 93 common opcode in malware. Output a 93-value vector.
* opcode.py: main program
* opcode_list: the list of the first 93 common opcode in malware
* TWO VERSION:
MODE 0: objdump ver. (Input: binary) (PE)
MODE 1: asm file ver. (Input: asm file)

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.

# Filetype :
### Description :
* There're lots of function in it, and most of them are used to check the type of a file.

# MD2 : 
### Usage :
* python MD2.py INPUT_FILE

### Description :
* Get the line number of the asm file and the size of file in bytes.
Format : [size, line number]

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.
INPUT_FILE must be .asm file

# MD1 :
### Usage :
* python MD1.py INPUT_FILE

### Description :
* Get the start address from the hexdump file and the size of file in bytes.
Format : [size, address]

**NOTE :**
Need a file named filetype.py, and it's in a folder named Filetype.
INPUT_FILE must be hexdump file.
				

# BytesNGram :
### Usage :
* For 1-D gram :
python extract_1_gram.py INPUT_FILE
* For 2-D gram :
python extract_2_gram.py INPUT_FILE

### Description :
* For extract_1_gram.py :
It takes byte as unit. Count the occurance of each byte, and makes into a 1 x 256 vector.

* For extract_2_gram.py :
It takes consecutive 2 bytes as a pair. Count the occurance of each pair, and makes into a 256 x 256 vector, like a1 2b c3 4d -> (a1, 2b), (2b, c3), (c3, 4d)

**NOTE :**
INPUT_FILE must be .bytes file.
Each line's first bytes will be discarded.

# String : 
### Usage :
* python str.py INPUT_FILE1 INPUT_FILE2

### Description :
* Get the strings in the file which is split by '\n', and put them in 32 bins based on their length. Finally, output as a 32-value vector.

**NOTE :**
If there is a file named opcode.pyc in the same directory, you have to delete it before running.
Need a file named filetype.py, and it's in a folder named Filetype.
INPUT_FILE must be PE file and not UPX packed.

# Miscellaneous : 
### Usage :
* python misc.py INPUT_FILE1 INPUT_FILE2 ......

### Description :
* It will calculate the occurance of keys in each file.
* If the is any tab in front of one of the key, dd, it will not count.

**NOTE :**
INPUT_FILE must be .asm file.

# Symbol : 
### Usage :
* python sym.py INPUT_FILE1 INPUT_FILE2 ......

### Description :
* It will calculate the occurance of symbols ['-', '+', '*', ']', '[', '?', '@'] in each file.

**NOTE :**
INPUT_FILE must be .asm file.

# DataDefine : 
### Usage : 
* python dp.py INPUT_FILE1 INPUT_FILE2 ......

### Description :
* It will calculate the occurance of db, dw, and dd in each file.
* If there is any tab in front of db, dw, or dd, it will not count.

**NOTE :**
INPUT_FILE must be .asm file.

