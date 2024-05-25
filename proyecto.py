import os
import matplotlib.pyplot as plt
from PIL import Image

#directorio donde esttán las imágenes
base_dir = "./imgs"

#creamos una lista que nos permitirá ver la cantidad de imágenes por cada categoría
num_images_per_category = []

#Obtenemos la cantidad de impagenes que hay en cada una de las categorías, las cuales están como folders y vamos iterando para ver la cantidad por folder
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    num_images = len(os.listdir(folder_path))
    num_images_per_category.append(num_images)

#Etiquetas para las categorías, las cuales son las 4 que ya se mencionaron
labels = ["Mild Demented", "Moderate Demented", "Non Demented", "Very Mild Demented"]

#gráfica de distribución para ver la cantidad
plt.figure(figsize=(8, 6))
plt.bar(labels, num_images_per_category, color='skyblue')
plt.xlabel('Categoría')
plt.ylabel('Número de imágenes')
plt.title('Distribución de imágenes por categoría')
plt.show()

#Por último, veremos de manera textual la cantidad de datos que se tienen por categoría para poder hacernos una idea si están balanceadas o desbalanceadas
#pequeño spoiler, no están nada balanceadas
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    num_images = len(os.listdir(folder_path))
    print(f"Número de imágenes en '{folder}':", num_images)


#COMPROBAREMOS EL TAMAÑO DE LAS IMÁGENES


#Volvemos a cargar el directorio donde se encuentran las imágenes, está será la última vez que comentemos esto, de ahora en más cada que se use en el código
#ya no lo vamos a mencionar
base_dir = "./imgs/"

#Creamos una lista donde se va a estar almacenando el tamaño de las imágenes, es decir, largo y ancho
image_sizes = []


#vamos a hacer primero una iteración en cada folder, de nuevo
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    #y ahora vamos a iterar en cada imagen de cada folder, obteniendo la dirección del folder y el nombre de la imágen, realmente el nombre no es muy útil
    #pero la función necesitaba dos parámetros y ps colocamos este para no tener problemas xd
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #una vez que se tenga una imgaen, calculamos el largo y ancho y lo agregamos a la lista creada arriba
        with Image.open(image_path) as img:
            width, height = img.size
            image_sizes.append((width, height))

#Separar los tamaños de ancho y largo, la primera entrada es el ancho de la imagen y la segunda entrada el alto
widths = [size[0] for size in image_sizes]
heights = [size[1] for size in image_sizes]

#para poder ver si hay diferencias entre los tamaños, hacemos una gráfica que nos muestre todos los tamaños de todas las imágenes, pequeño spoiler de nuevo, todas son
#el mismo tamaño, es una muy buena base para empezar
plt.figure(figsize=(10, 6))
plt.scatter(widths, heights, color='skyblue', alpha=0.5)
plt.title('Tamaño de todas las imágenes')
plt.xlabel('Ancho (píxeles)')
plt.ylabel('Alto (píxeles)')
plt.grid(True)
plt.show()


#vamos a recortar todas las imágenes originales, y crear un directorio donde estarán las recortadas, ya que son las que nos interesa conservar para el
#análisis y evaluación del modelo

base_dir = "./imgs"

#En este directorio donde se guardarán las imágenes recortadas, que se llama como el de imgs, pero cropped que significa recortado en inglés
cropped_dir = "./imgs_cropped"
os.makedirs(cropped_dir, exist_ok=True)

#Vamos a seleccionar dos parámetros, crop top y bottom, es decir, recorte por abajo y recorte por arriba, ya que esta es la parte de la radiografía que sobra
crop_top = 16
crop_bottom = 16

#Nuevamente, vamos a iterar por cada folder y cada imagen dentro del folder, y una vez más como en el caso de cargar el directorio, ya no lo vamos a mencionar, porque
#pues este proceso ya se hizo varias veces y es cansado estar comentando a cada rato esto xd
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        #Una vez que ya se abrió la imagen
        with Image.open(image_path) as img:
            #calculamos el tamaño original, el cual es 176 x 208
            width, height = img.size

            #Y ahora vamos a recortar la imagen, todas las imágenes
            img_cropped = img.crop((0, crop_top, width, height - crop_bottom))

            #Guardar la imagen recortada en el nuevo directorio, y posteriormente como estamos iterando, se van a guardar todas y cada una de las imágenes recortadas
            #en este mismo directorio
            cropped_image_path = os.path.join(cropped_dir, folder, image_name)
            os.makedirs(os.path.dirname(cropped_image_path), exist_ok=True)
            img_cropped.save(cropped_image_path)

