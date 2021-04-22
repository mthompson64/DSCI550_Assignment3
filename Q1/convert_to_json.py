import pandas as pd

df = pd.read_csv('fraudulent_emails_v3.tsv', sep='\t', header=0)

with open('columns.txt', 'w') as f:
    for i in df.columns:
        f.write(i + '\n')
    f.close()

# Then in terminal run:
# 
# tsvtojson -v -t fraudulent_emails_v3.tsv -j fraudulent_emails_v3.json -c columns.txt -o emails -s .9