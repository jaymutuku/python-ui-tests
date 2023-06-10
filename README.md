
### What this project is for?

This project is a selenium python UI testing project.
The script therein does the following:
1. Navigates to this site https://www.ultimateqa.com/filling-out-forms
2. Fills in the first form.
3. Clicks the submit buttom
4. Checks for the successful message

### Steps
1. Clone the repository
```bash
$ git clone https://github.com/jaymutuku/python-ui-tests
```
```bash
$ cd python-ui-tests/
```

#### Create and Activate a Virtual Environment
```bash
$ pip3 install virtualenv
$ virtualenv -p python3 venv 
$ source venv/bin/activate
```
Incase you get an error in the second step above:
command 'virtualenv' not found ...
Then
```bash
$ sudo apt install virtualenv
```
#### Install the required packages
```bash
$ pip install selenium
```
You don't need to install the unittest library is a built-in library.

#### Save the dependencies to _requirements.txt_
```bash
$ pip freeze > requirements.txt
```

### Running a single test case 

```bash
   $ python -m unittest testcases.test_ui.verifyMessageTest
```

### Running all tests
```bash
   $ python -m unittest discover
```

### Expected Output
```bash
.
----------------------------------------------------------------------
Ran 1 test in 11.108s

OK

```
