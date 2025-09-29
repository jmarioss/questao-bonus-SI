import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def extrair_caracteristicas(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (100, 100))  
    media_cor = img.mean(axis=(0,1))          
    desvio_cor = img.std(axis=(0,1))         
    return np.concatenate([media_cor, desvio_cor])  

X = []
y = []

X.append(extrair_caracteristicas("folhas/planta-saudavel-1.jpg")); y.append(0)
X.append(extrair_caracteristicas("folhas/planta-saudavel-2.jpg")); y.append(0)
X.append(extrair_caracteristicas("folhas/planta-saudavel-3.jpg")); y.append(0)
X.append(extrair_caracteristicas("folhas/planta-saudavel-4.jpg")); y.append(0)

X.append(extrair_caracteristicas("folhas/planta-doente-1.jpg")); y.append(1)
X.append(extrair_caracteristicas("folhas/planta-doente-2.jpg")); y.append(1)
X.append(extrair_caracteristicas("folhas/planta-doente-3.jpg")); y.append(1)
X.append(extrair_caracteristicas("folhas/planta-doente-4.jpg")); y.append(1)

clf = RandomForestClassifier()
clf.fit(X, y)

nova_folha = extrair_caracteristicas("folhas/folha-teste-2.jpg")
resultado = clf.predict([nova_folha])[0]

print("Resultado:", "Saudável" if resultado == 0 else "Doente")