#todos estos folders de imágenes se encuentran en la carpeta de archivos de google colab :D

"""Vamos a verificar que sí se nos recortó bien las imágenes:"""

#es el mismo código de la primera vez namas con el cambio de agarrar imágenes recortadas jaja

#Volvemos a cargar el directorio donde se encuentran las imágenes, está será la última vez que comentemos esto, de ahora en más cada que se use en el código
#ya no lo vamos a mencionar
cropped_dir = "./imgs_cropped"

#Creamos una lista donde se va a estar almacenando el tamaño de las imágenes, es decir, largo y ancho
cropped_image_sizes = []


#vamos a hacer primero una iteración en cada folder, de nuevo
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(cropped_dir, folder)
    #y ahora vamos a iterar en cada imagen de cada folder, obteniendo la dirección del folder y el nombre de la imágen, realmente el nombre no es muy útil
    #pero la función necesitaba dos parámetros y ps colocamos este para no tener problemas xd
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #una vez que se tenga una imgaen, calculamos el largo y ancho y lo agregamos a la lista creada arriba
        with Image.open(image_path) as img:
            width, height = img.size
            cropped_image_sizes.append((width, height))

#Separar los tamaños de ancho y largo, la primera entrada es el ancho de la imagen y la segunda entrada el alto
widths = [size[0] for size in cropped_image_sizes]
heights = [size[1] for size in cropped_image_sizes]

#para poder ver si hay diferencias entre los tamaños, hacemos una gráfica que nos muestre todos los tamaños de todas las imágenes, pequeño spoiler de nuevo, todas son
#el mismo tamaño, es una muy buena base para empezar
plt.figure(figsize=(10, 6))
plt.scatter(widths, heights, color='skyblue', alpha=0.5)
plt.title('Tamaño de todas las imágenes ya recortadas')
plt.xlabel('Ancho (píxeles)')
plt.ylabel('Alto (píxeles)')
plt.grid(True)
plt.show()

"""Y como podemos notar, efectivamente se tiene el mismo tamaño, por lo que hasta el momento nuestro preprocesamiento va bien.

### Patrón de colores en las imágenes

Necesitamos ver si todas las imágenes tienen una tonalidad parecida, puesto que esto nos va a permitir tener un proceso de clasificación más coherente y que pueda ser más confiable para este tipo de problemas sobre clasificar radiografías, ya que la confianza en el modelo debe ser lo mejor posible, aunque claro, al hacer esto vamos a perder variabilidad en los patrones de color si queremos ingresar otros datos, pero usualmente las radiografías siempre suelen tener el mismo tono, por lo que creemos esto será una buena idea e implementación.

Esto lo haremos usando el sistema de tonalidad de grises, ya que nuestras radiografías están en tonos de grises, donde se usa un solo canal de color para representar la intensidad, yendo ed 0 a 255, donde el 0 es negro absoluto y 255 blanco absoluto, además tener todo en esta escala ayuda a no cargar tanto costo computacional.
"""

#esto no lo vamos a comentar, es donde están las imágenes recortadas
cropped_dir = "./imgs_cropped"

#lista donde vamos a almacenar la tonalidad en escala de grises para cada imagen
average_brightness_values = []

#Iterar sobre las carpetas, de nuevo, no haremos mucho comentario
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(cropped_dir, folder)
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #para cada una de las imágenes
        with Image.open(image_path) as img:
            #Convertir la imagen a escala de grises
            img_gray = img.convert('L')

            #Y ahora vamos a calcular la tonalidad promedio de los píxeles en escala de grises, para obtener el brillo
            brightness = img_gray.getdata()
            average_brightness = sum(brightness) / len(brightness)
            average_brightness_values.append(average_brightness)

#Grafica
plt.figure(figsize=(10, 6))
plt.hist(average_brightness_values, bins=50, color='skyblue', edgecolor='black')
plt.title('Tonalidad de las Imágenes Recortadas')
plt.xlabel('Tonalidad Promedio')
plt.ylabel('Número de Imágenes')
plt.grid(True)
plt.show()

