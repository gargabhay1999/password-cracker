import hashlib

def get_probableEncryptedWordsDict():
    # create a dictionary having hashed sha1 encrypted probable word as key and the word as value
    dict = {}
    with open('probable-words.txt', 'r', encoding='utf-8' ) as f:
        words = f.read().splitlines()
        for word in words:
            # replace first 5 characters in hashed_word to '00000' since their value is from the common words
            hashed_word = '00000' + hashlib.sha1(word.encode()).hexdigest()[5:].strip()
            # hashed_word = hashlib.sha1(word.encode()).hexdigest().strip()
            dict[hashed_word] = word
        return dict

probableEncryptedWords = get_probableEncryptedWordsDict()

# read the SHA1.txt file
with open('linkedin-output.txt', 'w', encoding='utf-8') as f:
    with open('SHA1.txt', 'r', encoding='utf-8') as file:
        count=0
        lines = file.readlines()
        for line in lines:
            # check if the line (encrypted password is present in our dictionary)
            if line.strip() in probableEncryptedWords:
                f.write(f"{line.strip()} : {probableEncryptedWords[line.strip()]}\n") # print encryped and actual password
                count+=1
            # if count==100:
            #     break