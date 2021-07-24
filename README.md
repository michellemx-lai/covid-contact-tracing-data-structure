<h1>CovidData</h1>

Built with Python, this data structure is used to acess, analyze, and manipulate a set of fictitious COVID-19 contract tracing data.

I was provided a (fictitious) dataset of information collected by a COVID-19 contact tracer, and I developed data structures that allow quick access to and manipulation of that data. 

Completed in the middle of the COVID-19 pandemic, this project gave me a sense of the power of object-oriented programming to gather and display data, and helped me in understanding important worldwide events. 

<h1>The Code</h1>

This project is separated into five parts: 

<h2>Part 1 – Represent the Contact Tracing Data</h2>
I designed and implemented a data structure that will be used to represent information about an infected person, and others infected by contact with that person.

<h2>Part 2 – Parse the Contract Tracing Data</h2>
I designed and implemented a function to process the content of a file containing data on persons and infections. The data file is in csv format and has the following structure:

    id,infected-by,date a3959d249c3444dbb36310bb16e2a689,d03ba6ffa3b5475989ce477973d1617d,2021-02-09 ae66eefa796a4a59aa375d0514620fcf,209864c2f0f543089f8466e7bcff3acd,2021-01-27 435e781627db4635b966c3d4fd493728,d161fa8d17f244d186ef9a47b40e931c,2021-03-21 0583968bf83442858853ef7c2d0f75cb,c921ae9021ab440aa440601e20fdb45f,2021-01-16

<h2>Part 3 – Identify the Top Direct Superspreaders</h2>
A “direct superspreader” is a person who directly infects many others. In this part, I designed and implemented a function to identify the top direct superspreader(s): the person(s) that directly infected the most other persons.

<h2>Part 4 – Find Superspreading Dates</h2>
We define a superspreading date as the date in which the most persons were infected. Ties are possible and so there may be multiple direct superspreading dates. In this part, the superspreading dates are identified and extracted. 

<h2>Part 5 – Identify the Top (Direct + Indirect) Superspreaders</h2>
In Part 3 I looked at direct infections: when one person infects one or more others. Indirect infections are the ones that follow from a direct infection. For example, if person A infects person B and person B infects persons C and D, A is said to have indirectly infected C and D. If C and D do not infect anyone else, A is said to have (directly + indirectly) infected three persons: B, C, and D. In this part, I designed and implemented two functions to identify all people directly or indirectly infected by a person, and to identify the top (direct + indirect) superspreader(s).

<h1>What I Learned</h1>
After completing this project, I learned the following:

<h2>General knowledge</h2>
• Understand, explain, and use the basic programming concepts (variable creation and instantiation, loops, selection statements, functions)

• Understand, explain, and use the basic data types in Python (ints, floats, strings, Booleans, lists, dictionaries, sets, tuples)

• Understand and explain basic object-oriented design concepts (objects, classes, methods, inheritance, polymorphism)•Design, implement, and debug object-oriented programs•Use, reuse, and modify existing code

• Design, implement, and debug solutions to engineering problems in Python: (1) design a computational solution to a problem described in natural language, (2) express the solution in an algorithmic way, (3) convert the algorithm plan effectively into a Python program

• Learn how to use the Python interpreter for simple math calculations

<h2>Variables, values, expressions and simple statements</h2>
• Understand fundamentals of programming such as variables, values, statements, conditional anditerative execution

• Declare, instantiate variables(assignment statements) and distinguish between various types of statements

• Call/invoke None-returning functions

• Knowledge of basic data types and associated methods/operations, e.g., as split()),slicing [:], join(), and list().

• Instantiate basic built-in data types/classes

<h2>Control structures</h2>
• Develop a basic understanding ofcontrol structures, i.e., if statements, for and while loops, etc.
• Practice using control flow statements (if statements, for and while loops).FunctionsLearn the concept of function
• Use/call/invoke built-in functions
• Call functions from external libraries via importing modules
• Define a functionLearn the notion of helper function
• Write docstrings, including doctests
• Practice completing short functions where the docstring and doctests are provided.Practice translating mathematical functions into Python ones
• Practice designing complex functions based on a given descriptionLearn to find (and fix) bugs in provided functions

<h2>Recursion</h2>
• Learn the concept of recursion
• Practice writing recursive functions

<h2>Files</h2>
• Concept of file
• Open, close, read and write files

<h2>Fundamentals of Object-Oriented Programming</h2>
• Concept of data abstraction and encapsulation
• Define classes, including data and method attributesLearn how to implement constructors and class methods
• Basics of inheritance and polymorphism mechanisms
• Practice using class libraries
• Basics of linked data structures(i.e., classes that have at least a field of their own type)Learn how to use exception handling 
