# Applied Cryptography - TD 3.2 - AES ECB attack

## Understand the code
Let's try to find the flag from the source code !

The source code tells us that the variable ``message`` is formed using 3 strings :
 1. a 16 bytes AES (as a block)
 2. the input from user (blocks depending on the length)
 3. the flag

```
message = <16randombytes><myinput><flag>
```
Then, the message is padded depending on the length of the input, to make the number of bytes a multiple of 16.

```
message = <16randombytes><myinput><flag><00000>
```
It is then encrypted by the AES function by block of 16bytes :
```
cipher = ENC[<16randombytes>] + ENC[<16next>] + ENC[<16last>]
```
It then all encoded in base64.

We can see the first block is never changed, and we can see that in the outputs.
```
output_1 = "xX+NDjg0X9tmJLobdQv9k3p8OAaf7GXlB81oPjRoqhA="
output_2 = "xX+NDjg0X9tmJLobdQv9k9VR6ytFTCy5JN+wlNbxGzR6fDgGn+xl5QfNaD40aKoQ"
```

## Exploit the padding
We can now use the padding, to guess the characters of the flag.

Let's input 15 '1's so that the first character of the flag is part of the second block.
Let's say the flag is something like **flag{secret}**.

```
message = <16randombytes>111111111111111flag{secret}0000
```
separated in blocks :
```
message = <16randombytes> 111111111111111f lag{secret}0000
```
and now we can input 15 '**1**'s + **one character**. We try every character and compare the cipher block with the one of the flags first character.
```
111111111111111     (cipher to match)
111111111111111a
111111111111111b
111111111111111c
etc.
```
python3 ./solve.py 
Current flag: <
Current flag: <f
Current flag: <fl
Current flag: <fla
Current flag: <flag
Current flag: <flag>
Current flag: <flag>0
Current flag: <flag>00
Current flag: <flag>000
Current flag: <flag>0000
Current flag: <flag>00000
Current flag: <flag>000000
Current flag: <flag>0000000
Current flag: <flag>00000000
Current flag: <flag>000000000
```
I wrote the exploit in Python in the [solve.py](./solve.py) file

Here is the result output :
```

----

I also used [this](https://exploit-notes.hdks.org/exploit/cryptography/algorithm/aes-ecb-padding-attack/) article/writeups to learn on AES ECB attack byte-a-time.