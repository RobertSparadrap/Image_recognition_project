# IMPORT
import os
from PIL import Image
import numpy as np
from tqdm import tqdm

"""
# Classe permettant de convertir notre dataset d'images en tableaux Numpy
"""


def launchConversion(pathData, pathNumpy, resizeImg, imgSize):
    """
    # Permet de lancer la conversion des images en tableau numpy
    :param pathData: chemin ou sont les
    :param pathNumpy:
    :param resizeImg:
    :param imgSize:
    """

    #Pour chaque classe
    for ingredientClasse in os.listdir(pathData):
        pathIngredient = pathData + '/' + ingredientClasse
        imgs = []

        #Pour chaque image d'une classe, on la charge, resize et transforme en tableau
        for imgIngredient in tqdm(os.listdir(pathIngredient), "Conversion de la classe : '{}'".format(ingredientClasse)):
            imgIngredientPath = pathIngredient + '/' + imgIngredient
#           print(imgIngredientPath)
            img = Image.open(imgIngredientPath).convert('RGB')
            img.load()
            if resizeImg == True:
                img = img.resize(size=imgSize)

            data = np.asarray(img, dtype=np.float32)
            imgs.append(data)

        #Converti les gradients de pixels (allant de 0 à 255) vers des gradients compris entre 0 et 1
#        print(imgs)
#        try:
        print("GOOD", imgIngredientPath)
        imgs = np.asarray(imgs) / 255.
#            np.save(pathNumpy + '/' + ingredientClasse + '.npy', imgs)
#        except:
#            print("PROBLEME", imgIngredientPath)
#            continue

#        try:
#            print("GOOD FILE", ingredientClasse)
#            imgs = np.asarray(imgs) / 255.
        np.save(pathNumpy + '/ ' + ingredientClasse + '.npy', imgs)
#        except:
#            print("COUCOU", print(imgIngredientPath))
#            continue

        #Enregistre une classe entiere en un fichier numpy
#        np.save(pathNumpy + '/ ' + ingredientClasse + '.npy', imgs)


def main():
    """
    # Fonction main
    """

    pathNumpy = './numpy'
    pathData = './dataset'
    resizeImg = True
    imgSize = (50, 50)
    launchConversion(pathData, pathNumpy, resizeImg, imgSize)


if __name__ == '__main__':
    """
    # MAIN
    """
    main()

