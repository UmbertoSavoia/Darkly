# BruteForce
Scrivendo un semplice programma in python (inserito in questa cartella) e sfruttando una lista di password trovata su 
[skullsecurity](https://wiki.skullsecurity.org/index.php/Passwords) arriviamo alla password dell'utente `admin`:
```
http://192.168.56.134/?page=signin&username=admin&password=shadow&Login=Login#
********************
Username: Admin
Password: shadow
********************
```
e facendo il login abbiamo la flag:
```
B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2
```