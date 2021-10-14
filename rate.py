import pandas as pd

def dataRate(filename):
    date = pd.read_csv(filename)
    counts = date['label'].value_counts()
    print(counts)

if __name__ == '__main__':
    dataRate('train.csv')
    dataRate('test.csv')
    dataRate('valid.csv')