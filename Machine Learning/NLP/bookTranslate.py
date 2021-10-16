from textblob import TextBlob

with open('pride.txt',encoding='utf-8') as f:
    file_contents = f.read()
# print(file_content)

book_pride = TextBlob(file_contents)
positive_sentiment_sentences = []
negative_sentiment_sentences = []

for sentence in book_pride.sentences:
    if sentence.sentiment.polarity == 1:
        positive_sentiment_sentences.append(sentence)
    if sentence.sentiment.polarity == -1:
        negative_sentiment_sentences.append(sentence)

# print(positive_sentiment_sentences[:3])
# print(negative_sentiment_sentences[:3])

print("The " + str(len(positive_sentiment_sentences)) + " most positive sentences:")
for sentence in positive_sentiment_sentences:
    print("+ " + str(sentence.replace("\n", "").replace("      ", " ")))


print("The " + str(len(negative_sentiment_sentences)) + " most negative sentences:")
for sentence in negative_sentiment_sentences:
    print("- " + str(sentence.replace("\n", "").replace("      ", " ")))