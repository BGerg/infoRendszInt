# infoRendszInt

Készítsen egy alkalmazást, amely 2 kliensből áll. Az első kliens a '/queue/colorQueue'
üzenetsorra pont-pont csatlakozással véletlenszerűen RED, GREEN és BLUE paraméterrel
ellátott üzeneteket küld 1 másodpercenként. Készítsen három MDB-t (üzenet vezérelt bean)
amelyek filterrel a 'RED', 'GREEN' és a 'BLUE' paraméterrel ellátott üzeneteket kapják kizárólag.
Minden 10 megkapott üzenet után az MDB-k a '/queue/colorStatistics' sorra küldenek egy üzenetet,
ami azt jelzi, hogy 10 (adott színű) üzenetet feldolgoztak. Készítsen egy második klienst,
ami a '/queue/colorStatistics' sorrol olvassa a statisztikát és a konzolba kiírja hogy pl.
'10 'RED' messages has been processed'