import pandas as pd

# ----------------------
# Data Ingestion
# ----------------------

class DataSystemProcess():

    def __init__(self, path):

        self.df = pd.read_csv(path, index_col = 0)

    def get_clean_data(self):

        self.df['size_m2'] = self.df['GROSS SQUARE FEET'] / 10.764
        self.df = self.df[self.df['YEAR BUILT'] > 0]
        self.df['SALE DATE'] = pd.to_datetime(self.df['SALE DATE'])

        self.df.loc[self.df['size_m2'] > 10000, 'size_m2'] = 10000
        self.df.loc[self.df['SALE PRICE'] > 50000000, 'SALE PRICE'] = 50000000
        self.df.loc[self.df['SALE PRICE'] < 100000, 'SALE PRICE'] = 100000

        return self.df


    def means_lat_long(self):
        return self.df['LATITUDE'].mean(), self.df['LONGITUDE'].mean()

if __name__ == '__main__':
    pass