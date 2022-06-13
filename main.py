import re

def check_mail(sentence):
    if re.search(r'\bshared\b.*\bemail\b',sentence, flags= re.IGNORECASE):
        return 'Student has shared'
    elif re.search(r'\bshare\b.*\bemail\b',sentence, flags= re.IGNORECASE):
        return 'Student wants to know if can share'
    else:
        return 'Sentence has misspelt words or is invalid'
if __name__ == "__main__":
    print(check_mail("Can I share your Email"))
    print(check_mail("I've shared your email"))
    print(check_mail("I've shareed your email"))