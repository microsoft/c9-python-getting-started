# Function parameters

Functions allow you to take code that is repeated and move it to a module that can be called when needed. Functions are defined with the `def` keyword and must be declared before the function is called in your code. Functions can accept one or more parameters and return values.

- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

```python
def function_name(parameter):
    # code to execute
    return value
```

Parameters can be assigned a [default value](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) making them optional when the function is called.

```python
def function_name(parameter=default):
    # code to execute
    return value
```

When you call a function you may specify the values for the parameters using positional or [named notation](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)

```python
def function_name(parameter1, parameter2):
    # code to execute
    return value

# Positional notation pass in arguments in same order as parameters are declared
result = function_name(value1,value2)

# Named notation
result = function_name(parameter1=value1, parameter2=value2)
```
