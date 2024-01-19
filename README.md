# Command Line Bank System

I made a super basic bank system that allows new users to create accounts by inputting their names, IDs, and home addresses. The program then spits out an account number. They can then sign into their accounts and withdraw or deposit funds. All account information is saved onto a text file 'database'. When the user exits the program, the text file contents are erased. This all operates within the command line. 

###Main Menu  
```
Welcome to the Totally Ethical Bank System.
Create account(A)
Quit(Q)
List accounts(ls)
Login(E)
```
###Login Menu
```
Enter your id to login into your account: {id}
Welcome back! {person}
Available Options:
deposit 'amount'
withdraw 'amount'

help
Available actions:
deposit 'amount'
withdraw 'amount'

wrong keyword
Invalid input!The available actions are 'deposit' or 'withdraw'. Otherwise enter 'help'

deposit 100000
deposited R10000 into account
Would you like to transact again: y
withdraw 4000
withdrew R4000 from account
Would you like to transact again: n

```

###Database structure within text file

```
----------------------------------
Name: {name}
ID: {ID number}
Address: {Address}
Account Number: {Randomly generated number}
Balance: R{numeric balance}
----------------------------------
```


**Technologies**: Python
**Learnings**: text file manipulation
**Process and Inspiration**: Pursued this mini project really just for fun. I was bored one day and decided to be a systems engineer. I plan to add more actions in the future such as loaning, taxing, credit cards etc, overall just include more methods for my poor customers to place themselves into indebtness.  
