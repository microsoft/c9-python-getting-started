# Loops

## For loops

[For loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) takes each item in an array or collection in order, and assigns it to the variable you define.

``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

## While loops

[While loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) perform an operation as long as a condition is true.

``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```

## Additional (multi-variable for loop)

In the above example of for loop, we have used a single variable to iterate through the list. Similarly, we can use a zip() function to iterate through more than one list in a for loop.

The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together and so on.

```python
names = ['Christopher', 'Susan']
rolls = [123, 124]
for name,roll in zip(names, rolls):
    print(name,roll) 
```
