# htpasswd
Facendo una scansione con `nmap -A 192.168.56.134/80` abbiamo il seguente output:
```
Starting Nmap 7.70 ( https://nmap.org ) at 2021-11-05 20:19 CET
Illegal netmask in "192.168.56.134/80". Assuming /32 (one host)
Nmap scan report for 192.168.56.134
Host is up (0.83s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    nginx 1.8.0
| http-robots.txt: 2 disallowed entries
|_/whatever /.hidden
|_http-server-header: nginx/1.8.0
|_http-title: BornToSec - Web Section
4242/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   1024 c1:03:76:40:29:e8:ab:f6:8a:9f:1c:71:6e:23:e0:58 (DSA)
|   2048 89:95:1a:c3:7c:1b:fc:3c:34:1d:76:d5:c9:fa:86:03 (RSA)
|_  256 09:86:1a:be:13:a5:a1:0c:7f:f7:55:50:ac:7a:c7:1a (ECDSA)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.65 seconds
```
Dunque abbiamo scoperto il percorso `http://192.168.56.134/whatever/` dove all'interno abbiamo il file `htpasswd`
con all'interno
```
root:8621ffdbc5698829397d97767ac13db3
```
La password è cifrata con md5 e cercando su google troviamo la stringa `dragon`, quindi accedendo su `http://192.168.56.134/admin/`
otteniamo la flag:
```
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```