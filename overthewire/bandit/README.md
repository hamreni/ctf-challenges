
# [The Bandit wargame](https://overthewire.org/wargames/bandit/)



## lvl0
using ssh to login

    ssh bandit0@bandit.labs.overthewire.org -p 2220
    cat readme


 
 **password**

boJ9jbbUNNfktd78OOpsqOltutMc3MY1


## lvl1 
    cat ./- 

 
 **password**

CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

## lvl2 
    cat ./spaces\ in\ this\ filename 
 
 
 **password**

 UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

## lvl3 
    cd inhere/  ls -a   cat ./.hidden 
 
 
 **password**

 pIwrPrtPN36QITSp3EQaw936yaFoFgAB

## lvl4 
files are not human-readables 
need conversion

    hexdump -C inhere/* -file07 seems psw 
 
 
 **password**

 koReBOKuIDDepwhWk7jZC0RTdopnAYKh

## lvl5 
    find -readable -not -executable -size 1033c 
 
 
 **password**

 DXjZPULLxYr17uwoI01bNLQbtFemEgo7

*b – 512-byte blocks (this is the default if no suffix is used)
c – bytes
w – two-byte words
k – Kilobytes
M – Megabytes
G – Gigabytes*

## lvl6 
home was clear so go up to the root 

    cd /
now can find sg w this:  

    find . -group bandit6 -user bandit7 -size 33c -
    lib/dpkg/info/bandit7.password 
 
 
 **password**

 HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

## lvl7 
    find . -name "data.txt" 
    vi ./data.txt -

change to command mode in vim
    
    /millionth -
 
 
 **password**

 cvX2JJa4CFALtqS87jk27qwqGhBM9plV

## lvl8 
    cat data.txt | sort | uniq -u 
 
 
 **password**

 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

## lvl9
    xxd data.txt | grep -n "=="| cut -d : -f 1 | tail -1
    xxd data.txt | sed '1013,1015!d' 
 
 
 **password**

 truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

## lvl10
    base64 -d data.txt 
 
 
 **password**

 IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

## lvl11
    cat data.txt | tr '[A-Z]' '[N-ZA-O]' | tr '[a-z]' '[n-za-o]' 
 
 
 **password**

 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

## lvl12
use file, mv and compression (tar/gzip/bzip2) commads
until get the ASCII text file data8 -
 
 
 **password**

 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

## lvl13
*wsl: chmod don't work on the mount*
    
    scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
    chmod 600 sshkey.private
    ssh -i /tmp/pem_key.pem bandit14@bandit.labs.overthewire.org -p 2220
    cat /etc/bandit_pass/bandit14 
 
 
 **password**

 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

## lvl14
    bandit14@bandit:~$ nc localhost 30000
and send bandit14's password
 
 
 **password**

 BfMYroe26WYalil77FoDi9qh59eK5xNr

## lvl15
    bandit15@bandit:~$ openssl s_client -connect localhost:30001 

and send bandit15's password
 
 
 **password**

 cluFn7wTiGryunymYOu4RcffSxQluehd

## lvl16
    nc -zvn 127.0.0.1 31000-32000
    echo cluFn7wTiGryunymYOu4RcffSxQluehd | openssl s_client -quiet -connect localhost:31790
copy the printed key
    
    touch /tmp/private.key
    nano /tmp/private.key
insert the key
    
    cd /tmp
    chmod 600 private.key
    ssh -i private.key bandit17@localhost
    cat /etc/bandit_pass/bandit17 
 
 
 **password**

 xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

## lvl17
    bandit17@bandit:~$ cat passwords.old | diff passwords.new
 
 
 **password**

 kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

## lvl18 
    ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash   
    cat readme

*command after the ssh executes before the fw takes me out*
 
 
 **password**

 IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

## lvl19
    ./bandit20-do cat /etc/bandit_pass/bandit20
 
 
 **password**

 GbKksEFF4yrVs6il55v6gwY5aVje5f0j

## lvl20 
*two terminal is needed!*

    T1: nc -lp 4000
    T2: ./suconnect 4000
    T1: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
 
 **password**

 gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

## lvl21 
*read files step-by-step*

    cat /etc/cron.d/cronjob_bandit22 
    cat /usr/bin/cronjob_bandit22.sh  
    cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
 
 **password**

 Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

## lvl22 
*understand how the mytarget variable created*

    cat /usr/bin/cronjob_bandit23.sh
    echo I am user bandit23 | md5sum | cut -d ' ' -f 1
    cat /tmp/8ca319486bfbbc3663ea0fbe81326349
 
 
 **password**

 jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

## lvl23 
*don't forget give execution rights! ..blocked ls is very annoying*
    
    cat /usr/bin/cronjob_bandit24.sh
    mkdir /tmp/getpwd
    chmod 777 getpwd
    echo '
    #!/bin/bash' > getpwd.sh
    echo 'cat etc/bandit_pass/bandir24 > /tmp/getpwd/pwd24.txt' >> getpwd.sh
    cp getpwd.sh /var/spool/bandit24
    cat pwd24.txt -
 
 
 **password**

 UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## lvl24
    mkdir /tmp/brute 
    vi bf_num_gen.py    
    netcat localhost 30002 < PINs.txt
 
 **password**

 uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

## lvl25