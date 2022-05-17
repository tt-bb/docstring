# Convertisseur code couleur HEX en RGB 

![Facile](https://img.shields.io/badge/-Facile-success)

## Énoncé

Dans cet exercice vous devez créer une fonction convertir_hex_en_rgb qui prend en paramètre une chaîne de caractères correspondant à un code couleur hexadécimal (HEX). La fonction doit être capable de renvoyer le résultat de la conversion hexadécimal en une nuance RGB (Red / Green / Blue) sous la forme d’un tuple.

Un code couleur hexadécimal commence toujours par un hashtag (#) puis 6 caractères compris dans la base 16. Chaque ensemble de 2 caractères forment une nuance de couleur, les deux premiers pour le rouge, les deux suivants pour le vert puis les deux derniers pour le bleu.


## Exemples d’utilisation

```python
>>> convertir_hex_en_rgb("#FF00FF")
(255, 0, 255)

>>> convertir_hex_en_rgb("#99CC33")
(153, 204, 51)
```
