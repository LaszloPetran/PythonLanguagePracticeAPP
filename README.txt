This webapp has been created in Python and Flask framework. 

Created by Laszlo Petran

This is a simplified English practice webapp, but it can be used in any language, from and to. 
The goal was simply encouraging students with pregenerated options to create a sentence, it is easier than choosing words without options. 
The students this way can boost their own success-feeling by completing simple tasks, and also learning new words. 

The app is based on json file!!!

The files: 
words.py: the Wordform in a function, it was the only solution how to make each instance a proper submit button to be identified with. 
practiceController.py: The logic and routes. 
beginner.html: The sentences to choose to solve. 
singletest.html: The chosen sentence to solve. 
createform.html: Creating a 4 word sentence. Every field must be filled up. 

The process: 
1. The app loads data from json file.
2. Each sentence has attributes, the unique Submitx (in /beginner.html) attribute opens the route (/singletest), which is the task itself. 
3. Creating the sentence properly a flash message informs the student if it's correct. 
4. Redirected back to main page (/beginner.html), where the result is displayed. 
5. The number of sentences are infinite, so as the input output language. (Some special encoding may be needed with special characters)
6. A teacher can create sentences for students for exams, or homework, and the students can show the result. 