"""Podemos ver que la mayoría de las imágenes tiene un tono de grises parecido, cerca del 80 en el valor de escala de grises, no vamos a hacer modificaciones para tener todas del mismo tono, puesto que estaríamos quitando mucha generalidad al modelo, dejándolo así podemos tener un poco más de variabilidad en los datos que nos puede ayudar a obtener mejores resultados.

## Elección del modelo

Ya tenemos los datos con su primera preprocesación, la general que es para poder implementarlo a cualquier tipo de modelo, pero bien, ahora la pregunta es, ¿Qué modelo usar?

Bueno, sabemos de primera mano que por la cantidad de datos y etiquetas lo mejor a usar podrían ser Redes Neuronales, usando deeplearning, pero este proceso es muy tardado y conlleva alto costo computacional, es por esto que veremos si podemos escoger otro modelo que sea más simple en implementar y ver si tiene buenos resultados.

Proponemos el SVM, este modelo es eficaz cuando se tienen grandes dimensiones de datos, en este caso tenemos imágenes, donde las dimensiones son los pixeles y tenemos 176x176, es por esto que hemos optado por usar este modelo, más aún haremos como tal dos modelos, primero uno donde probaremos el modelo sin realizar una disminución de dimensiones, y luego uno donde applicaremos PCA para ver si hay alguna mejora, para cada uno haremos ajustes de hiperparámetros necesarios que nos permitan obtener el mejor modelo.
"""

### Normalización de las imágenes ya procesadas


#Descargar la librería scikit-image para poder normalizar los pixeles
from skimage import io, transform
import numpy as np

#directorio
cropped_dir = "/content/ia-2024/imgs_cropped"

#Otra lista más, ahora para almacenar las imágenes recortadas
normalized_images = []

#iteracion en todas las imagenes en todos los folders
folders = ["MildDemented", "ModerateDemented", "NonDemented", "VeryMildDemented"]
for folder in folders:
    folder_path = os.path.join(cropped_dir, folder)
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        #vamos a cargar todas las imágenes que vamos teniendo
        img = io.imread(image_path)

        #y normalizamos los pixeles de cada una de ellas, restando los pixeles originales, menos la media entre la desviación estándar de los pixeles en la imagen
        img_normalized = (img - np.mean(img)) / np.std(img)

        #vamos añadiendo cada imagen normalizada a nuestra lista
        normalized_images.append(img_normalized)

### Aplanamiento de Imágenes:

#Nuestras imágenes, al ser imágenes, tienen muchas dimensiones, debemos de realizar un aplanado que nos permitirá tener las imágenes como conjuntos de características bidimensionales, que es la entrada que espera nuestro modelo de SVM, para solucionar esto tenemos que hacer un aplanamiento de imágenes, para que puedan ser tratadas como vectores de características.

#Hacemos una lista donde se irán almacenando las imágenes aplanadas
flattened_images = []

#hacemos otra itreacion, pero en este caso iteramos sobre todas las imágenes que ya fueron normalizadas, estas son las que vamos a aplanar
for img_normalized in normalized_images:
    #Aplanamos la imagen y la vamos agregando a la lista creada para almacenar imágenes aplanadas, usamos una función .flatten de la librería
    flattened_images.append(img_normalized.flatten())

#convertimos la lista donde se guardaron las imagenes aplanadas a un tipo de array numpy
X_flattened = np.array(flattened_images)

#verificar las dimensiones del array resultante
print("Cantidad de imagenes a la izquierda, longitug del vector unidimensional que representa cada imagen", X_flattened.shape)

