import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest

# Input text
text = " The trucks packed with cucumbers, green beans and bananas inched forward in a long, looping line, waiting to come into the United States at the Mariposa port of entry, one of the border’s busiest crossings for Mexican-grown produce. U.S. inspectors used to refer only a handful of drivers for cargo screening with powerful scanning equipment to check for illegal drugs. But on a recent morning they routed every truck through a new drive-through machine the size of a carwash. Known as a “multi-energy portal,” the equipment has allowed U.S. Customs and Border Protection to scan nearly six times as much cargo per day.Construction crews were busy installing a second machine alongside it, racing to finish before peak grape season this spring, when trucks coming from Mexico are expected to roll through with 30 million pounds of fruits and vegetables per day. The harvest is an auspicious time for drug smugglers."

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize the sentences into words
words = [word_tokenize(sentence.lower()) for sentence in sentences]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = []
for sentence in words:
    filtered_words.append([word for word in sentence if word.casefold() not in stop_words])

# Calculate the word frequency
word_freq = FreqDist([word for sentence in filtered_words for word in sentence])

# Calculate the sentence scores using the TextRank algorithm
rankings = defaultdict(int)
for i, sentence in enumerate(filtered_words):
    for word in sentence:
        rankings[i] += word_freq[word]

# Get the top n sentences as the summary
n = 3
summary = nlargest(n, rankings, key=rankings.get)
summary_text = ' '.join([sentences[i] for i in summary])

print(summary_text)
