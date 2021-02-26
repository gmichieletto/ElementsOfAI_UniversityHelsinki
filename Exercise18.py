# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

import math

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf.append(tf[word][doc_index] * math.log(1 / df[word] , 10)) 

        print(tfidf)

main(text)

print("--------advanced---------")

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(row1, row2):
    sum = 0
    for a, b in zip(row1, row2):
        sum += abs(a-b)
    return sum

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]
    N = len(docs)
    
    # 2. go over each unique word and calculate its term frequency, and its document frequency
    vocabulary = list(set(text.lower().split()))
    n = len(vocabulary)
    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vecto
    for doc_index, doc in enumerate(docs):
        tfidf = np.empty((N, len(vocabulary)), dtype=np.float)
        for word_index, word in enumerate(vocabulary):
            tfidf[doc_index,word_index] = tf[word][doc_index] * math.log(1/df[word] , 10)
    
    
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    dist = np.empty((N, N), dtype=np.float)
    for i, row1 in enumerate(tfidf):
        for j, row2 in enumerate(tfidf):
            if i == j:
                dist[i,j] = np.Inf
            else:
                dist[i, j] =  distance(row1 , row2)
    print(np.unravel_index(np.argmin(dist), dist.shape))

main(text)