"""Una vez que tenemos las imágenes ya con todo el procesamiento completo, vamos a la parte de crear el modelo.

### División en conjunto de entrenamiento y prueba

Finalmente tenemos todos los datos ya procesados (al menos lo necesario para esta sección), así que ahora necesitamos dividir los datos en conjunto de entrenamiento y prueba.

El problema es que como vimos, tenemos un severo desbalanceo en los datos para la cantidad de las clases, recordemos cuantos datos teníamos:

- Número de imágenes en 'MildDemented': 717

- Número de imágenes en 'ModerateDemented': 52

- Número de imágenes en 'NonDemented': 2000

- Número de imágenes en 'VeryMildDemented': 1792

Es por esto que vamos a realizar una división de los datos de manera estratificada, lo que nos va a grantizar que la proporción en la división en cada clase se mantenga para ambos conjuntos de train y test de manera equilibrada, porque si no hacemos esto, al realizar la división tomando 70% de train, puede ser que todas nuestras imágenes de ModerateDemented sean seleccionadas para el Train, lo que haría que no tengamos forma de probarlas, o puede pasar al revés, por esto lo haremos de manera estratificada.

Tomaremos 70% de los datos para el conjunto de train y 30% para el test, esto porque hay una característica donde sólo tenemos 52 datos, tomar esta división nos permite obetener una cantidad considerable de datos para cada uno de los conjuntos.

Así como hicimos en el proyecto 2, lo que haremos es tomar 3 semillas: 170119, 2024 y 123456789, para observar si la división de los datos afecta la precisión del modelo, calcularemos el "mejor" modelo en base a la métrica de accuracy, usando un SVM con kernel lineal, kernel polinomial y Gaussiana, es decir, tendremos 9 combinaciones al final del cual sólo quedará una.
"""

#vamos a iterar sobre las clases que tenemos y cargar las imágenes que ya hemos preprocesado anteriormente

from sklearn.model_selection import train_test_split

#La lista de equitetas que tenemos para cada clase, las cuales ya hemos mencionado varias veces
labels = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

#Otras dos listas más, en la lista X se guardan las imágenes procesadas, mientras que en la y se encuentran las etiquetas de cada una de las imágenes
X = []
y = []

#Otra iteración, en este caso vamos a iterar por cada etiqueta en el conjunto de etiquetas
for label in labels:
    #buscamos el directorio donde se encuentran las imágenes y obtenemos el nombre de su etiqueta
    folder_path = os.path.join(cropped_dir, label)
    #y ya que lo tenemos, iteramos sober todas las imágenes de la categoría actual
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #cargamos ahora la imagen que ya fue normalizada
        img_normalized = io.imread(image_path)
        #Añadimos la imagen a la lista X
        X.append(img_normalized)
        #y su etiqueta a la lista y
        y.append(label)

#Convertimos nuestras listas a un array de numpy para poder realizar bien las divisiones y los demás procedimientos
X = np.array(X)
y = np.array(y)

#hacemos una división estratificada para el conjunto de train y test, en este caso usamos la semilla 170119 para observar si la división de los datos afecta
#la efectividad del modelo
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#vamos a ver cuantos datos de cada catacterística se quedaron en cada uno de los conjuntos de los datos
#creamos una función que nos permitirá CONTAR el número de datos que hay en cada una de las etiquetas

print("\tCantidad de datos por conjuntos para la primer semilla: 170119")
print("\n")
def contar(y):
    clases, recuentos = np.unique(y, return_counts=True)
    for clase, recuento in zip(clases, recuentos):
        print(f"Cantidad de Datos en '{clase}': {recuento}")

#Calculamos el conjunto de datos de cada característica para el conjunto de train
print("Conjunto de entrenamiento:")
contar(y_train)

#y ahora lo mismo, pero para test
print("\nConjunto de prueba:")
contar(y_test)

#vamos a iterar sobre las clases que tenemos y cargar las imágenes que ya hemos preprocesado anteriormente

from sklearn.model_selection import train_test_split

#La lista de equitetas que tenemos para cada clase, las cuales ya hemos mencionado varias veces
labels = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

#Otras dos listas más, en la lista X se guardan las imágenes procesadas, mientras que en la y se encuentran las etiquetas de cada una de las imágenes
X = []
y = []

#Otra iteración, en este caso vamos a iterar por cada etiqueta en el conjunto de etiquetas
for label in labels:
    #buscamos el directorio donde se encuentran las imágenes y obtenemos el nombre de su etiqueta
    folder_path = os.path.join(cropped_dir, label)
    #y ya que lo tenemos, iteramos sober todas las imágenes de la categoría actual
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #cargamos ahora la imagen que ya fue normalizada
        img_normalized = io.imread(image_path)
        #Añadimos la imagen a la lista X
        X.append(img_normalized)
        #y su etiqueta a la lista y
        y.append(label)

#Convertimos nuestras listas a un array de numpy para poder realizar bien las divisiones y los demás procedimientos
X = np.array(X)
y = np.array(y)

#hacemos una división estratificada para el conjunto de train y test, en este caso usamos la semilla 170119 para observar si la división de los datos afecta
#la efectividad del modelo
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=2024, stratify=y)

