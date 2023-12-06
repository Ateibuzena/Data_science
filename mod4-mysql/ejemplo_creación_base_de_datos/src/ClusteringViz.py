import os
from tqdm.notebook import tqdm

#análisis y visualización
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#from matplotlib.ticker import FixedLocator, FixedFormatter
import seaborn as sns
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import silhouette_visualizer

#Procesamiento de datos
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from umap import UMAP

# Modelos
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples

#otros
import warnings
warnings.filterwarnings('ignore')
    
    
class ClusteringViz():    
    
    def plot_corr(df:pd.DataFrame, save:bool=False)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub


            Función que muestra la matriz de correlación de un dataframe recibido como parámetro a través de un heatmap,
            limitada a la triangular inferior


            Parametros:
            -----------

               - df: Recibe un pandas DataFrame al que posteriormente le calcularemos su matriz de correlación.
               - save: Booleano por defecto False, si le pasamos True podremos guardar el gráfico para utilizarlo posteriormente en 
                       informes, si no exite la carpeta de destino podremos crear una nueva

            Return:
            -------

                    La función no devuelve nada, muestra por pantalla un gráfico en forma de heatmap, con los valores de correlación de
                los datos proporcionados.

        '''

        plt.figure(figsize=(15,10))

        sns.set(style='white')

        mask=np.triu(np.ones_like(df.corr(), dtype=bool))

        cmap=sns.diverging_palette(0, 10, as_cmap=True)


        sns.heatmap(df.corr(),
                   mask=mask,
                  cmap=cmap,
                  center=0,
                  square=True,
                  annot=True,
                  linewidths=0.5,
                  cbar_kws={'shrink': 0.5})

        if save:
            title = input('Introduce un nombre para el grafico')
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def plot_productos_x_cluster(df:pd.DataFrame, cluster:int, save:bool=False)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub


            Función que crea un gráfico en base al número de productos contratados por cliente en un cluster determinado.

            Parametros:
            -----------

               - df: Pandas DataFrame
               - cluster: int, número del cluster por el que queremos filtrar el dataframe
               - save: bool, guarda el gráfico en la ruta determinada, si no existe la carpeta de destino, pedirá crear una nueva

            Return:
            -------

                No devuelve nada, muestra el gráfico por pantalla.


        '''

        plt.figure(figsize=(15,10))
        sns.barplot(y=df[df.cluster==cluster]['familia_captacion'].value_counts().index, x=df[df.cluster==cluster]['familia_captacion'].value_counts().values)
        plt.title(f'Contrataciones por tipo de producto cluster {cluster}, total clientes {df[df.cluster==cluster].shape[0]}')

        if save:
            title = f'Contrataciones por tipo de producto cluster {cluster}, total clientes {df[df.cluster==cluster].shape[0]}'
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def plot_total_productos_x_cluster(df:pd.DataFrame, cluster:int, hue:str = None, save:bool=False)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub

            Función que devuelve un gráfico en el que muestra el recuento de productos que tiene contratado un cliente y los agrupa 
            por número de productos contratados.


            Parametros:
            -----------

               - df: Pandas DataFrame
               - cluster: int, número del cluster por el que queremos filtrar el dataframe
               - hue: str, columna categorica normalmente por la que queremos agrupar los resultados de nuestro gráfico
               - save: bool, guarda el gráfico en la ruta determinada, si no existe la carpeta de destino, pedirá crear una nueva

            Return:
            -------

                No devuelve nada, muestra el gráfico por pantalla.


        '''

        plt.figure(figsize=(15,10))
        sns.countplot(data=df[df.cluster==cluster], y='total_productos', hue=hue)
        plt.title(f'Cantidad de productos contratados por cliente, cluster {cluster}')

        if save:
            title = f'Cantidad de productos contratados por cliente, cluster {cluster}'
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def cal_angle(x1:int,x2:int,y1:float,y2:float)->float:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 24/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub


            Función que devuelve el angulo entre dos vectores


            Parametros:
            -----------

               - x1: int, valor en el eje x del punto 1
               - x2: int, valor en el eje x del punto 2
               - y1: float, valor en el eje y del punto 1
               - y2: float, valor en el eje y del punto 2

            Return:
            -------

                Devuelve el ángulo formado por dos vectores, a partir de las coordenadas en los ejes x,y de dos puntos.

        '''

        x = np.array([x1, x2])
        y = np.array([y1, y2])

        lx = np.sqrt(x.dot(x))
        ly = np.sqrt(y.dot(y))

        cos_angle = x.dot(y)/(lx*ly)

        angle = np.arccos(cos_angle)

        angle2 = angle*360/2/np.pi

        return angle2

    def plot_elbow(inertias:list, start:int=2, end:int=10,annot:bool=False,save:bool=False)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub

            Función que muestra por pantalla el gráfico obtenido a partir de las inercias obtenidas del modelo Kmeans, y marca el que 
            debería ser el punto óptimo de clusters.

            Parametros:
            -----------

                - inertias: list, lista obtenida a partir de las inercias obtenidas por entrenar un modelo Kmeans
                - start: int, punto de inicio para generar el plot, por defecto 2.
                - end: int, punto para finalizar el rango del plot, por defecto 10.
                - annot: bool, muestra una flecha apuntando al punto óptimo de k clusters en base a diferencia del valor de inercias
                - save: bool, parámetro para guardar el gráfico generado con la función.


            Return:
            -------

                 No devuelve nada, muestra el gráfico por pantalla.   

        '''

        #dif = [inertias[i]-inertias[i+1] for i in range(len(inertias)-1)]
        #max_el = max(dif)

        an = [ClusteringViz.cal_angle(i+start,i+(start+1), inertias[i],inertias[i+1]) for i,e in enumerate(inertias) if i<(end-3)]

        dif_an = [180-(90-an[i]-(90-an[i+1])) for i in range(len(an)-1)]
        max_ch = [dif_an[i+1]-dif_an[i] for i in range(len(dif_an)-1)]
        max_ = max_ch.index(min(max_ch))

        #for i in range(len(dif)):
        #    if dif[i] == max_el:
        #       opt = i

        plt.figure(figsize=(15, 10))
        plt.plot(range(start, end), inertias, "bo-")
        plt.xlabel("$k$", fontsize=14)
        plt.ylabel("Inertia", fontsize=14)
        if annot:
            plt.annotate(f'K óptimo = {max_+start+1}, inertia = {round(inertias[max_],2)}',
                         xy=(max_+start+1, inertias[max_+1]),
                         xytext=(0.4, 0.75),
                         textcoords='figure fraction',
                         fontsize=16,
                         arrowprops=dict(facecolor='red', shrink=0.1)
                        )
        if save:
            title = input('Introduce un nombre para el grafico')
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def plot_silhouette_scores(silhouette_scores:list, start:int=2, end:int=10, save:bool=False)->None: 

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub



            Parametros:
            -----------

                - silhouette_scores: list, lista de silohuette scores obtenida del modelo Kmeans
                - start: int, punto de inicio para generar el plot, por defecto 2.
                - end: int, punto para finalizar el rango del plot, por defecto 10.
                - save: bool, parámetro para guardar el gráfico generado con la función.

            Return:
            -------

                - No devuelve nada, muestra el gráfico por pantalla.  


        '''

        min_ = min(silhouette_scores)-0.2
        max_ = max(silhouette_scores)+0.2
        plt.figure(figsize=(15, 10))
        plt.plot(range(start, end), silhouette_scores, "bo-")
        plt.xlabel("$k$", fontsize=14)
        plt.ylabel("Silhouette score", fontsize=14)
        plt.axis([start-0.2, end+0.2, min_, max_])
        plt.title('Silhouette Scores')

        if save:
            title = input('Introduce un nombre para el grafico')
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def plot_KElbowVisualizer(df:pd.DataFrame, ks:tuple=(2,15))->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub


            Función similar para obtener el valor optimo de clusters a través de la técnica del elbow a partir de la distancia entre las 
            inercias del modelo, usa la libreria yellowbrick, y muestra las inercias frente al tiempo de calculo de las predicciones en base 
            al número de clusters, y en base a estas dos métricas indica el número óptimo de clusters.

            Parametros:
            -----------

                - df: pandas DataFrame, datos que recibirá el modelo para calcular los clusters
                - ks: tuple, rango de clusters a entrenar para ajustar el modelo


            Return:
            -------

                - No devuelve nada, muestra el gráfico por pantalla.


        '''

        plt.figure(figsize=(15,10))
        visual=KElbowVisualizer(KMeans(random_state=42), k=ks)
        visual.fit(df)

        visual.show();


    def plot_silhouette_visualizer(df:pd.DataFrame, k:int)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub

            Función para generar un gráfico de shiloutte, en el que muestra como se distribuyen los datos en cada cluster a partir
            del número de clusters pasado como parámetro. 

            Parametros:
            -----------
                - df: pandas DataFrame, datos que recibirá el modelo para calcular los clusters
                - k: int, numero de clusters a entrenar para ajustar el modelo
                - save: bool, parámetro para guardar el gráfico.


            Return:
            -------
                - No devuelve nada, muestra el gráfico por pantalla.

        '''
        plt.figure(figsize=(15,10))
        visual = silhouette_visualizer(KMeans(k, random_state=42), df, colors='yellowbrick')
        visual.show();

    def get_umap(data:pd.DataFrame, n:int):

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 19/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub

            Función para reducir las dimensiones del dataframe pasado como parámetro, y reducirlas a un número dado. 
            UMAP son las siglas de Uniform Manifold Approximation and Projection for Dimension Reduction, mas info en
            !['UMAP'](https://umap-learn.readthedocs.io/en/latest/index.html)

            Parametros:
            -----------

                - data: pandas DataFrame
                - n: int, numero de columnas a las que queremos reducir nuestros datos


            Return:
            -------

                Devuelve un pandas DataFrame con los embeddins obtenidos después de aplicar la reducción de dimensiones.

        '''

        umap=UMAP(n_components=n,random_state=42)
        emb=umap.fit_transform(data)

        return pd.DataFrame(emb, columns=[f'emb_{i+1}' for i in range(n)])

    def plot_clusters(df:pd.DataFrame, model, centroids:bool=True, palette:str='Spectral', save:bool=False)->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 20/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub

            Función para imprimir la dispersión de los datos recibidos como parámetro y mostrar su distribución entre los diferentes
            clusters propuestos por el modelo, marcando su posición en el gráfico

            Parametros:
            -----------

                - df: Pandas dataframe tratado con la función get_umap perteneciente a esta clase.
                - model: Modelo utilizado para la creación de los clusters, su principal función es poder obtener los centroides para 
                        poder mostrarlos en el gráfico.
                - centroids: Por defecto True, si está activado, obtendrá los centroides calculados por el modelo y posteriormente los 
                            mostrará en el gráfico
                - palette: Paleta de colores para mostrar los clusters, por defecto 'Spectral'
                - save: Permite guardar el gráfico en un archivo para poder utilizarlo posteriormente, si no exite el directorio por defecto
                        pedíra crear uno nuevo

            Return:
            -------

                    La función no devuelve ningún valor, imprime el gráfico de dispersión junto con los centroides y su división por 
                clusters por pantalla.

        '''
        if centroids:
            centroids = pd.DataFrame(model.cluster_centers_, columns=['x','y'])
            plt.figure(figsize=(15,10))
            sns.scatterplot(data=df, x='emb_1', y='emb_2', hue='cluster', palette= palette)

            plt.scatter(data=centroids, x='x', y='y',
                        marker='+', s=30, linewidths=30,
                        color='limegreen', zorder=11, alpha=1)
            for i in range(len(centroids)):
                plt.annotate(f'Cluster {i}', (centroids['x'][i]-0.03,centroids['y'][i]+0.05), zorder=13, color='red')
        else:
            plt.figure(figsize=(15,10))
            sns.scatterplot(data=df, x='emb_1', y='emb_2', hue='cluster', palette= palette)
        plt.title(f'Distribución de clientes por Cluster en {model}')

        title = f'Distribución de clientes por Cluster en {model}'

        if save:
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();

    def countplot_cluster(df:pd.DataFrame, cluster:int ,col:str, hue:str, save:bool=False )->None:

        '''
            Autor: Enrique Revuelta Garcia
            Fecha: 20/11/2022
            email: enrique.revuelta@enriquerevueltagarcia.com
            LinkedIn: https://www.linkedin.com/in/kike-rev/
            github: https://github.com/Gobuub


            Función que muestra un countplot de una columna determinada de un dataframe, filtrado por el número
            de cluster y agrupando los datos por una columna categórica dada.

            Parametros:
            -----------

                - df: pandas DataFrame, datos que queremos usar para realizar el gráfico.
                - cluster: int, cluster por que el queremos filtrar nuestros datos.
                - col: str, columna categórica sobre la que queremos realizar el countplot.
                - hue: str, columna categórica que queremos usar para agrupar los datos y mostrarlos separados en +
                      el gráfico divididos por colores.
                - save: bool, parámetro para guardar el gráfico.


            Return:
            -------

                La función no devuelve nada, muestra el gráfico por pantalla en base a los parámetros dados.

        '''

        plt.figure(figsize=(15,10))
        sns.countplot(data=df[df.cluster==cluster], x=col, hue=hue)
        plt.title(f'Cluster {cluster}: {col} por {hue}')

        if save:
            title = f'Cluster {cluster}: {col} por {hue}'
            try:
                plt.savefig(f'graphics/{title}.png')
            except:
                destino = input('No exite la carpeta de destino, introduce un nombre para la carpeta de destino: ')
                os.mkdir(destino)
                plt.savefig(f'{destino}/{title}.png')

        plt.show();