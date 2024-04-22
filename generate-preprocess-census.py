import pandas as pd
import numpy as np
import os
pd.set_option('future.no_silent_downcasting', True)

datasetsDir = 'Datasets/census/data'
outputDir = 'Datasets/census/data-clean'

def processDataset(datasetPath, outputPath):
    df = pd.read_csv(datasetPath, low_memory=False)

    df = df.iloc[:,:-1] # Drop extra column
    df.columns = df.iloc[0] # Make header first data row
    df = df[1:] # Get rid of first header row

    # Get percentage and zip columns
    df = df.filter(regex='^(Geography|Geographic Area Name|Percent!!)')

    # Replace nulls
    df.replace("(X)", np.nan, inplace=True)
    df = df.dropna(axis=1, how='all')

    # Drop columns
    df = df.loc[:, ~df.columns.str.contains('SEX AND AGE')]
    df = df.loc[:, ~df.columns.str.contains('CITIZEN')]

    # Get wanted columns
    searchColumns = [
        'Geography',
        'Percent!!RACE!!Total population!!One race!!White',
        'Percent!!RACE!!Total population!!One race!!Black or African American',
        'Percent!!RACE!!Total population!!One race!!American Indian and Alaska Native',
        'Percent!!RACE!!Total population!!One race!!Asian',
        'Percent!!RACE!!Total population!!One race!!Native Hawaiian and Other Pacific Islander',
        'Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
    ]
    toFilterColumns = []
    for column in searchColumns:
        if column in df.columns:
            toFilterColumns.append(column)
        elif column.replace('Total population!!', '') in df.columns:
            toFilterColumns.append(column.replace('Total population!!', ''))
        elif column.replace('Percent!!', 'Percent Estimate!!') in df.columns:
            toFilterColumns.append(column.replace('Percent!!', 'Percent Estimate!!'))
        else:
            raise KeyError('Failed to find: ' + column)
    byGroup = df[toFilterColumns]

    # Strip zip
    byGroup.loc[:, 'Geography'] = byGroup['Geography'].str[-5:]

    # Rename columns
    originalColumns = byGroup.columns
    mapping = {}
    for column in originalColumns:
        lastWord = column.split('!!')[-1]
        lastWord = lastWord.split(' (')[0]
        wordList = lastWord.split(' ')
        upperWords = []
        for word in wordList:
            upperWords.append(word.upper())
        newWord = '_'.join(upperWords)

        mapping[column] = newWord
    finalDataset = byGroup.rename(columns=mapping)

    finalDataset.to_csv(outputPath, index=False)

datasetsToProcess = os.listdir(datasetsDir)
for dataset in datasetsToProcess:
    thisDatasetYear = dataset.split('.')[0].split('ACSDP5Y')[1]

    thisDatasetPath = datasetsDir + '/' + dataset
    thisDatasetOutputPath = outputDir + '/' + 'census-' + str(thisDatasetYear) + '.csv'

    print(f'For dataset: {dataset}')
    print(f'Input Path: {thisDatasetPath}')
    print(f'Output Path: {thisDatasetOutputPath}')
    print('Processing...')
    try:
        processDataset(thisDatasetPath, thisDatasetOutputPath)
        print('Processed!')
    except Exception as e:
        print('Failed to process...')
        print(e)
    print()