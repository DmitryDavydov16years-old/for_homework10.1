import pandas as pd

# with open('../src/transactions.csv', encoding='UTF-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# df = pd.read_excel("../src/transactions_excel.xlsx")
# data = df.to_dict(orient='records')
# for row in data:
#     print(row)

wine_reviews = pd.read_csv("transactions.csv")


# # for i in wine_reviews:
# #     v = i
# # d = v.split(";")
# # for i in d:
# #     print(i)
# wine_reviews = pd.read_csv("transactions.csv")
# c=wine_reviews.iloc[0]
# for i in c:
#     print(i)
# # print(c)
# f=wine_reviews.columns
# for i in f:
#     d=i.split(";")
#     for i in d:
#         print(i)
# print(f)
# c=(wine_reviews.shape[0])

import pandas as pd
def foo():
    counter = 0
    dictionary_1 = []
    while True:
        wine_reviews = pd.read_csv("transactions.csv")
        a = wine_reviews.shape[0]
        counter_1 = 0
        dictionary = {}
        c = wine_reviews.iloc[counter]
        f = wine_reviews.columns
        for i in f:
            j = i.split(';')
            for s in j:
                for g in c:
                    n = g.split(';')
                    dictionary[s] = n[counter_1]
                counter_1 += 1
            dictionary_1.append(dictionary)
        counter += 1
        if counter == a:
            return dictionary_1
            break

# def foo():
#     wine_reviews = pd.read_csv("transactions.csv")
#     data = wine_reviews.to_dict(orient='records')
#     return data[0]['id;state;date;amount;currency_name;currency_code;from;to;description']
#

print(foo())
