import pandas as pd

with open(file="Spanish words.txt", encoding="utf-8") as espw:
    ap = espw.readlines()
    sp = [_.strip() for _ in ap]

esp_words = []
eng_meanings = []
for _ in sp:
    esp_words.append(_.split(sep=">", maxsplit=2)[1])
    eng_meanings.append(_.split(sep=">", maxsplit=2)[2])

esp_word_dict = {
    "Spanish" : esp_words,
    "English" : eng_meanings
}

esp_word_df = pd.DataFrame(esp_word_dict)
esp_word_df.to_csv("esp_word_list.csv",index=False)