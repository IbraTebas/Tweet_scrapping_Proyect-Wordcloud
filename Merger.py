# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:42:09 2022

@author: ibrah
"""

import glob
import pandas as pd
import Word_cloud_Twitter as wct
from datetime import date

##List of users
users = ["gbianchi404", "BautiGilC",'PedroBordaberry','Luisaheber','pdasilve', 'ElsaLevrero', 'veronica_alonso', 'Pablo_Mieres','el-RusoMachenaud','EdgardoNovick','opepasquet','Dip_ConradoRod','SergioAbreu_Uy','JMCarzolio', 'Tabareviera','AndreaTabarez', 'diegoleuco','edufeiok', 'AldoLema_uy','dasilvailiana', 'BancoMundialLAC','PatriciaJMadrid','leohaberkorn','LeoPereyra5','gonza_ferreira', 'OliveraPdu','fcomesana', 'SoleGaston', 'carinanovarese','luciabrocal','LongobardiM','Mauri_RepettoUy','BaroniGonzalo','JBarriosBove','HoracioVaroli', 'Jovenes40', "gbianchi404",'MatiasTM71', 'ctapia1982','Ni_Martinelli','IreneMoreiraUy', 'natiroba', 'conradoh47','PatoBullrich','Fedecas','loliponcedeleon', 'MercedesVigilUY','Minterioruy', 'compresidencia','midesuy','MSPUruguay','JuanSartoriUY', 'SenadoUy','MEC_Uruguay', 'Parlamento_UY', 'ANEP_Uruguay','NeyCastillo9','leosarro','ferresrodrigo','Alfredolara29', 'ACTUALIDADPress','pfvierci','IdiazAyuso', 'OrsiYamandu', 'TelenocheUy','PNACIONAL','beatrizargimon',"camboue",'RobertSilva1971','GuidoManiniRios','JavierGarcia_Uy', 'igalvar71','MartinLemaUy','grazianopascale', 'GustavoZubia', 'RominaPesce25', 'lauraraffo', 'MonicaBatlle4']
# users_high = ['TelenocheUy', 'MonicaBatlle4', 'Alfredolara29', 'PatoBullrich']  
# Get CSV files list from a folder
LISTA = [] 
for user in users:
    path = './DATA/'+ user
    csv_files = glob.glob(path + "/*.csv")
    for file in csv_files:
        if 'no_mentions' not in file:
            csv_files.remove(file)
    
                
        
       # Read each CSV file into DataFrame
       # This creates a list of dataframes
    df_list= [pd.read_csv(file) for file in csv_files]

        
    #     # Concatenate all DataFrames
    try:
        big_df = pd.concat(df_list, ignore_index=True) 
        big_df = big_df.iloc[: , 1:]
        big_df = big_df.drop_duplicates()
          
        wct.nube(big_df, 'text', user, len(big_df)-1, date.today())
        wct.histogram_frecuencies(big_df, 'text', user, 20, len(big_df)-1,date.today() )
    except:
        pass

# for user in users_high:
#     path = './DATA/'+ user
#     csv_files = glob.glob(path + "/*.csv")
        
#        # Read each CSV file into DataFrame
#        # This creates a list of dataframes
#     df_list = (pd.read_csv(file, index_col=[0]) for file in csv_files)
        
#         # Concatenate all DataFrames
#     try:
#         big_df   = pd.concat(df_list, ignore_index=True) 
#         big_df = big_df.drop_duplicates()
#         wct.nube(big_df, 'text', user, len(big_df)-1, date.today())
#         wct.histogram_frecuencies(big_df, 'text', user, 50, len(big_df)-1,date.today() )
#     except:
#         pass     