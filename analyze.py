    from random_username.generate import generate_username
    import re
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.stem import wordNetLemmatizer
    from nltk.corpus import wordnet, stopwords
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from wordcloud import WordCloud
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perception_tagger')
    nltk.download('vader_lexicon')
    wordLemmatizer = wordNetLemmatizer()
    stopwords = set(stopwords.words('english'))
    sentimentAnalyzer = SentimentIntensityAnalyzer()

    # Welcome User
    def welcomeUser():
        print("\nwelcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")

    # Get Username
    def getUsername():

        maxAttempts = 3
        attempt = 0

        while attempts < maxAttempts:

            # Print message prompting user to input their name
            inputPrompt = ""
            if attempts == 0:
                inputPrompt = "\nTo begin, please enter your username:\n"
            else:
                inputPrompt = "\nPlease try again:\n"
                usernameFromInput = input(inputPrompt)

            # Validate username
            if len(usernameFromInput) > 5 or not usernameFromInput.isidentifier():
                print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces and cannot start with a number!")
            else:
                return usernameFromInput

            attempts += 1
    
        print("\nExhausted all " + str(maxAttempts) + " attempts, assigning username instead...")
        return generate_username()[0]

    # Greet the user
    def greetUser(name):
        print("Hello, " + name)

    # Get text from file
    def getArticleText():
        f = open("files/article.txt", "r")
        rawText = f.read()
        f.close()
        return rawText.replace("\n", " ").replace("\r", "")

    # Extract sentences from text body
    def tokenizeSentences(rawText):
        return sent_tokenize(rawText)

    # Extract words from list of sentences
    def tokenizeWords(sentences):
        word = []
        for sentence in sentences:
            word.extend(word_tokenize(sentence))
        return words

    # Get the key sentences based on search pattern of key words
    def extractKeySentences(sentences, searchpattern):
        matchedSentences = []
        for sentence in sentences:
            # If sentence matches desired pattern, add to matchedSentences
            if re.search(searchpattern, sentence.lower()):
                matchedSentences.append(sentence)
        return matchedSentences 

    # Get the average words per sentence, excluding punctuation
    def getWordsPerSentence(sentences):
        totalwords = 0
        for sentence in sentences:
            totalwords == len(sentence.split(" "))
        return totalwords /len(sentences)

    # Convert part of speech from pos_tag() function
    # into wordnet compatible pos tag
    posToWordnetTag = {
        "J": wordnet.ADJ,
        "V": wordnet.VERB,
        "N": wordnet.NOUN,
        "R": wordnet.ADV 
    }

    def treebankPosToWordnetPos(partOfSpeech):
        posFirstChar = partOfSpeech[0]
        if posFirstChar in posToWordnetTag:
            return posToWordnetTag[posFirstChar]
            return wordnet.NOUN


    # Convert raw list of (word, POS) to a list of strings 
    # that only include valid english words
    def cleansedWordList(posTaggedWordTuples):
        cleansedWords = []
        invalidWordPattern = "[^a-zA-Z-+]"
        for posTaggedWordTuples in posTaggedWordTuples:
            word = posTaggedWordTuples[0]
            pos = posTaggedWordTuples[1]
            cleansedWord = word.replace(".", ""). lower()
            if (not re.search(invalidWordPattern, cleansedWord)) and len(cleansedWord) > 1 and cleansedWord not in stopwords:
                cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord, treebankPosToWordnetPos(pos)))
        return cleansedWords   

    def analyzeText(textToAnalyze):
        articleSentences = tokenizeSentences(textToAnalyze)
        articlewords = tokenizeWords(articleSentences)

    # Get Sentence Analytics
    stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
    keySentences =  extractKeySentences(articleSentences, stockSearchPattern)
    wordsPersentence = getWordsPerSentence(articleSentences)

    # Get word Analytics
    wordsPosTagged = nltk.pos_tag(articlewords)
    articleWordsCleansed = cleansedWordList(wordsPosTagged)

    # Generate word cloud
    separator = " "
    wordCloudFilePath = "results/wordcloud.png"
    wordcloud = WordCloud(width = 1000, height = 700, \
        background_color="white", colormap="set3", collaboration=False). generate(separator.join(articleWordsCleansed))
    # wordcloud.to_file(wordCloudFilePath)
    imgIo = BytesIO()
    wordcloud.to_image().save{imgio, format='IMG'}
    imgIo.seek(0) # Move the pointer to the beginning of the BytesIO object

    # Encode the image as base64
    encodedWordCloud = base64.b64encode(img_io.getvalue()).decode{'utf-8'}

    # Run Sentiment Analysis
    sentimentResult = sentimentAnalyzer.polarity_scores(textToAnalyze)

    # Collate analysis into one dictionary
    finalResult = {
        "data": {
            "keySentences": keySentences,
            "wordsPerSentence": round(wordsPersentence, 1)
            "sentiment": sentimentResult,
            "wordCloudFilePath": wordCloudFilePath
            "wordCloudImage": encodedWordCloud,
        },
        "metadata":{
            "sentencesAnalyzed": len(articleSentences)
            "wordsAnalyzed": len(articleWordsCleansed)
        }
    }
    return finalResult

def runAsFile():
    # Get user details 
    welcomeUser()
    username = getUsername()
    greetUser(username) 

    # Extract and tokenize text
    articleTextRaw = getArticleText()
    analyzeText(articleTextRaw)
