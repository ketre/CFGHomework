Theory Questions

*1.1    What does SDLC stand for? (1 mark)*

Software Development Life Cycle - a phased and systemic framework for software engineers to follow in application design. There are several models of SDLC - like waterfall, agile, scrum

*1.2 What exception is thrown when you divide a number by 0? (1 mark)*

ZeroDivisionError

*1.3   What is the git command that moves code from the local repository to the remote repository? (1 mark)*

git push

*1.4 What does NULL represent in a database? (1 mark)*

A blank or non-existent value at point of creation

*1.5 Name 2 responsibilities of the Scrum Master (2 marks)*

1. Scrum master helps their team overcome and foresee obstacles impeding progress
2. Scrum master facilitates effective and procedural team collaboration and communication by means of agile management

*1.6 Name 2 debugging methods, and when you would use them. (4 marks)*

1. **Exception handling:** allows your program to gracefully respond to events and execution. To catch and handle exceptions, we wrap the code in *try* (your desired code) and *except* (block of code to determine how to handle the exception) blocks. Exception is a python object raised in response to logical errors.
2. **Assertions** : debugging aids to help catch errors during development. You can turn it on/off after finishing testing your program - by default, these are disabled in Python. Are often placed at the start and end of the function to check for valid input and output. In Python, assert keyword is used to check if the condition is met - error is triggered if not.

`assert <boolean expression as condition>, “error message text”`

*1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. (5 marks)*

```python
def can_pay(price, cash_given):
if cash_given >= price:
return True
else:
return False
```

The above function will throw an error if incorrect value type is passed as an argument. This function will only produce meaningful output for numeric values. TypeError will be thrown when string is passed as input for one of arguments, because you can't compare strings with numbers or floats.

We can handle the exception by adding the try-except block as below to indicate the TypeError and indicate invalid input to the developer.

```python
def can_pay(price, cash_given):
    try:
        if cash_given >= price:
            return True
        else:
            return False
    except TypeError as e:
        return (f'{e}: Please only pass numeric values as arguments')
```

*1.8 What is git branching? Explain how it is used in Git. (6 marks)*

Git is a Version Control System. In git, branching suggests diverging from the main line of development into a series of isolated commits, or branches. This allowss for a simultaneous development without copying the code. Each branch represents a pointer as a reference to series of commits made to it.

By default, you will be wroking in to the main branch. `git checkout -b ‘newbranch’` will create a new branch and switch to it. You are able to make changes to your branch without affecting the main line.

Once changes have been made and tested, your branch can be merged with main, by first staging all files (`git add .`), committing those (`git commit -m ‘your commit message’` ), and pushing to your branch (`git push`). Depending on the project and team structure, you can then either merge this with main by calling `git merge ‘newbranch’` from the main, or raising a pull request.

Sometimes, a clean merge isn’t possible due to conflicting code blocks - these won’t be merged until resolved. Once manually resolved, a git commit can finalise the merge. Once done, it’s good practice to delete obsolete branches.

To get a list of all branches, you can run `git branch` . The current branch will be marked with an asterisk in the list given.

*1.9  Design a restaurant ordering system.(10 marks) *

*You do not need to write code, but describe a high-level approach:*

*a. Draw a list of key requirements*

*b. What are your main considerations and problems?*

*c. What components or tools would you potentially use?*

**For the purpose of this question, I will be assuming a website for a restaurant, allowing to place orders without having to create an account.**

Requirements:

1. Client-facing website: inclusive of HTML, CSS, and JS elements to allow for basic user interaction and display of the menu items, as well as filters an grouping.
2. Server: server-side logic for handling orders, payments, and data storage
3. Database management: allowing restaurant to update its menu items pre- and post- ordering
4. Order management: interface allowing to place an order and leave notes for the restaurant on client side.
5. Payment management: for client side, this involves the total sum of ordered items, and gateways for a secure transaction. For admin side, this includes passing a request to the kitchen.

Main considerations:

User interface has to be intuitive, welcoming, and easy to navigate. Imagery should have ALT text, where possible - to cater to PwD.

Server should be hosted on the cloud, allowing for sufficient traffic during peak hours (dinner time, weekends)

Database synchronisation should work with no exceptions, accepting updates from both admin side and client side to keep the menu up-to-date. All dietary requirements and considerations should be clearly labelled. Relational db should be used to effectively manage complex orders.

Payment security protocols should be adhered to. Various payment options should be presented to the customer. User data should be protected at all times, adhering to the local GDPR standards and protocols.

Components/tools to use:

Front-end (html, CSS, JS), back-end (JS, python), database management (SQL), APIs to fetch geolocation data and time, encryption services, cloud server client
