# Visual Search
Epitech-Edhec Project, Visual search

## Infos

Permet de créer avec Tensorflow et Keras une reconnaissance d'image entre 5 types de nourritures différentes, avec des algorithmes de deep learning.

## Installer les pré-requis

`$ install numpy`
`$ install pillow`
`$ install tqdm`
`$ install keras`
`$ install tensorflow`
`$ install scikit-learn`
`$ install matplotlib`
`$ install pandas`

### Generer les tableaux numpy

`$ python generateNumpyFiles.py`

### Entrainer le model et crée un fichier .hdf5

`$ python trainModel.py`

C'est deux premières commandes sont a lancé si on rajoute de nouveaux données a nos datas. Si on ne rajoute pas de nouvelles datas, ces 2 commendes sont inutiles car ces fichier sont déjà push et présent dans ce GitHub. Il suffit plus qu'a lancer l'IA qui est la commande suivante.

### Lancer l'IA et donner la prédiction 

`$ python autoPredict.py /image path/`

(image path est l'image qu'on donne en paramètres qu'on veux analyser)

## Lancer l'appication

Tous d’abord, allez créer un fichier "node_modules" via la commande:

`$ npm install express`

Puis lancer la commande: `$ node src/main.js`. Cela lancera le serveur, il suffit plus qu'a aller sur le web et taper `http://localhost:3000/imageAI`.

Le programme suivant `generateProposal` est un script qui regarde le résultat de l'IA puis regarde le fichier "fleury_michon.json" où on y touve toutes les recettes. Ce script va nous remplire le fichier suivant "result.json" dont on utilisera pendant le web pour les afficher.
Le script suivant `runIA.sh` est un script qui utilise le `$ python autoPredict.py /image path/` et enregistre un fichier avec le résultat dedans et ensuite il utilise `generateProposal`. Ce script a été créé pour appeler "un seul script" pendant qu'on est sur le web.

Malheureusement, a cause de certains problèmes au Mac. Lorsqu'on envoie la photo dans la barre de recherche, le Mac donne le chemin de la photo "C:\\fakepath\\" qui n'est pas un véritable chemin et le code n’apprécie pas ce faux chemin. Pour régler ce souci, on a décidé de hard code le chemin "/Users/robert/edhec_IA/B-PRO-995-NCE-0-1-edhecepitech-clement1.berard/datasetTest/ham/" ce qui signifie que le dossier dont on a fait la demo ce situe toujours sur le même dossier. Cela signifie que sur un ordinateur autre que le mien, le script ne se lancera jamais. Pour que des autres personnes l’utilisent, il va falloir changer le path a la main dans la ligne 189 du code "src/front.html". Toutes les photos souhaitées ce situent dans le dossier "B-PRO-995-NCE-0-1-edhecepitech-clement1.berard/datasetTest/ham/", il va donc falloir rajouter le chemin manquant.
Mais l'IA lui peut être utiliser par n’importe qui via la commande `$ python autoPredict.py /image path/`, en général les photos testés sont dans le dossier datasetTest.


## Authors

* **Clément Bérard** ([GitHub](https://github.com/Twisterrr) / [LinkedIn](https://www.linkedin.com/in/clementberard/))
* **Robert Harakaly** ([GitHub](https://github.com/RobertSparadrap) / [LinkedIn](https://www.linkedin.com/in/robert-harakaly-3b19391a1/))
