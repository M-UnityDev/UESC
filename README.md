# UNICODE ESCAPE SEQUENCE CATCHER (UESC)

## UESC - is a simple python script that translates every Unicode Escape Sequence in a given file into English

## Dependencies:

- [Python](https://www.python.org/downloads/) >= 3.12

- [mtranslate](https://github.com/mouuff/mtranslate) 

- re and os (there is no way you don't have that in your installed python)

## How to Use it:

Install ```mtranslate``` using: ```pip install mtranslate```  

Then run a script, specify a path to the file you want to translate, and provide any corrections if needed

At the end of execution the script will create an edited copy of provided file in the original's path with ```[TRANSLATED]``` at the end of it's extension
