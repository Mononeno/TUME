import pandas as pd

#Load ISEAR data
filename = ""
data = pd.read_excel(filename)

#Form better index
data['ind'] = data.index

#Manual removal of answers of no information
indices = [112,127,370,435,468,559,694,710,1139,1157,1172,1192,1208,1238,1395,\
           1450,1464,1557,1625,1733,1817,1822,1830,1877,1945,1947,1964,1976, \
           2035,2045,2050,2053,2081,2091,2100,2149,2163,2311,2461,2555,2651, \
           2680,2696,2819,2830,2888,3045,3183,3190,3207,3216,3243,3392,3582, \
           3692,3699,3724,3734,3752,3762,3772,3869,3905,3917,3956,3957,3964, \
           3972,3981,3987,4001,4003,4047,4053,4058,4062,4065,4069,4107,4117, \
           4163,4343,4495,4562,4809,5337,5498,5550,5557,5576,5598,5722,6296, \
           6311,6602,6628,6669,6675,6682,6684,6692,6799,6735,6751,6754,6758, \
           6767,6789,6792,6816,6817,6875,6882,6890,7022,7035,7038,7043,7062, \
           7072,7106,7119,7198,7208,7375,7383,7388,7395,7409,7411,7473,7480, \
           7491,7499,7505,7511,7594,7595,7601]

#Stopwords for answers which do not include any information about the emotion
stop_responses = ['i can', 'no response', 'no description', \
                  'i cant', 'i cannot']

other_indices = []

#Remove manually collected rows
for ind in indices:
    data = data.drop(data.ind[ind])

#Collect indices of rows with no information
for row in data.itertuples():
    for item in stop_responses:
        if item in row.SIT.lower():
            other_indices.append(row.ind)

#Remove rows with no information
for ind_o in other_indices:
    if ind_o in data.ind:
        data = data.drop(data.ind[ind_o])

new_data = data[['SIT', 'Field1']]
new_data = new_data.rename(columns={'SIT': 'text', 'Field1': 'sentiment'})

output = ""
new_data.to_csv(output, index=False)