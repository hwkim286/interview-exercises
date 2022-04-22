"""
@author: Eric Kim
"""
import pandas as pd
#read in csv files
data1 = pd.read_csv('a.csv')
data2 = pd.read_csv('b.csv')

#Create column with count of each ids
count1 = data1.value_counts().rename_axis('id').reset_index(name = 'a')
count2 = data2.value_counts().rename_axis('id').reset_index(name = 'b')

#outer join count1 and count2
merge = pd.merge(count1, count2, on = 'id', how = 'outer')

#replace NaN with 0
merge = merge.fillna(0)

#change data type of columns a and b to integer
merge = merge.astype({'a' : int})
merge = merge.astype({'b' : int})

#sort merged dataframe
merge = merge.sort_values('id')

#write merged dataframe into csv file
merge.to_csv('final.csv', index = False)


