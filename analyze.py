from random_username.generate import generate_username

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

# Extract words from list of sentneces
def tokenizeWords(sentences):
    word = []
    for sentence in sentences:
        word.extend(word_tokenize(sentence))
    return words

# Get user details 
# welcomeUser()
# username = getUsername()
# greetUser(username) 

# Extract and tokenize text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articlewords = tokenizeWords(articleSentences)

print("GOT:")
print(articlewords)
# for sentenceTest in articleSentences:
#    print(sentencesTest = "\n")
