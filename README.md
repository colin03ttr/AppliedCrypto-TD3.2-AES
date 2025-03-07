# Applied Cryptography - TD 3.2 - AES ECB attack

Let's try to find the flag from the source code !

The source code tells us that the variable ``message`` is formed using 3 strings :
 1. a 16 bytes AES (as a block)
 2. the input from user (blocks depending on the length)
 3. the flag


When we send an empty input, here is the result cipher :
```
xX+NDjg0X9tmJLobdQv9k3p8OAaf7GXlB81oPjRoqhA=
```
When we send a block of 16 known bytes like ``AAAAAAAAAAAAAAAA``, the result cipher is :
```
xX+NDjg0X9tmJLobdQv9k9VR6ytFTCy5JN+wlNbxGzR6fDgGn+xl5QfNaD40aKoQ
```
We can easily see that the first part of the cipher is the same.
```
xX+NDjg0X9tmJLobdQv9k 3p8OAaf7GXlB81oPjRoqhA=
xX+NDjg0X9tmJLobdQv9k 9VR6ytFTCy5JN+wlNbxGzR6fDgGn+xl5QfNaD40aKoQ
```
