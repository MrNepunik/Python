My Python Projects
This repository contains a few small Python programs I made while learning the basics. Each one helped me practise things like taking input, using loops, writing conditions, and working with lists.

What's Included
Billing System with VAT
This program makes a simple shopping bill. You enter the items, their quantities, and the price of each piece. It then shows the subtotal, adds 13% VAT, and prints the final amount to pay.

The updated version also asks again if you enter an invalid quantity or price. The 13% rate is fixed in the code and is applied to every item for this project.

GPA Calculator
This program takes your subject marks and calculates your grades, GPA, and percentage.

You can choose a class from 9 to 12. For classes 11 and 12, you can also choose science or management and select the subjects included in the program.

Here is the grading scale used in the code:

Marks	Grade	Grade Point
90–100	A+	4.0
80–89	A	3.6
70–79	B+	3.2
60–69	B	2.8
50–59	C+	2.4
40–49	C	2.0
0–39	F	0.0
Every subject is marked out of 100 and has equal weight. The overall GPA is the average of the subject grade points. This is the scale used for this practice project, so it should not be treated as an official grading calculator.

Quiz Game
A simple quiz with 10 multiple-choice questions. Each question has four options, and you enter the number of your answer. Correct answers move you to the next question and increase your virtual prize money. A wrong answer ends the game.

There are still a few things to fix:

The introduction says you can quit at any time, but entering 0 only works as a quit option from question 4 onward.

Entering text instead of an option number is not handled yet.

Some questions, answers, and prize amounts need checking.

The prize money is just part of the game.

Password Strength Checker
This program checks a password and gives it a basic rating: Weak, Moderate, or Strong.

It looks at the password's length, checks a small list of common passwords, and looks for a few predictable patterns and repeated characters. It also shows whether the password contains uppercase letters, lowercase letters, numbers, and symbols.

The character-type checks are shown as extra information; the rating comes from the other rules in the code.

This is only a learning project, not a complete security tool. It does not check leaked-password databases, and a Strong rating does not guarantee a safe password. Use made-up passwords when trying it out, especially in an online editor. What you type is visible in the current version.

How to Try the Programs
On your computer
You will need Python 3 installed.

Download the Python file you want to run.

Open a terminal in the folder where you saved it.

Run the command below, replacing filename.py with the actual filename:

bash
python filename.py
If your computer uses python3 instead, run:

bash
python3 filename.py
Then follow the instructions shown in the terminal.

Using an online editor
You can also copy one program into an online Python editor, click Run, and answer the prompts in its terminal.

These programs do not import any third-party packages.

What I Practised
While making these projects, I worked with:

User input and output

Variables and calculations

Conditions using if, elif, and else

Loops, lists, and tuples

Functions

Handling invalid input with try and except

Formatting output with f-strings

Things to Improve
Some improvements I could make next are:

Add better input checks throughout the programs.

Fix the quiz answer key and make the quit option work on every question.

Add an option to play or run a program again.

Let the billing system save a bill to a file.

Add more pattern checks to the password checker.

These projects are part of my Python practice. They are small programs for learning, and there is still room to improve them.