#vamos a ver cuantos datos de cada catacterística se quedaron en cada uno de los conjuntos de los datos
#creamos una función que nos permitirá CONTAR el número de datos que hay en cada una de las etiquetas

print("\tCantidad de datos por conjuntos para la primer semilla: 2024")
print("\n")
def contar(y):
    clases, recuentos = np.unique(y, return_counts=True)
    for clase, recuento in zip(clases, recuentos):
        print(f"Cantidad de Datos en '{clase}': {recuento}")

#Calculamos el conjunto de datos de cada característica para el conjunto de train
print("Conjunto de entrenamiento:")
contar(y_train)

#y ahora lo mismo, pero para test
print("\nConjunto de prueba:")
contar(y_test)

#vamos a iterar sobre las clases que tenemos y cargar las imágenes que ya hemos preprocesado anteriormente

from sklearn.model_selection import train_test_split

#La lista de equitetas que tenemos para cada clase, las cuales ya hemos mencionado varias veces
labels = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']

#Otras dos listas más, en la lista X se guardan las imágenes procesadas, mientras que en la y se encuentran las etiquetas de cada una de las imágenes
X = []
y = []

#Otra iteración, en este caso vamos a iterar por cada etiqueta en el conjunto de etiquetas
for label in labels:
    #buscamos el directorio donde se encuentran las imágenes y obtenemos el nombre de su etiqueta
    folder_path = os.path.join(cropped_dir, label)
    #y ya que lo tenemos, iteramos sober todas las imágenes de la categoría actual
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        #cargamos ahora la imagen que ya fue normalizada
        img_normalized = io.imread(image_path)
        #Añadimos la imagen a la lista X
        X.append(img_normalized)
        #y su etiqueta a la lista y
        y.append(label)

#Convertimos nuestras listas a un array de numpy para poder realizar bien las divisiones y los demás procedimientos
X = np.array(X)
y = np.array(y)

#hacemos una división estratificada para el conjunto de train y test, en este caso usamos la semilla 170119 para observar si la división de los datos afecta
#la efectividad del modelo
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=123456789, stratify=y)

#vamos a ver cuantos datos de cada catacterística se quedaron en cada uno de los conjuntos de los datos
#creamos una función que nos permitirá CONTAR el número de datos que hay en cada una de las etiquetas

print("\tCantidad de datos por conjuntos para la primer semilla: 123456789")
print("\n")
def contar(y):
    clases, recuentos = np.unique(y, return_counts=True)
    for clase, recuento in zip(clases, recuentos):
        print(f"Cantidad de Datos en '{clase}': {recuento}")

#Calculamos el conjunto de datos de cada característica para el conjunto de train
print("Conjunto de entrenamiento:")
contar(y_train)

#y ahora lo mismo, pero para test
print("\nConjunto de prueba:")
contar(y_test)


