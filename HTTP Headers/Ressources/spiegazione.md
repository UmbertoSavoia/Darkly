# HTTP Headers
Come descritto nei commenti della pagina html all'indirizzo 
`http://192.168.56.134/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`
```html
<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
è bastato cambiare lo User-Agent con `ft_bornToSec` e il Referer con `https://www.nsa.gov/`:
```
curl -H 'User-Agent: ft_bornToSec' -H 'Referer: https://www.nsa.gov/' 'http://192.168.56.134/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' | grep flag
```
```
The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```
