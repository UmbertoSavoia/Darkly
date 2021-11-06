# XSS Feedback
Inizialmente sono riuscito ad applicare un vero attacco XSS nel campo `Name` scrivendo il seguente testo:
```
</td><script type="text/&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;">alert("Ciao")</script>
```
Ma non è servito, basta semplicemente scrivere la parola `script` e otteniamo la flag:
```
0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E
```
