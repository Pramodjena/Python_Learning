## Strings 

A string is a `sequence of characters`, and it is one of the fundamental data types used to represent textual data.

Why sequence of characters?
---------------------------
- Sequence means that the characters are stored in a particular order.
- Each character in a string has a fixed position(index).
- The order matters : `"cat"` is different from `"tac"`.

```python

single_quoted_string = 'Hello, World!'

double_quoted_string = "Hello , World!"

multiline_string = '''Hello, World'''

```

String Concatenation
--------------------
- Concatenation is the process of combining two or more strings into a single string.
- Strings can be concatenated using the `+` operator.
- Using `+=` operator is also possible.

```python

s = 'Py'
s += 'thon'
print(s)  # Output: 'Python'

```


## String Indexing and Slicing

### String Indexing

Definition:

- Accessing individual characters in a string using their position (index).

Key Points:

- Python uses zero-based indexing (starts at 0).

- Supports negative indexing (starts at -1 from the end).

Analogy:

- Imagine a bookshelf where each book has a numbered position.

`0 = First book (leftmost).`

`-1 = Last book (rightmost).`

```python

s = "HELLO"

# Positive Indexing:
print(s[0])  # Output: 'H' (1st character)
print(s[4])  # Output: 'O' (5th character)

# Negative Indexing:
print(s[-1]) # Output: 'O' (last character)
print(s[-3]) # Output: 'L' (3rd from the end)

```

### String Slicing 

Definition:

- Extracting a substring by specifying a range of indices.

string[start:end:step]

- `start` : Index to begin (Inclusive). `Default = 0`
- `end`   : Index to end (Exclusive). `Default = length of string`
- `step`  : Interval between characters `Default = 1`

Analogy:

Cutting a slice of cake:

- `Start` = Where you place the knife.

- `End` = Where you stop cutting (but you don’t eat the stop point!).

- `Step` = How many layers you skip between bites.

### Common Slicing Patterns

Let’s use s = "PYTHON" for all examples:

Slice	Result	Explanation:

- `s[2:5]`    "THO"	         Characters from index 2 to 4 (5-1).
- `s[:3]`	    "PYT"	         Start to index 2 (3-1).
- `s[3:]`	    "HON"	         Index 3 to end.
- `s[::2]`    "PTO"	         Every 2nd character.
- `s[::-1]`   "NOHTYP"	 Reverse the string.
- `s[-3:-1] ` "HO"	     From 3rd-last to 2nd-last.

### Edge Cases & Pitfalls

Empty Slices:

```python

print(s[3:2])  # Output: "" (start > end with positive step)

```
Out-of-Bounds Indices:

Python handles this gracefully:

```python

print(s[0:100])  # Output: "PYTHON" (ignores excess)

```
Step Behavior:

- Positive step: Moves left to right.

- Negative step: Moves right to left (requires start > end).

### Practical Use-Cases

Extracting File Extensions:

```python

filename = "image.jpg"
extension = filename[-3:]  # "jpg"

```
Reversing Strings:

```python

palindrome = "madam"
is_palindrome = (palindrome == palindrome[::-1])  # True

```
Parsing Data:

```python

date = "2023-10-05"
year = date[:4]  # "2023"

```
### Key Takeaways

- Indexing: Use [] to access single characters.

- Slicing: Use start:end:step to extract substrings.

- Immutability: Strings can’t be modified in-place (slicing creates new strings).

### Practice Exercise

```python

text = "ABCDEFGHIJK"
# Predict the outputs:
print(text[2:7:2])    # ?
print(text[::-2])     # ?
print(text[-4:-10:-1]) # ?

```
String Formatting
-----------------

Definition:

- Inserting values, variables or expressions into an string template.

`Why` :

- For dynamic strings. (User greetings or error messages)
- Avoid messy concatenation. (`+` Operator)

Methods of string formatting 
----------------------------

A. `f-string` : (python 3.6+)

`syntax`:` f" Text {variable} Text {expression}"`

- Evaluates expression at run time.

```python

name = 'Pramod'
age = 26

print(f"My name is {name} and I am {age} years old.)

```
B. `.format()` method :

`syntax` : `"Text {variable} Text".format(value,value)`

- Flexible but verbose.

```python 

name = 'Pramod'
age = 26

print("My name is {0} and I am {1} years old..format("Pramod",26)")

```
C. `%` Formatting Legacy :

`syntax` : `"Text %s %d %f Text" % (value, value, value)`

- `%s = string` , `%d = integer` , `%f = float`

```python 

print("Hello %s!! you have %d message and your energy is %f" % ("Pramod",10,92.56))

```

Escape Characters 
-----------------

Definition :

Special sequences starting with `\` to re-present non-printable chars or chars with special meaning.

`\n` --> Newline

`\t` --> Tab Indentation

`\"` --> Double Quote

`\'` --> Single Quote

`\\` --> Back Slash 

```python

print("Hey\n I am Pramod\n I am coding.\t ...")

```