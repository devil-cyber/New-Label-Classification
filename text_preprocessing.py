import csv
from tqdm import tqdm
from nltk.corpus import stopwords

class PreprocessText:
    def __init__(self):
        pass

    def PreProcessDataset():
        STOPWORD = set(stopwords.words('english'))
        articles = []
        labels = []
        with open("data.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            print("Processing Dataset...")
            for row in tqdm(reader):
                labels.append(row[0])
                article = row[1]
                for word in STOPWORD:
                    token = ' ' + word + ' '
                    article = article.replace(token, ' ')
                    article = article.replace(' ', ' ')
                articles.append(article)
        print("Processing ended..")
        return articles,labels



