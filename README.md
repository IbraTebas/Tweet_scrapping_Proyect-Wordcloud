
# Tweet extraction and analysis of word frequency -- Spanish version

### Twitter Scrapping Project in Spanish -  It access  the last 100 tweets on the last week from a list of users and process the wordcloud and histogram for word frequency.
### It also saves the tweets after cleaning on a csv file with date for future access or concatenate of several files for same user. 
<br>

### Example of Wordcloud:  


### Example of Histogram: 


### Example of CSVs files saved: 

### Relevant Files: 

Twitter_extractor.py ---> 
                               * Execute and extract last 100 tweets in a the last week if possible
                               * Creates a wordcloud and histogram for the word frequency on those tweets 
                               * Save the Tweets in a correspondent folder under the username with date reference


Word_cleaning.py  ---> Cleaning of punctuation and other symbols (still experiencing issues with " and emojies - 24/04/2022)

Word_cloud_Twitter.py ---> Creates the visualization after cleaning. 

Dataframe_column_to_string.py ---> converts column of Dataframe with text into a string



