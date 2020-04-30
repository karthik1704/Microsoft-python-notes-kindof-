# Python

https://aka.ms/MSLearnPython

## Print

```python
# save file with .py extension (print.py)
print('Hello World')
print("Hello World")
```

### Input and variable print

```python
name = input('Please enter your name: ')
print(name)
```

### Blank Lines using print

```python
print() # Creates blanks line
print('Hello \nWorld') # new line \n
```

### Debugging With print

```python
print('Adding Number')
x = 34+88
print('Perfroming Division')
y = x/0  # thorws error
print('math complete') # its never print
```

## Run Python File

in Terminal/Cmd

```cmd
python print.py
```

## Comments

```python
# Hi I'am Comment


```

## String

```python
first_name = 'karthi' # string
print(first_name)
```

### Combine Strings With +

```python
first_name = 'karthi'
last_name = 'A'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)
```

### Functions to Modify Strings

```python
# common functions
sentence = 'The dog is named sammy'
print(sentence.upper()) # turns UPPERCASE
print(sentence.lower()) # turns lowercase
print(sentence.capitalize()) # Turns First Latter Capitalize
print(sentence.count('a')) # counts given strings, in this case 'a' is 2
```

## Formatting Strings

```python
output = 'Hello, ' + first_name + ' ' + last_name
output = 'Hello, {} {}'.format(first_name , last_name)
output = 'Hello, {0} {1}'.format(first_name , last_name) # 0 - first_name, 1 - last_name

# Only available in Py3
output = f'Hello, {first_name} {last_name}'

```

## Numbers

```python
pi = 3.14159 # numbers
print(pi)
```

```python
first_number = 6
second_number = 8

print(first_number + second_number)
print(first_number ** second_number) # ** - Exponent
```

### Combine Strings with Numbers

```python
# This Thorws Error (Combining Two unsupported data type Error)
days_in feb = 28
print(days_in_feb + 'days in Feb') # error
print(str(days_in_feb) + 'days in Feb') # str() converts int to string
```

```python
first_number = '6'
second_number = '8'

print(first_number + second_number) # 68
print(int(first_number) + int(second_number)) # int() converts string into number
```

```python
# input() always returns string
first_number = input('Enter First Number')
second_number = input('Enter Second Number')

print(int(first_number) + int(second_number)) # int() converts string into number


print(float(first_number) + float(second_number)) # float () converts string into floating point number
```

## Date

```python
# To get current date and time
# we Need to use the datetime library
from datetime import datetime

current_date = datetime.now()

# the function (datetime.now()) returns a datetime # object, in order to print with strng  we need to # convert to str()
print('Today is ' + str(current_date))

```

```python
from datetime import datetime

current_date = datetime.now()

print(' Day: ' + str(current_date.day))
print(' Month: ' + str(current_date.month))
print(' Year: ' + str(current_date.year))

```

## Manipulate Date

```python
from datetime import datetime, timedelta
today = datetime.now()
print('Today is ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was:' + str(yesterday))


```

### Date as a string & convert to date

```python
from datetime import datetime

birthday = input('When is Your Birthday (dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print(' Birthday: ' + str(birthday_date))

```

## Error Handling

```python
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not Allowed to Divide by Zero')
else:
    print('Someting else went wrong')
finally:
    print('This is our clean-up code')


```

## Conditional Logic

```python
if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)
```

### Elif

```python

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
```

### OR

```python
if province == 'Alberta' or province == 'Nunavut':
tax = 0.05
elif province == 'Ontario':
tax = 0.13
else:
tax = 0.15

```

### IN

```python
if province in ('Alberta', 'Nunavut', 'Yukon'):
tax = 0.05
elif province == 'Ontario':
tax = 0.13
else:
tax = 0.15

```

### Nested If

```python
if country == 'Canada':
    if province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
    elif province == 'Ontario':
    tax = 0.13
    else:
    tax = 0.15
else:
    tax = 0.0
```

### Complex Condition

```python
if gpa >= .85 and lowest_grade >= .70:
    print('well done')
```

## Collections

### List

```python
names = ['karthi','A']
scores = []
scores.append(98)
scores.append(99)
print(names)
print(scores)
print(scores[1]) # 99
```

```python
print(len(names)) # 2
names.insert(0,'Bill') # Insert Before Index
print(names) # [Bill,Karthi,A]
names.sort()
print(names) # [A,Bill,Karthi]

```

#### Retriving Ranges

```python
names = ['bill','karthi', 'Jhon', 'Doe' ]

presenters = names[1:3] # start and end index
# Start to 3 [:3],
print(presenters) # ['karthi','Jhon']

```

### Arrays

```python
from array import array # numeriacal data type
# must all in same data type
scores = array('d') # d - double data type
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

```

### Dictionaries

```python
person = {'first':'Karthi'} # {'key':'value'}
peson['last'] = 'A'
print(person) # {'first':'karthi', 'last':'A'}
print(person['first']) # karthi
```

## Loops

### For

```python
for name in ['Karthi', 'Barry']:
    print(name)

names = ['Karthi', 'Barry']

for name in names:
    print(name)

for index in range(0,3):
    print(index) # 0 1 2
```

