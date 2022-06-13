# FoondaMate ML Engineer Coding Challenge-001

## History

1. Assume Marry, a college student adviser helps students solve timetable clashes over email.
2. Assume Marry is so helpful that students want to share her email address with their friends.
3. To ensure students know they can share her email address, Marry has updated her signature to say, “If you found this conversation  helpful, feel free to share my email address with your friends”.
5. With the updated signature, Marry now gets about 250 emails from students a week either asking if they can share her email 6. address with other students, or saying they’ve shared her email address with other students.
5. Most the emails Marry gets are unpunctuated one liners, like the below:
   1. "Can I share your email"
   2. "I will share your email"
   3. "I shall share your email"
   4. "I've shared your email"
   5. "May I share your email"
   6. "Should I share your email"
   7. "I already shared the email"
   8. "I've just shared your email"
   9. "Am I allowed to share your email"
   10. "Am I able to share your email"
   11. "I am able to share your email"
   12. "Will you help my friends if I share your email with them?"
    
6. Marry has asked the college’s IT department to help her find or build some kind of filter that labels emails of this kind as either:
“Student has shared”
“Student wants to know if can share”
 
## Project Description
The function 'check_email' takes in a string as a sentence and returns 'Student has shared' if the sentence has the words 'shared' and 'email', returns 'Student wants to know if can share' if the sentence has the words 'share' and 'email' and returns 'Sentence has misspelt words or is invalid' if the sentence does not have 'share/shared' and 'email'.

## Installation

- First, start by installing python 3.x and pip.
  > https://www.python.org/downloads/
  > https://pypi.org/project/pip/

- Then clone this repository

``
git clone https://github.com/Thandiwe-Khalaki/Thandiwe-Khalaki-FoondaMate-ML-Engineer-Coding-Challenge-001.git
``

- I recommend installing virtualenv

``pip install pipenv
``

- Create a virtual environment with the name of your choice

``python -m venv ./env``

- Activate the virtualenv. If you are a Mac or Unix user, you can activate it as follows:

``source env/bin/activate``

- If you are a windows user, you can activate it as follows:

`` .\env\Scripts\activate``
 - Install the python dependencies on the virtual environment

``pip install -r requirements.txt``

- You can now run the main file 

`` python main.py``

- You can run the test file

`` python test_main.py``


## References
https://careers.foondamate.com/machine-learning-engineer-remote/foondamate-ml-engineer-coding-challenge-001
### License

[MIT](https://choosealicense.com/licenses/mit/)