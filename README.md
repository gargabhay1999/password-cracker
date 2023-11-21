# password-cracker
Here is a sample README file for the password crackers for LinkedIn, Yahoo, and FormSpring data breaches:

# Password Crackers for LinkedIn, Yahoo, and FormSpring Data Breaches

This repository contains Python scripts to crack passwords for LinkedIn, Yahoo, and FormSpring data breaches. The techniques used to obtain the passwords are described below:

## Yahoo

The user ID and password were split using the splitter (“:”) to help crack the password.

## LinkedIn

The following process helped crack the password:

1. Fetched the probable password word list from the internet.
2. Encrypted each word into its SHA1 hashing form and created the dictionary where the key = SHA1 encrypted string and the value = actual word.
3. An obvious pattern - the first five characters in the input password file were replaced with zeros.
4. In step 2, while encrypting the probable words, I replaced the first five characters with zeros.
5. For each line in the input password file, check if the line (key) is present in the above dictionary. If yes, then print the actual word (value).

### Formspring

The following technique was followed:

1. Created a salt list having all possible two-digit strings.
2. Fetched the probable password word list from the internet.
3. Prefixed each word with the salt from the salt list.
4. Encrypted each word into its SHA256 hashing form and created the dictionary where the key = SHA256 encrypted string and the value = actual word.
5. For each line in the input password file, check if the line (key) is present in the above dictionary. If yes, then print the actual word (value).

Please note that these scripts are for educational purposes only and should not be used for any illegal activities.

Here is a sample README file for the password crackers for LinkedIn, Yahoo, and FormSpring data breaches:

## Other techniques I considered:

## Yahoo

The simplest technique was to extract the user ID and password from the file.

## LinkedIn

Other hashing techniques such as SHA256 and SHA3_256 were tried, but the password was cracked using the Secure Hashing Algorithm (SHA1) technique. The difficulty in cracking passwords was identifying the first five characters of the encrypted string which were replaced with zeros.

## Formspring

Other hashing techniques such as SHA1 and SHA3_256 were tried. The Brute-Force method, which looks for all possible characters of the given length, was also tried. However, the time complexity of this method is very high. So, the Salt hashing approach was used. The passwords were encrypted using the salt and hashing technique. Using two-digit salt and SHA256 hashing technique, many passwords were cracked.

## How were the passwords stored? Comparison of the difficulty in cracking passwords protected with each type of storage.

For Yahoo, the passwords were stored in a simple text file. The passwords were not encrypted, they were in their original text form. It was easy to crack all those passwords.

For LinkedIn, the passwords were encrypted using the SHA1 hashing technique. The difficulty in cracking passwords was identifying the first five characters of the encrypted string which were replaced with zeros.

For Formspring, the passwords were encrypted using the salt and hashing technique. Using two-digit salt and SHA256 hashing technique, it cracked many passwords.

Please note that these scripts are for educational purposes only and should not be used for any illegal activities.
