import hashlib

def get_probableEncryptedWordsDict():
    # create a dictionary having hashed sha1 encrypted probable word as key and the word as value
    dict = {}
    # two digits string
    saltList = [str(num).zfill(2) for num in range(100)]
    with open('probable-words.txt', 'r', encoding='utf-8' ) as f:
        words = f.read().splitlines()
        for word in words:
            for salt in saltList:
                #adding salt as prefix before each word
                saltedWord = salt + word
                hashedWord = hashlib.sha256(saltedWord.encode()).hexdigest().strip()
                dict[hashedWord] = word
        return dict

probableEncryptedWords = get_probableEncryptedWordsDict()

# read the formspring.txt file
with open('formspring-output.txt', 'w', encoding='utf-8') as f:
    with open('formspring.txt', 'r', encoding='utf-8') as file:
        count=0
        lines = file.readlines()
        for line in lines:
            # check if the line (encrypted password is present in our dictionary)
            if line.strip() in probableEncryptedWords:
                f.write(f"{line.strip()} : {probableEncryptedWords[line.strip()]}\n") # print encryped and actual password
                count+=1
            if count==100:
                break