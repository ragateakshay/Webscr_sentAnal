import os
from negation_words import negation_words



corpa_path = os.path.join(os.path.dirname(__file__), 'corpa.txt')
with open(corpa_path, 'r') as f:
    corpa = dict(map(str.strip, line.split('\t')) for line in f)


with open("english_stopwords.txt", "r") as f:
    stopwords = f.read().split()


def calculate_sentiment(text):
    words = text.lower().split()
    words = [word for word in words if word not in stopwords]
    

    negate = False
    sentiment_score = 0
    for i, word in enumerate(words):
        negate = False
        if word in negation_words:
            negate = True
        elif negate:
            if i+1 < len(words):
                next_word = words[i+1]
                if next_word in corpa:
                    sentiment_score -= int(corpa[next_word])
                negate = False
            else:
                sentiment_score -= int(corpa.get(word, 0))
                negate = False
        else:
            sentiment_score += int(corpa.get(word, 0))


    num_words = len(words)
    if num_words == 0:
        return 0
    else:
        sentiment = round(sentiment_score/num_words, 2)
        return sentiment
    
text = "the product is not good"
senti = calculate_sentiment(text)    
print(senti)