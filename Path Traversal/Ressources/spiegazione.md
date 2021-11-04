# Path Traversal
Come riportato su [OWASP](https://owasp.org/www-community/attacks/Path_Traversal) ho provato ad utilizzare `../` per
tornare indietro nella root del server sfruttando la variabile `?page=` e cercando di aprire il file `passwd` contenuto
in `etc` così sono arrivato al seguente url per avere la flag:
```
http://192.168.56.134/?page=../../../../../../../etc/passwd
```