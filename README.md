## urlwatch_standalone
Ce projet était un test pour savoir si l'outil permettait de monitorer les sites modernes (SPA, AJAX).
La réponse est que le module utilié Pyppeteer dans le job Browser fonctionne bien sur des sites JS classiques. Toutefois, il fonctionne pas pour les sites en React par exemple.
De ce fait, le projet a été recyclé pour développer une nouvelle browser avec un autre outil Playwright.

## des tests déjà effectuées (ancien browser)
il arrive à récupérer les changement à un site Apache localhost.
il n'arrive pas sur le site préparé en React.
Tous les waituntil ont été testés

## des tests déjà effectuées (nouveau browser)
Un sites en React a été monté.
Deux jobs ont été créé sur ce site, un avec un bouton, l'autre sans.
Il arrive à récupérer les changements sur les deux.

Ensuite, il a été modifié pour passer un script, il peut être passé en mattant ; après chaque ligne. 

## les commandes
`urlwatch --urls urlwatch/urls.yaml --config urlwatch/urlwatch.yaml --hooks urlwatch/hooks.py`
`urlwatch --gc-cache`
"# test_urlwatch_alone" 