### While

```python
names = ['Karthi', 'Barry']
index = 0

while index < len(names):
    print(names[index])
    index += 1 # index = index + 1
```

## Functions

```python
from datetime import datetime

def print_time():
    print('Task Completed')
    print(datetime.now())
    print()

first_name = "Barry Allen"
print_time()

for x in range(0,10):
    print(x)

print_time()
```

```python
from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = "Barry Allen"
print_time('First name assigned')

for x in range(0,10):
    print(x)

print_time('Loop completed')
```

```python
def get_initial(name):
    initial = name[0:1]
    return inital

first_name = input('Enter First Name : ')
first_name_initial = get_initial(first_name)

last_name = input('Enter Last Name : ')
last_name_initial = get_initial(last_name)

```

## Parameterized Functions

```python
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else
        initial = name[0:1]
    return inital

first_name = input('Enter First Name : ')
first_name_initial = get_initial(first_name, False)

last_name = input('Enter Last Name : ')
last_name_initial = get_initial(last_name, True)

```

### Default Value for a Parameter

```python
def get_initial(name, force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    else
        initial = name[0:1]
    return inital

first_name = input('Enter First Name : ')
first_name_initial = get_initial(first_name)

last_name = input('Enter Last Name : ')
last_name_initial = get_initial(last_name, False)

```

### Named Notation Parameter

```python
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else
        initial = name[0:1]
    return inital

first_name = input('Enter First Name : ')
first_name_initial = get_initial(name=first_name,force_uppercase =  False)

last_name = input('Enter Last Name : ')
last_name_initial = get_initial(force_uppercase = True, name=last_name)

```

## Modules and Packages

### Module

```python
# helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)

```

### Importing a Module

```python
# otherfile.py
# we can import file 3 type

# import module as namespace
import helpers
helpers.display('Not a Warning')

# import all into current namespace
from helpers import * # * means all
display('Not a Warning')

# import specific items into current namespace
from helpers import display
display('Not a Warning')

```

## Packages

Installing third-party pacakges using pip
in cmd-line

```cmd
pip install colorama
```

Installing from list of packages

```cmd
pip install -r requirements.txt
```

- -r - requirement file flag

requirements.txt

```txt
colorama
```

## Virtual Environments

in terminal/cmd

```cmd
pip install virtualenv
```

in windows

```cmd
python -m  venv <folder_name>
```

- -m - module

Ex

```cmd
python -m  venv myenv
```

in Linux

```bash
virtualenv <folder_name>
```

ex

```bash
virtualenv myenv
```

### Activate Virtual Environments

Windows System

in cmd

```cmd
<folder_name>\Scripts\Activate.bat
```

in powershell

```cmd
<folder_name>\Scripts\Activate.ps1
```

in bash shell

```bash
. ./<folder_name>/Scripts/activate
```

OSX/Linux

```bash
<folder_name>/bin/activate
```

### Installing Packages in VENV

in cmd-line

```cmd
pip install colorama
```

Installing from list of packages

```cmd
pip install -r requirements.txt
```

- -r - requirement file flag

requirements.txt

```txt
colorama
```

### Using Third-Package

```python
# helpers.py
from pip._vendor.colorama import init, Fore


def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)

```

## Calling an API

```python
import requests
import json

API_KEY = ''

url =  ''
address = url + 'analyze'

parameters = {'visualFeatues': 'Description,Color','language': 'en'}

images_path = './images.jpeg'
image_data = open(image_path, 'rb').read()

headers = {'content-type': 'appliaction/octet-stream',
...
}

response = requests.post(address,headers = headers,params = parameters ,  data= image_data)

response.raise_for_status()

results = response.json()

print(json.dump(results))
```

### JSON

```python
# above same code
print(json.dumps(results))

# Print value from JSON output
print()
print('requesetId')
print(results['requestId'])

```

#### Subkey

```python
# {
# "color":{
#     "dominantColorBackground":"white"
# }
# }
print('dominantColorBackground')
print(results['color']['dominantColorBackground'])

```

#### Array Items

```python
# {
# "description":{
#     "tag":["bear","Polar"...]
# }
# }
print('first Tag')
print(results['description']['tag'][0])

print('all Tag')

for item in results['description']['tag']:
    print(item)
```

### Create JSON from DICT

```python
import json

person_dict = {
    'first':'Barry',
    'last':'Allen',
}

person_dict['city'] = 'Centeral City'

person_json = json.dumps(person_dict)

print(person_json)

```

### Mananging Keys

- Environment Variables With .env

```cmd
pip install python-dotenv
```

```python
import os
os_version = os.getenv('OS')

print(os_version) # Windows_NT

```

## Decorators

```python
# Sippets from flask


@route('api/products')  # Decorators
def get_products:
    # Code to list from DB
    pass;

```

### Creating Decorators

```python
def logger(func):
    def wrapper():
        print('Logging Execution')
        func()
        print('Done Logging')
    return wrapper

@logger
def sample():
    print('--Inside sample function')

sample()
```
