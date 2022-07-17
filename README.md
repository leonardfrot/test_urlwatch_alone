# urlwatch_standalone
## Pré-requis
Le site en React doit être allumé https://github.com/leonardfrot/test_scraping_frontend.
Il est possible d'ajouter le site en Apache, il faut juste l'ajouter dans urls.yaml https://github.com/leonardfrot/test_ajax.
## Démarrer le monitoring
`docker-compose up`

## Fonctions
### Tester et entrainer la conteneurisation
Comme Playwright devait être ajouté à Jestime, ce projet a aidé à trouver la bonne configuration Docker avec Playwright et Urlwatch.
### Tester les browsers
Ce projet a permis de tester le browser nativement intégré à Urlwatch avec Pyppeteer, mais également à développer le nouveau avec Playwright.
#### Résultat browser natif
- Il permet de récupérer la différence sur le site Apache.
- Il ne permet pas de récupérer la différence sur le site en React.
#### Résultat nouveau browser
- Il permet de récupérer la différence sur le site Apache et React
## Synthèse
Ce projet a permis de comprendre que le problème de l'outil venait de Pyppeteer. <br/>
De ce fait, il fallait créer un nouveau browser avec Playwright.
