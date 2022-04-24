
# Tweet extraction and analysis of word frequency -- Spanish version

![AVATAR](https://user-images.githubusercontent.com/35322625/164973338-842a456b-ccbe-4ee1-a2f5-058a41bdfa66.png)

### Twitter Scrapping Project in Spanish -  It access  the last 100 tweets on the last week from a list of users and process the wordcloud and histogram for word frequency.
### It also saves the tweets after cleaning on a csv file with date for future access or concatenate of several files for same user. 
<br>

### Example of Wordcloud:  

![Figure 2022-04-24 165318 (14)](https://user-images.githubusercontent.com/35322625/164973357-552e3299-8972-4b4a-ad44-793449d17c36.png)

### Example of Histogram: 

![Figure 2022-04-24 165318 (89)](https://user-images.githubusercontent.com/35322625/164973403-1922ff4c-fc2c-4e98-8d3f-5b7242914cac.png)

### Example of CSVs files saved: 
<br>
[CSV_with_mentions](https://github.com/IbraTebas/Tweet_scrapping/files/8549518/BautiGilC-2022-04-22_with_mentions.csv) <br>
[CSV_no_mentions.csv](https://github.com/IbraTebas/Tweet_scrapping/files/8549519/BautiGilC-2022-04-23_no_mentions.csv)

### Relevant Files: 

Twitter_extractor.py ---> 
                               * Execute and extract last 100 tweets in a the last week if possible
                               * Creates a wordcloud and histogram for the word frequency on those tweets 
                               * Save the Tweets in a correspondent folder under the username with date reference


Word_cleaning.py  ---> Cleaning of punctuation and other symbols (still experiencing issues with " and emojies - 24/04/2022)

Word_cloud_Twitter.py ---> Creates the visualization after cleaning. 

Dataframe_column_to_string.py ---> converts column of Dataframe with text into a string



