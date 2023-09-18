import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import sys

def process_text(input_text):
    # Initialize an empty list to store the filtered lines
    filtered_lines = []
    lines = input_text.split('\n')

    # Process each line, skipping columns 1, 2, 3, and 5 which
    # are the dates and time.
    for line in lines:
        
        columns = line.strip().split(' ')

        if len(columns) >= 6:
            # Join columns 4 and 6 onwards into a single string
            filtered_content = ' '.join(columns[3:4] + columns[5:])
            tokens = word_tokenize(filtered_content)

            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            tokens = [word for word in tokens if word.lower() not in stop_words]

            characters_to_exclude = [',', ':', '<', '>', "''", 's', "n't", '?']
            tokens = [word for word in tokens if not any(char in word for char in characters_to_exclude)]

            # Remove dates
            tokens = [word for word in tokens if not re.match(r'\d{1,2}/\d{1,2}/\d{2,4}', word)]

            # Append the filtered content to the list
            filtered_lines.append(' '.join(tokens))

    # Join the filtered lines into a single text
    filtered_text = '\n'.join(filtered_lines)

    # Count word frequency using NLTK
    frequency_dist = nltk.FreqDist(word_tokenize(filtered_text))

    # Convert the frequency distribution to a DataFrame
    df = pd.DataFrame.from_dict(frequency_dist, orient='index', columns=['Frequency'])
    df.index.name = 'Word'
    df = df.sort_values('Frequency', ascending=False).reset_index()

    return df
