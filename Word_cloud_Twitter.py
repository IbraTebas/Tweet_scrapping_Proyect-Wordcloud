import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from Word_cleaning import *
from PIL import Image

################### Common words load, file 'common words Spanish.csv needed ###########################################

words = pd.read_csv('common words Spanish.csv')

################################## mask shape for cloud, file 'head.png' needs to be on root  ##########################

mask = np.array(Image.open("head.png"))


################################### Cloud creation ######################################################################

def create_cloud(dictio, user, Tweets_count, today):
    try:
        wordcloud = WordCloud(width=900,height=500, mask=mask,contour_color='#FFFFFF',contour_width=3, max_words=20, font_path='ZingRustDemo-Base.otf', relative_scaling=1,normalize_plurals=False, colormap = 'Pastel1', background_color='black').generate_from_frequencies(dictio)
        plt.figure( figsize=(40,20) )
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title('Las 20 palabras más usadas de @{} \n Tweets analizados:{} - Fecha: {}'.format(user,Tweets_count, today), loc='left', fontsize=40, color = 'rebeccapurple', fontfamily = 'cursive')
        plt.show()
    except:
        pass
    
def nube(dataframe, column, user, Tweets_count, today):
    dictio=count_sent(convert_column_to_string(dataframe[column]))
    clean = clean_common_words(dictio, words)
    clean_final = clean_emojies(clean)
    create_cloud(clean_final, user, Tweets_count, today)
    return dictio

################################# Histogram creation #####################################################################
    
def histogram_frecuencies(dataframe, column, user,number_times, Tweets_count, today):
    dictionary = frecuencia_palabras_columna(dataframe, column)
    dictio = {key:val for key, val in dictionary.items() if val > number_times}
    if len(dictio) == 0:
        dictio = {'No words':0}
    keys = list(dictio.keys())
    values = list(dictio.values())
    #frec=pd.DataFrame.from_dict(frecuencia_palabras_columna(dataframe, column), orient = 'index')
    ax=sns.barplot(x=keys, y=values)
    if "No words" in dictio:
        ax.set_xticklabels(ax.get_xticklabels())
        ax.set_xlabel("Palabras con más de {} apariciones - Usuario: @{} \n Tweets analizados: {} - Fecha: {}".format(number_times, user,Tweets_count, today), fontsize = 12)
        ax.set_ylabel("Número de veces fueron mencionadas", fontsize = 15, loc = 'center')
    else:
        ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
        ax.set_xlabel("Palabras con más de {} apariciones - Usuario: @{} \n Tweets analizados: {} - Fecha: {}".format(number_times, user,Tweets_count, today), fontsize = 12)
        ax.set_ylabel("Número de veces fueron mencionadas", fontsize = 15, loc = 'center')
    return ax, dictio
    