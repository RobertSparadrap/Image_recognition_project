#IMPORT
from keras.models import load_model
from PIL import Image
#from tensorflow.keras.models import load_model
#from tensorflow.keras.models import Sequential as load_model
import numpy as np
import time
import sys




def main():
    modelPath = './trainedModel/moModel.hdf5'
#    imagePath =  './testImage/mushroom.jpg'
    imagePath = sys.argv[1]
    imageSize = (50,50)
    label = ['egg', 'ham', 'mushroom', 'pasta', 'surimi']

    predict(modelPath, imagePath,imageSize, label)


def predict(modelPath,imagePath, imageSize, label):
    start = time.time()

    # Chargement du modele
    print("Chargement du modele :\n")
    model = load_model(modelPath)
    print("\nModel charge.")

    #Chargement de notre image et traitement
    data = []
    img = Image.open(imagePath)
    img.load()
    img = img.resize(size=imageSize)
    img = np.asarray(img) / 255.
    data.append(img)
    data = np.asarray(data)

    #On reshape pour correspondre aux dimensions de notre modele
    # Arg1 : correspond au nombre d'image que on injecte
    # Arg2 : correspond a la largeur de l'image
    # Arg3 : correspond a la hauteur de l'image
    # Arg4 : correspond au nombre de canaux de l'image (1 grayscale, 3 couleurs)
    dimension = data[0].shape

    #Reshape pour passer de 3 a 4 dimension pour notre reseau
    data = data.astype(np.float32).reshape(data.shape[0], dimension[0], dimension[1], dimension[2])

    #On realise une prediction
    prediction = model.predict(data)


    #On recupere le numero de label qui a la plus haut prediction
    maxPredict = np.argmax(prediction)

    #On recupere le mot correspondant a l'indice precedent
    print(label, maxPredict)
    prediction[0] = [prediction[0][1], prediction[0][2], prediction[0][3], prediction[0][4], prediction[0][0]]
    maxPredict -= 1
    print(label, prediction[0])
    word = label[maxPredict]
    pred = prediction[0][maxPredict] * 100.
    end = time.time()



    #On affiche les predictions
    print()
    print('----------')
    print(" Prediction :")
    for i in range(0, len(label)):
        print('     ' + label[i] + ' : ' + "{0:.2f}%".format(prediction[0][i] * 100.))

    print()
    print('RESULTAT : ' + word + ' : ' + "{0:.2f}%".format(pred))
#    print('temps prediction : ' + "{0:.2f}secs".format(end-start))

    print('----------')


if __name__ == "__main__":
    """
    # MAIN
    """
    main()
