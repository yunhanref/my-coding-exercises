import numpy as np
path = "/content/coffee.csv" #we specify the path we are going to work on.
coffee = pd.read_csv(path) #we assign the object to the coffee variable
#now we can access coffee dataset through coffee variable
coffee.head() #shows the top
coffee.tail() #shows the bottom
coffee.describe() #statistical info
#coffee.info() #general info
coffee.columns #Index(['Day', 'Coffee Type', 'Units Sold'], dtype='object')
coffee.index #RangeIndex(start=0, stop=14, step=1)
coffee.shape #returns (columns,indexes)
coffee.size #returns the value of index*columns
coffee.sample(3) #returns 3 random samples
coffee.loc[[0,1,2,3,6,12,13]] #shows the indexes listed inside the brackets
coffee.loc[3:12] #shows the indexes and all columns of belonging index, starting from 3 to 12.
coffee.loc[3:12,["Day","Units Sold"]] #shows the rows and column 'Day' and 'Units Sold' only
coffee.iloc[3:12,[1,2]] #Shows the rows from 3 to 12 and shows the columns 1 and 2 (column indexing start from 0)
coffee.iloc[:5,[0]] #Shows the rows from 0 to 5 and shows the columns 0 only.
coffee.loc[:,["Day"]] #Shows all rows and Day column only
coffee

### MODIFYING VALUES IN PANDAS ###
#lets change the sell rate for espresso in saturday to 42
#first we need to locate the espresso in saturday. Saturday espresso is 10th row.
coffee.loc[[10],['Units Sold']] = 42
coffee # as you can see we just changed it to 42
#now lets change all of them
for  i in coffee.index:
  coffee.loc[[i],["Coffee Type"]] = "Ice Caramel Latte" #changed all coffe type values of all rows with iced caramel latte.
  if i == 6:
    coffee.loc[[i],["Coffee Type"]] = "love beverage"
for i in coffee.index:
  coffee.loc[[i],["Units Sold"]] = i+500
  if i == 6:
    coffee.loc[[i],["Units Sold"]] = 66
coffee