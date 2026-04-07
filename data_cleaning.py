import pandas as pd
def clean_data():
  df=pd.read_csv("rent_data.csv")
  print("Before cleaning:"df.shape)
  df=df.dropna()
  df=df.drop_duplicates()
  print("After Cleaning:",df.shape)
  df.to_csv("cleaned rent data.csv",index=False)
  print("clean file saved")

if __name__=="__main__":
  clean_data() 
  
  