"""Pues, se tienen la misma cantidad de datos para cada una de las semillas, el problema es cuales serán los datos que se mantienen en cada categoría según la semilla, en este caso no prestaremos mucha atención y únicamente tomaremos la semilla de 170119 para evitar costo computacional y con esta vamos a ajustar el modelo con cada uno de los kernels para ver cual es mejor, posteriormente ajustar hiperparámetros, ver si no está sobreajustado y por último, la matriz de confusión para ver la eficacia del modelo en lo que nos interesa, poder clasificar bien la etapa de Alzheimer temprano para poder avisarle a los pacientes.

### Ajustando el modelo SVM con Kernel Lineal sin PCA

Vamos a implementar este modelo SVM, usando la semilla de reproducibilidad 170119 y sin hacer uso de PCA, con las imágenes recortadas y normalizadas
"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#obtenemos de nuevo la división de los datos, con la semilla y la cantidad de datos ya establecida, y recordemos que está estratificada
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#creamos un clasificador con kernel lineal, sin más,no hay mucho quer decir aquí más de usaremos SVC de la librería sklear
svm_classifier = SVC(kernel='linear', random_state=170119)

#Hacemos un fit del modelo usando los datos que se tomaron para el conjunto de entrenamiento
svm_classifier.fit(X_train, y_train)

#Realizamos unas predicciones con lo que sería el conjunto de imagenes de test, sin las etiquetas
y_pred = svm_classifier.predict(X_test)

#para calcular las métricas hacemos una comparación entre las etiquetas predichas y las reales, en el caso de precision, f1 y recall usamos weighted que calcula la métrica para
#cada clase y luego hace una media
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Accuracy del modelo SVM con kernel lineal, semilla 170119, división estratificada:", accuracy)
print("Precision del modelo:", precision)
print("Recall del modelo:", recall)
print("F1 score del modelo:", f1)

"""Podemos ver que se tiene una accuracy imponente, se tiene cerca de un 97%, quizás el modelo esté sobreajustado, pero eso ya lo veremos más adelante en caso de optar por usar este modelo, de momento veamos la matriz de confusión generada:"""

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#calculamos la matriz de confusión comparando las y predichas por las y reales, y ver que tan bien clasfica las categorías
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Etiquetas predecidas')
plt.ylabel('Etiquetas reales')
plt.title('Matriz de Confusión para el Kernel Lineal')
plt.show()

"""Podemos ver que la categoría que más nos interesa, tiene una buena precisión, que es la de VeryMild, puesto que casi todas se clasifican correctamente y son pocas las que tienen una mala clasificación, aunque esto indica que de 538 personas, a 4 se les dirá que no tienen alzheimer lo que puede ser un problema, es mejor clasificar estas personas como si tuvieran un Alzheimer alto a decirles que no lo tengan, puesto que si les decimos que tienen Alzheimer las personas irán a empezar tratamientos y les harán mejores evaluaciones, pero decirles que no lo tienen, puede hacer que se confien y que no comiencen los tratamientos a tiempo.

También podemos ver que la categoría de ModerateDemented tiene un 100% de clasificación, lo cual es extraño, seguramente nuestro modelo sí esté sobreajustado, lo vamos a ver si es que decidimos este modelo con kernel lineal.

### Ajustando un modelo SVM con kernel polinomial y sin PCA

Ahora veremos para el kernel polinomial, tomaremos el parámetro de regularización C = 1, en caso de decidir este modelo veremos si es necesario ajustarlo para tener una mayor o menor regularización, tomamos el valor de uno ya que se considera un valor "moderado", y tomamos el polinomio de grado 3.
"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#obtenemos de nuevo la división de los datos, con la semilla y la cantidad de datos ya establecida, y recordemos que está estratificada
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#creamos un clasificador con kernel polinomial, sin más,no hay mucho quer decir aquí más de usaremos SVC de la librería sklearn, y agregamos los parámetros que son distintos
#en este caso el degree y C
svm_classifier = SVC(kernel='poly', degree = 3, C=1, random_state=170119)

#Hacemos un fit del modelo usando los datos que se tomaron para el conjunto de entrenamiento
svm_classifier.fit(X_train, y_train)

#Realizamos unas predicciones con lo que sería el conjunto de imagenes de test, sin las etiquetas
y_pred = svm_classifier.predict(X_test)

#para calcular las métricas hacemos una comparación entre las etiquetas predichas y las reales, en el caso de precision, f1 y recall usamos weighted que calcula la métrica para
#cada clase y luego hace una media
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Precision del modelo:", precision)
print("Recall del modelo:", recall)
print("F1 score del modelo:", f1)
print("Accuracy del modelo SVM con kernel polinomial de 3 grados y con C=1, semilla 170119, divisón estratificada:", accuracy)

#corrimos este código una primera vez y ahora lo silenciamos porque vimos que no tiene buenos resultados y el modelo de kernel lineal es mejor

"""Este modelo tiene un 85% de accuracy.

Ahora veamos la matriz de confusión:
"""

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#calculamos la matriz de confusión comparando las y predichas por las y reales, y ver que tan bien clasfica las categorías
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Etiquetas predecidas')
plt.ylabel('Etiquetas reales')
plt.title('Matriz de Confusión para el Kernel Polinomial de grado 3')
plt.show()

