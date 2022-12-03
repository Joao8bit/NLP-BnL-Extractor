import pandas as pd

header = ['Source', 'Date', 'Publisher', 'Description', 'Language', 'Score']
def csv_concatenator(file1, file2, output):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    out = pd.concat((df1, df2))
    with open(output, 'w', encoding='utf-8') as f:
        out.to_csv(f, index=False)