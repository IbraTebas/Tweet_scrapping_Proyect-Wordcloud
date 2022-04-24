# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 23:00:59 2022

@author: Tebas
"""
import tweepy
import config
import pandas as pd
from datetime import date
import re 
from Word_cloud_Twitter import *
import os

########################## Date to be used when presenting results and storing files #############################
today = date.today()

############################ load of client, 'config.py' needed on root ##########################################
client = tweepy.Client(bearer_token=config.bearer_token)

################## list of users to scrap without the '@' symbol, case sensitive. ################################

#users = ["BautiGilC",'PedroBordaberry','Luisaheber','pdasilve', 'ElsaLevrero', 'veronica_alonso', 'Pablo_Mieres','elRusoMachenaud','EdgardoNovick','opepasquet','Dip_ConradoRod','SergioAbreu_Uy','JMCarzolio', 'Tabareviera','AndreaTabarez', 'diegoleuco','edufeiok', 'AldoLema_uy','dasilvailiana', 'BancoMundialLAC','PatriciaJMadrid','leohaberkorn','LeoPereyra5','gonza_ferreira', 'OliveraPdu','fcomesana', 'SoleGaston', 'carinanovarese','luciabrocal','LongobardiM','Mauri_RepettoUy','BaroniGonzalo','JBarriosBove','HoracioVaroli', 'Jovenes40', "gbianchi404",'MatiasTM71', 'ctapia1982','Ni_Martinelli','IreneMoreiraUy', 'natiroba', 'conradoh47','PatoBullrich','Fedecas','loliponcedeleon', 'MercedesVigilUY','Minterioruy', 'compresidencia','midesuy','MSPUruguay','JuanSartoriUY', 'SenadoUy','MEC_Uruguay', 'Parlamento_UY', 'ANEP_Uruguay','NeyCastillo9','leosarro','ferresrodrigo','Alfredolara29', 'ACTUALIDADPress','pfvierci','IdiazAyuso', 'OrsiYamandu', 'TelenocheUy','PNACIONAL','beatrizargimon',"camboue",'RobertSilva1971','GuidoManiniRios','JavierGarcia_Uy', 'igalvar71','MartinLemaUy','grazianopascale', "GustavoZubia", "RominaPesce25", 'lauraraffo', "MonicaBatlle4"]
users = ["Parlamento_UY"]
################################################ Extractor ###############################################################
 
for user in users:
    path = 'D:\DataScience\GitHub\Tweetpol\DATA\{}'.format(user)
    if not os.path.exists(path):
        os.mkdir(path)
    query = 'from:' + ' {} '.format(user) +  ' -is:retweet'
    response = client.search_recent_tweets(query=query, max_results=100, media_fields=['preview_image_url'], tweet_fields=['id', 'text', 'author_id', 'created_at', 'public_metrics', 'attachments'], expansions=['attachments.media_keys'])  #tweet_fields=['created_at', 'public_metrics']
          
    listed = []
     
    if response.data is not None :
        for tweet in response.data:
            if tweet.attachments != None:
                tw = [tweet.author_id, tweet.id, tweet.created_at, tweet.text, tweet.public_metrics, "https://twitter.com/i/web/status/{}".format(tweet.id), tweet.attachments] 
                listed = listed + [tw]
            else:
                tw = [tweet.author_id, tweet.id, tweet.created_at, tweet.text, tweet.public_metrics, "https://twitter.com/i/web/status/{}".format(tweet.id), float("NaN")] 
                listed = listed + [tw]
      
        df = pd.DataFrame(listed, columns=['author_id', 'tweet_id', 'time', 'text', 'metrics', 'tweet_url', 'images'])        
            
        #Saving dataframe with mentions.
        df.to_csv(os.path.join(path, "{}-{}_with_mentions.csv".format(user, today)))
            
        # Cleaning user mentions
        df2=df.replace(regex=r"(?:\@|https?\://)\S+",value='')
        df2['text'] = df2['text'].str.strip()
            
        #saving clean dataframe
        df2.to_csv(os.path.join(path, "{}-{}_no_mentions.csv".format(user, today)))
           
            ################ Shows plots for only latest  week #######
        Tweets_count = len(listed)    
        nube(df2, 'text', user,Tweets_count, today)
        histogram_frecuencies(df2, 'text', user,4, Tweets_count, today)
    else:
        pass
   
   