"""Podemos ver que no sólo el rendimiento según la medida Accuracy es menor al usar un kernel polinomial, si no que también la categoría que nos interesa clasificar de manera adecuada tiene más problemas, es por esto que no consideramos buena idea mantener este modelo, si bien podemos ajustar hiperparámetros para buscar mejores resultados, esta no será nuestra opción principal.

### Modelo SVM con kernel Gaussiano y sin PCA

Por último, el modelo SVM con kernel Gaussiano, tomando el valor de la gamma como un inverso de la cantidad de características, y tomando de nuevo C = 1, nuevamente mencionamos que en caso de optar por este modelo, vamos a modificar los hiperparámetros más adelante, estos fueron tomados porque es algo así como el valor "común" que se suele usar.
"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#obtenemos de nuevo la división de los datos, con la semilla y la cantidad de datos ya establecida, y recordemos que está estratificada
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#creamos un clasificador con kernel gaussiano, sin más,no hay mucho quer decir aquí más de usaremos SVC de la librería sklearn, y agregamos los parámetros que son distintos
#en este caso el degree y scale
svm_classifier = SVC(kernel='rbf', gamma = 'scale', C=1, random_state=170119)

#Hacemos un fit del modelo usando los datos que se tomaron para el conjunto de entrenamiento
svm_classifier.fit(X_train, y_train)

#Realizamos unas predicciones con lo que sería el conjunto de imagenes de test, sin las etiquetas
y_pred = svm_classifier.predict(X_test)

#para calcular las métricas hacemos una comparación entre las etiquetas predichas y las reales, en el caso de precision, f1 y recall usamos weighted que calcula la métrica para
#cada clase y luego hace una media
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Precision del modelo:", precision)
print("Recall del modelo:", recall)
print("F1 score del modelo:", f1)
print("Accuracy del modelo SVM con kernel Gaussiano, con gamma = scale y con C=1, semilla 170119, divisón estratificada:", accuracy)

"""Este modelo sólo tuvo 75% de accuracy, siendo el peor de los tres, aún así no son tan malos resultados.

Ahora veamos la matriz de confusión de nuestra última prueba de kernel
"""

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#calculamos la matriz de confusión comparando las y predichas por las y reales, y ver que tan bien clasfica las categorías
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Etiquetas predecidas')
plt.ylabel('Etiquetas reales')
plt.title('Matriz de Confusión para el Kernel Gaussiano')
plt.show()

#corrimos este código una primera vez y ahora lo silenciamos porque vimos que no tiene buenos resultados y el modelo de kernel lineal es mejor

"""Este modelo resultó peor para clasificar lo que queríamos, es por esto que después de ver todos los modelos, optaremos por un kernel lineal y ajustar los hiperparámetros, ya que presentó mejores resultados y además, tardó menos tiempo en compilación, lo que es mejor

## Ajuste de Hiperparámetros

En esta sección vamos a evaluar el modelo SVM con kernel lineal y ver cuales son los mejores hiperparámetros que podemos usar, vamos a hacer una búsqueda de malla, definida como:

    'C': [0.1, 1, 10, 100],
    'class_weight': [None, 'balanced']

Donde C es el parámetro de regularización, y class_weight son los pesos, vamos a probar el modelo cambiando cada valor de C y los tipos de pesos, para ver cual tiene aún mejores resultados, además de tomar 5 de CV, teniendo así un total de 40 fits a probar hasta encontrar el mejor modelo.
"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

#obtenemos de nuevo la división de los datos, con la semilla y la cantidad de datos ya establecida, y recordemos que está estratificada
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#creamos un clasificador con kernel lineal, sin más,no hay mucho quer decir aquí más de usaremos SVC de la librería sklear
svm_classifier = SVC(kernel='linear', random_state=170119)

#Hacemos un fit del modelo usando los datos que se tomaron para el conjunto de entrenamiento
svm_classifier.fit(X_train, y_train)

#Realizamos unas predicciones con lo que sería el conjunto de imagenes de test, sin las etiquetas
y_pred = svm_classifier.predict(X_test)

#para calcular la accuracy hacemos una comparación entre las etiquetas predichas y las reales
accuracy = accuracy_score(y_test, y_pred)

#######VAMOS A HACER UNA BÚSQUEDA DE MALLA, PARA VER CUALES SON LOS MEJORES HIPERPARÁMETROS A USAR EN NUESTRO MODELO, VAMOS A CONSIDERAR CAMBIAR EL
#PARÁMETRO DE REGULARIZACIÓN TOMANDO VALORES DE .01, 1, 10 Y 100, TOMAREMOS LOS PESOS COMO NO MODIFICARLOS O TENER PESOS BALANCEADOS EN EL MODELO,
#ESTO PUEDE AYUDAR DEBIDO A LA NATURALEZA DESBALACEADA DE LOS DATOS, ESTO LO ANALIZARÁ EL PROGRAMA Y VERÁ SI SI ES MEJOR O NO

