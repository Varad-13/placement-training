# Placement Training 15 Jan to 21 Jan

## Day 1
### Topics Covered:
- C Compiler introduction
- .pyc files introduction
- Python interpreter
- Python as a hybrid langage (rather than interpreted)
- Python Virtual Machine introduction

### Python:
**Python is popular for few reasons:**
- Python is simple, easy, fast, has plenty of libraries and great community support
- Python is mainly used for AI, DS applications
- Python is the most in demand programming language as per LinkedIn Job postings
- Python requires minimal amount of code as compared to other languages
- Python follows algorithm to coding principle

**Features of Python:**
- Loose Syntaxed: Multiple ways of doing a single thing
- OOPS
- Simple
- Dynamic Casting: Cast as per need. No need to initialize variables to int, String, double etc. Python compiler handles it on its own.

**Save Space by sharing:**
- Python shares address space in variable with equal values
- Python always updates values by giving new space. Old values will always be replaced at every update.
- Old values are marked as garbage and taken care of by AGC
- Python supports AGC (Auto Garbage Collection)

**In Python, inputs can only be of type string. To avoid this, we can cast the datatype while taking input. Casting input to bool is special case. It checks whether there is any input and if there is any data inputted, it will always be casted to true**

**Python Data Types:**
- int
- float
- string
- boolean
- complex

**Python operators:**
- There is not increment or decrement operators ``(i++, i--, ++i, --i)``
- Arithmetic operators are present ``(* / + - %)``
- ``//`` : Integer division. It always returns floor value, not nearest integer.
- ``**``: Power
- Shorthand operators: x+=1: Instead of ``x=x+1`` or ``x++``
- Relational and logical:
    - ``< > <= >= == !=``
    - and
    - or
- Bitwise operations:
    - `` <<n is to multiply number by 2^n ``
    - `` >>n is to divide(int) number by 2^n ``
    - `` ~(n) is to finds 2's complement ``
    - `` a^b is a xor b``

**Swapping 2 numbers:**
- ``a,b=b,a ``
- xor can be used for this operation
- ```
    a=a^b 
    b=a^b
    a=a^b
    ```
    

**Bottom up approach to coding**
- Think about output/outcome
- Formulize a process
- Think about inputs
- Before coding, always do some paperwork to find a basic flow of the program
- Let us take an example of finding area of circle:
    - Output: area of the circle
    - Process: pi*square(radius)
    - Input: radius

**Program to calculate percentage of passing:**
- Output: Percentage
- Process: If x/total then y/100. Find y
- Input: Passing marks and Total marks

**Program to find average of three numbers**
- Output: Average
- Process: (a+b+c)/3
- Input: a, b, c where a, b and c are numerical values

**Program to convert Farenheit to Celcius**
- Output: Temperature in Celcius
- Process: C = (F-32) * 5/9
- Input: Temperature in 

**Program to find roots of Quadratic equation**
- Output: Real roots of the equation or None
- Process: 
    1. Check if there is possible real roots
    2. If yes, find roots and return
    3. Else return none
- Input: a, b, c of Quadratic equation

**Sequence:**
A set of statements which are executed one after another.

**Branch:**
Based on conditions, execute only a particular sequence from a group of sequences.

``Conditions: if..else, if...elif...else``

**Loops:**
Repeat a set of instructions or a sequence "n" number of times.

``Loops: for, while``