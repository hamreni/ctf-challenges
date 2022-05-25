
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

*b – 512-byte blocks (this is the default if no suffix is used), 
c – bytes, 
w – two-byte words, 
k – Kilobytes, 
M – Megabytes, 
G – Gigabytes*

## lvl6 
*home was clear so go up to the root* 

    cd /
now can find sg w this:  

    find . -group bandit6 -user bandit7 -size 33c
    lib/dpkg/info/bandit7.password 
 
 
 **password**

 HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

## lvl7 
    find . -name "data.txt" 
    vi ./data.txt

change to command mode in vim
    
    /millionth
 
 
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
until get the ASCII text file data8
 
 
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
    echo '#!/bin/bash' > getpwd.sh
    echo 'cat etc/bandit_pass/bandir24 > /tmp/getpwd/pwd24.txt' >> getpwd.sh
    cp getpwd.sh /var/spool/bandit24
    cat pwd24.txt
 
 
 **password**

 UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## lvl24
    mkdir /tmp/brute 
    vi bf_num_gen.py    
    netcat localhost 30002 < PINs.txt
 
 **password**

 uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

## lvl25

    ssh -i bandit26.sshkey bandit26@localhost

*but bandit26 lock me out immediately :(*
    
    cat /etc/passwd | grep bandit26

*/urs/bin/showtext is the shell entry of bandit26*

    cat /urs/bin/showtext
    man more

*we can get buffer if we minimize the terminal, so more stuck in printing the full msg*

    v
    :r /etc/bandit_pass/bandit26

**password**
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z 

## lvl26
*again, we can take advantage of the fact that the more command is stuck in small screen, so we can set and open a subshell with vi and finally we use the SUID bit*

    v  
    :set shell=/bin/bash
    :shell
    ./bandit27-do /etc/bandit_pass/bandit27

**passworld**
 3ba3118a22e93127a4ed485be72ef5ea

 ## lvl27
    cd /tmp/
    git clone ssh://bandit27-git@localhost/home/bandit27-git/repo new-repo
    cat new-repo/README

**password**
0ef186ac70e04ea33b4c1853d2526fa2

## lvl28
    cd /tmp/
    git clone ssh://bandit28-git@localhost/home/bandit28-git/repo new-repo28
    cat new-repo28/README.md
    git log --oneline
    git diff de2ebe2 c086d11

**password**
bbc96594b4e001778eee9975372716b2

## lvl29
    cd /tmp/
    git clone ssh://bandit29-git@localhost/home/bandit29-git/repo new-repo29
    git branch -r
    git checkout dev
    cat README.md

**password**
5b90576bedb2cc04c86a9e924ce42faf

## lvl30

    cd /tmp/
    git clone ssh://bandit30-git@localhost/home/bandit30-git/repo new-repo30

*nothing interesting found in git log and branches*

    cat .git/packed-refs

*get an additional ref /refs/tags/secret, lets check it*

    git show f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea

**password**
47e603bb428404d265f59c42920d81e5

## lvl 31

    cd /tmp/
    git clone ssh://bandit31-git@localhost/home/bandit31-git/repo new-repo31
    cd new-repo31

*delete \*.txt from .gitignore*

    echo 'May I come in?' > key.txt
    git add .
    git commit -m "add key.txt"
    git push

**password**
56a9bf19c63d650ce78e6ec0354ee45e

## lvl 32