#Definimos la malla en la que haremos las pruebas, en total serán 4x2x5, es decir, 100 fits, ya que tomaremos 5 de CV
param_grid = {
    'C': [0.1, 1, 10, 100],
    'class_weight': [None, 'balanced']
}

#creamos una instancia de clasificador svm con un kernel lineal, que es el que vimos con mejores resultados
svm_classifier = SVC(kernel='linear', random_state=170119)

#Ahora cargamos el GridSearch, que hará los fits del modelo según los parámetros de la malla y se irá calculando la accuracy para cada combinación que tengamos
#elegiremos el mejor modelo según está métrica
grid_search = GridSearchCV(svm_classifier, param_grid, cv=5, scoring='accuracy')
#Ahora vamos haciendo los fits
grid_search.fit(X_train, y_train)

#Vamos a obtener lo que el programa considera los mejores hiperparámetros para el modelo
best_params = grid_search.best_params_
print("Mejores hiperparámetros para el modelo SVM con kernel Lineal:", best_params)

#Y obtenemos la accuracy del mejor modelo
#para calcular las métricas hacemos una comparación entre las etiquetas predichas y las reales, en el caso de precision, f1 y recall usamos weighted que calcula la métrica para
#cada clase y luego hace una media
best_model = grid_search.best_estimator_
best_accuracy = best_model.score(X_test, y_test)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Precision del modelo:", precision)
print("Recall del modelo:", recall)
print("F1 score del modelo:", f1)
print("Accuracy del modelo con los mejores hiperparámetros, kernel lineal con semilla 170119:", best_accuracy)


#Este código está silenciado porque si usamos la versión gratis de colab dice que tarda 83 horas en cargar xd
#Así que lo compilamos en nuestro entorno local

"""El código de arriba nos da el siguiente resultado:

Mejores hiperparámetros para el modelo SVM con kernel Lineal:

    'C': 0.1, 'class_weight': None
    Accuracy del modelo con los mejores hiperparámetros: 0.9817384952520087

La accuracy del modelo ahora con un valor de regularización igual a 0.1 tiene un valor del 98.17%, es decir, mejoró en alrededor de un 1%, lo cual es muy bueno puesto que queremos una efectividad casi del 100% para esta clasificación, aunque claro está, debemos ver que no haya un sobreajuste en nuestro modelo, pero veamos como se ve la matriz de confusión.
"""

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#obtenemos de nuevo la división de los datos, con la semilla y la cantidad de datos ya establecida, y recordemos que está estratificada
X_train, X_test, y_train, y_test = train_test_split(X_flattened, y, test_size=0.3, random_state=170119, stratify=y)

#creamos un clasificador con kernel lineal, sin más,no hay mucho quer decir aquí más de usaremos SVC de la librería sklear
svmejor = SVC(kernel='linear', C = 0.1, class_weight = None, random_state=170119)

#Hacemos un fit del modelo usando los datos que se tomaron para el conjunto de entrenamiento
svmejor.fit(X_train, y_train)

#Realizamos unas predicciones con lo que sería el conjunto de imagenes de test, sin las etiquetas
y_pred = svmejor.predict(X_test)


#calcular la matriz de confusión, comparando los y reales y las etiquetas que predijo el modelo
conf_matrix_manual = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_manual, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.xlabel('Etiquetas Predichas')
plt.ylabel('Etiquetas Reales')
plt.title('Matriz de Confusión del mejor modelo')
plt.show()

"""Podemos ver que si tiene mejores clasificaciones que el modelo antes de ajustar hiperparámetros, sobretodo en la parte de NonDemented, puede tener mejor clasificación para decirles a las personas que no tienen la enfermedad, y en general parece presentar mejores resultados, pero si notamos en la categoría de VeryMild, la que nos interesa, podemos ver que se presentan problemas, puesto que tiene una cantidad poco mayor de datos mal clasificados, donde categoriza 13 de los datos de VeryMild como NonDemented, mientras que en el modelo antes de ajustarlos sólo hubo 4 datos mal clasificados, es por este hecho que decidimos mejor conservar únicamente el modelo con kernel lineal, puesto que tiene mejor clasificación para resolver el problema al que nos enfrentamos.
