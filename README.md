# Python Type Checking
Some code to understand Python type checking.

### sales1.py
A script with today's my understanding. I do not fully utilize type checking.

### sales2.py
I hear that [mypy](http://mypy-lang.org/) runs sanity check on types. I write code to set string as int
property and mypy does not complain. Why doesn't it warn my mistake? What mypy
offers is potential mistakes like putting a string into a property which should
an integer?

### sales3.py
[mypy](http://mypy-lang.org/) reports errors on reduce functions. My code returns value of int or float
correctly, but mypy thinks it is wrong.

This is understandable. Real values will be known when code really executes.
Software such as mypy cannot know what values are actually thrown to functions
such as reduce().

I added more of type hints to helper functions that reduce() uses, but mypy
raises errors anyway.

So, here is my question. What is mypy for, if it does not understand code correctly. In what ways does it help users?

When I define a class such as order, and I want its itemlines property to be a list of another class Itemline, I can write `List[Itemline]`, which is nice. When I do this, definition of `class Itemline` should be come before definition of `class Order`. This is understandable.


## Conclusion
Type hints and checking helps me become more organized about data structure I am
trying to create.

[typing package](https://docs.python.org/3/library/typing.html) "does not enforce function and variable type annotations." Still it helps me to think ahead about data structure.

[mypy](http://mypy-lang.org/) seems not to be able to analyze my code correctly, although I give extensive type hints. I do not understand what [mypy](http://mypy-lang.org/) is for.


# History
October 11th, 2020: Written.