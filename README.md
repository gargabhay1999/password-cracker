# password-cracker
Password crackers for LinkedIn, Yahoo, FormSpring data breaches
The technique I used to obtain the passwords:
1. For Yahoo, splitting the user ID and password using the splitter (“:”) helped crack the password.
2. For LinkedIn, the below process helped crack the password -
a. Fetched the probable password word list from the internet.
b. Encrypted each word into its SHA1 hashing form and created the dictionary where the key = SHA1 encrypted string and the value = actual word.
c. An obvious pattern - the first five characters in the input password file were replaced with zeros.
d. In step b, while encrypting the probable words, I replaced the first five characters with zeros.
e. For each line in the input password file, check if the line (key) is present in the above dictionary. If yes, then print the actual word (value).
3. For Formspring, the following technique was followed -
a. Created a salt list having all possible two-digit strings.
b. Fetched the probable password word list from the internet.
c. Prefixed each word with the salt from the salt list.
d. Encrypted each word into its SHA256 hashing form and created the dictionary where the key = SHA256 encrypted string and the value = actual word.
e. For each line in the input password file, check if the line (key) is present in the above dictionary. If yes, then print the actual word (value).

Other techniques you considered:
1. For Yahoo, the simplest technique was to extract the user ID and password from the file.
2. For LinkedIn, I tried other hashing techniques such as SHA256 and SHA3_256. I was able to crack the password using the Secure Hashing Algorithm (SHA1) technique.
3. For FormSpring, I tried other hashing techniques such as SHA1 and SHA3_256. I was able to crack the password using the 256-bit hashing technique SHA256. I tried the Brute-Force method, which looks for all possible characters of the given length. However, the time complexity of this method is very high. So, I went with the Salt hashing approach.
How were the passwords stored? Compare the difficulty in cracking passwords protected with each type of storage.
1. For Yahoo, the passwords were stored in a simple text file. The passwords were not encrypted, they were in their original text form. It was easy to crack all those passwords.
2. For LinkedIn, the passwords were encrypted using the SHA1 hashing technique. The difficulty in cracking passwords was identifying the first five characters of the encrypted string which were replaced with zeros.
3. For Formspring, the passwords were encrypted using the salt and hashing technique. Using two-digit salt and SHA256 hashing technique, it cracked many passwords.
