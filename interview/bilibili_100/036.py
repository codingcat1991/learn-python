"""
英文分词计算词频
"""
import collections
import re

content = """
New to programming? Python is free and easy to Learn if you know where
Chinese Trans lation
New to Python?
Read BeginnersGuide/Overview for a short explanation of what Python is.
Getting Python
Next, install the Python 3 interpreter on your computer. This is the program that reads Python pl
There are also Python interpreter and IDE bundles available, such as Thonny. Other options can be
At some stage, you' 11 want to edit and save your program code. Take a Look at HowToEditPythonCodc
Learning Python
I
Nextl read a tutorial and try some Simple experiments with your new Python interpreter.
If you have never programmed before, see BeginnersGuide/NonProgrammers for a list of kuitable tut
If you
have previous programming-
eut ReainersGuide/Prog rammers, which lists mort
"""

words = re.split(r'\W', content)
words = [word for word in words if word]
counter = collections.Counter(words)
print(counter.most_common(2))
