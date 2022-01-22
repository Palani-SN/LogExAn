# LogExAn (Logical Expression Analysis)

- A Solver for Solving any Logical Expressions, shortly Reverse calculations of logical expressions for Analysis.
- Check out the example code in repo ( https://github.com/Palani-SN/LogExAn ) for reference

## LogAn

- Generate an Output of type **Dict/Json** from any Logical expression for direct solutions.
- Generate an Output of type **Dataframe/MarkDown** from any Logical expression for elaborate solutions
- Sample usage of the file is as given below (Refer Examples in the repo for detailed Usage)

```python
from LogExAn.LogicalAnalyser import LogAn

Cond = "( ( Var_new_1 == 1 ) && ( ( Var_new_4 == 7 ) || ( Var_new_9 == 12 ) ) )";
LA = LogAn(Cond);

# Default Argument 'DICT' returns dict 
asDict = LA.solution(); 
print('type :', type(asDict), end = '\n\n');
print(asDict, end = '\n\n');

# Argument 'JSON' returns json formatted string (from the Dict)
asJson = LA.solution('JSON');
print('type :', type(asJson), end = '\n\n');
print(asJson, end = '\n\n');

# Default Argument 'DATAFRAME' returns dataframe
asDataframe = LA.elaborate_solution();
print('type :', type(asDataframe), end = '\n\n');
print(asDataframe, end = '\n\n');

# Argument 'MARKDOWN' returns markdown formatted string (from the Dataframe)
asMarkdown = LA.elaborate_solution('MARKDOWN');
print('type :', type(asMarkdown), end = '\n\n');
print(asMarkdown, end = '\n\n');

```
- The Output of the above code looks as follows

```output
type : <class 'dict'>

{'True': {'Var_new_1': [1], 'Var_new_4': [7], 'Var_new_9': [12]}, 'False': {'Var_new_1': [-4, -3, -2, -1, 0, 2, 3, 4, 5, 6], 'Var_new_4': [2, 3, 4, 5, 6, 8, 9, 10, 11, 12], 'Var_new_9': [7, 8, 9, 10, 11, 13, 14, 15, 16, 17]}}

type : <class 'str'>

{
    "False": {
        "Var_new_1": [
            -4,
            -3,
            -2,
            -1,
            0,
            2,
            3,
            4,
            5,
            6
        ],
        "Var_new_4": [
            2,
            3,
            4,
            5,
            6,
            8,
            9,
            10,
            11,
            12
        ],
        "Var_new_9": [
            7,
            8,
            9,
            10,
            11,
            13,
            14,
            15,
            16,
            17
        ]
    },
    "True": {
        "Var_new_1": [
            1
        ],
        "Var_new_4": [
            7
        ],
        "Var_new_9": [
            12
        ]
    }
}

type : <class 'pandas.core.frame.DataFrame'>

                            Condition                                              True                                              False
0   Var_new_1 == 1 and Var_new_4 == 7    {'Var_new_1': [(1, 2)], 'Var_new_4': [(7, 8)]}  {'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_4': ...
1  Var_new_1 == 1 and Var_new_9 == 12  {'Var_new_1': [(1, 2)], 'Var_new_9': [(12, 13)]}  {'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_9': ...

type : <class 'str'>

|    | Condition                          | True                                             | False                                                              |
|---:|:-----------------------------------|:-------------------------------------------------|:-------------------------------------------------------------------|
|  0 | Var_new_1 == 1 and Var_new_4 == 7  | {'Var_new_1': [(1, 2)], 'Var_new_4': [(7, 8)]}   | {'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_4': [(2, 7), (8, 13)]}   |
|  1 | Var_new_1 == 1 and Var_new_9 == 12 | {'Var_new_1': [(1, 2)], 'Var_new_9': [(12, 13)]} | {'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_9': [(7, 12), (13, 18)]} |

```

### solution()

- Gets the format to return the direct result of the analysis.(of type dict/json string)

```python
## Definition
def solution(self, format = 'DICT'):
```
- Arguments
  - Arg 1 - format (format of the return value)
	- 'DICT' - default argument/returns output as type : <class 'dict'>
	- 'JSON' - returns output as type : <class 'str'> (json formatted string of dictionary)
- Returns 
  - Results 
	- the result as a dictionary ( if format == 'DICT' )
	- the result as a json formatted string ( if format == 'JSON' )
			
#### Accessing Dictionary (general Format)

- A dictionary with 'True' and 'False' as keys and the corresponding inputs as values

```python
from LogExAn.LogicalAnalyser import LogAn

# entire condition to be enclosed in a bracket
Cond = " ( ( low_bnd > 2 && low_bnd < 7 ) || ( up_bnd > 15 && up_bnd < 21 ) ) "; 
LA = LogAn(Cond);

# Accessing only values for the condition to pass (expected result : True)
values_for_true = LA.solution()['True'];
print(values_for_true, end = '\n\n')

# Access the results as a normal dictionary
for var, val in values_for_true.items():
	print(var, val);

print(end = '\n')

# Accessing only values for the condition to fail (expected result : False)
values_for_false = LA.solution()['False'];
print(values_for_false, end = '\n\n')

# Access the results as a normal dictionary
for var, val in values_for_false.items():
	print(var, val);

```
- The Output of the above code looks as follows

```output
{'low_bnd': [3, 4, 5, 6], 'up_bnd': [16, 17, 18, 19, 20]}

low_bnd [3, 4, 5, 6]
up_bnd [16, 17, 18, 19, 20]

{'low_bnd': [-3, -2, -1, 0, 1, 2, 7, 8, 9, 10, 11, 12], 'up_bnd': [10, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 26]}

low_bnd [-3, -2, -1, 0, 1, 2, 7, 8, 9, 10, 11, 12]
up_bnd [10, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25, 26]

```
			
### elaborate_solution()

- Gets the format to return the elaborate result of the analysis.(of type dataframe/markdown string)

```python
## Definition
def elaborate_solution(self, format = 'DATAFRAME'):
```
- Arguments
  - Arg 1 - format (format of the return value)
	- 'DATAFRAME' - default argument/returns output as type : <class 'pandas.core.frame.DataFrame'>
	- 'MARKDOWN' - returns output as type : <class 'str'> (markdown formatted string of dataframe)
- Returns 
  - Results 
	- the result as a dataframe ( if format == 'DATAFRAME' )
	- the result as a markdown formatted string ( if format == 'MARKDOWN' )

#### Accessing Dataframe (general Format)

- A dataframe with 'True' and 'False' as columns and the corresponding inputs as cells.
- For detailed usage of dataframe refer pandas documentation here :point_down:      
	( https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html ).

```python
from LogExAn.LogicalAnalyser import LogAn
import ast

Cond = " ( ( low_bnd >= 2 || up_bnd == 3 ) && ( low_bnd == 4 || up_bnd <= 5 ) ) "
LA = LogAn(Cond);

# Accesing direct result
possible_values = LA.solution();
print(possible_values, end = '\n\n')

# Accesing result with explanation
asMarkdown = LA.elaborate_solution('MARKDOWN');
print(asMarkdown, end = '\n\n')

# Accessing elaborate results as elements of dataframe
asDf = LA.elaborate_solution();

# Accessing elements of dataframe
for idx, row in asDf.iterrows():

    print('-> index : ', idx)
    print(f'-> Condition {idx+1} : ', row['Condition'])

    print('-> True : ', row['True'])
    true_results_dict = ast.literal_eval(row['True'])
    # Access the results as a normal dictionary
    for var, val in true_results_dict.items():
        print('---> variable : ', var);

        # Expanding values from list of tuples 
        Expanded_Range = []
        for tup in val:
            Expanded_Range += [*range(tup[0],tup[1])];
        print('---> values : ', Expanded_Range)

    print('-> False : ', row['False'])
    false_results_dict = ast.literal_eval(row['False'])
    # Access the results as a normal dictionary
    for var, val in false_results_dict.items():
        print('---> variable : ', var);

        # Expanding values from list of tuples 
        Expanded_Range = []
        for tup in val:
            Expanded_Range += [*range(tup[0],tup[1])];
        print('---> values : ', Expanded_Range)

    print();


```
- The Output of the above code looks as follows

```output
{'True': {'low_bnd': [2, 3, 4, 5, 6, 7], 'up_bnd': [0, 1, 2, 3, 4, 5]}, 'False': {'low_bnd': [-1, 0, 1], 'up_bnd': [6, 7, 8]}}

|    | Condition                     | True                                      | False                                                        |
|---:|:------------------------------|:------------------------------------------|:-------------------------------------------------------------|
|  0 | low_bnd >= 2 and low_bnd == 4 | {'low_bnd': [(4, 5)]}                     | {'low_bnd': [(-3, 4), (5, 10)]}                              |
|  1 | low_bnd >= 2 and up_bnd <= 5  | {'low_bnd': [(2, 8)], 'up_bnd': [(0, 6)]} | {'low_bnd': [(-3, 2)], 'up_bnd': [(6, 11)]}                  |
|  2 | up_bnd == 3 and low_bnd == 4  | {'up_bnd': [(3, 4)], 'low_bnd': [(4, 5)]} | {'up_bnd': [(-2, 3), (4, 9)], 'low_bnd': [(-1, 4), (5, 10)]} |
|  3 | up_bnd == 3 and up_bnd <= 5   | {'up_bnd': [(3, 4)]}                      | {'up_bnd': [(-2, 3), (4, 11)]}                               |

-> index :  0
-> Condition 1 :  low_bnd >= 2 and low_bnd == 4
-> True :  {'low_bnd': [(4, 5)]}
---> variable :  low_bnd
---> values :  [4]
-> False :  {'low_bnd': [(-3, 4), (5, 10)]}
---> variable :  low_bnd
---> values :  [-3, -2, -1, 0, 1, 2, 3, 5, 6, 7, 8, 9]

-> index :  1
-> Condition 2 :  low_bnd >= 2 and up_bnd <= 5
-> True :  {'low_bnd': [(2, 8)], 'up_bnd': [(0, 6)]}
---> variable :  low_bnd
---> values :  [2, 3, 4, 5, 6, 7]
---> variable :  up_bnd
---> values :  [0, 1, 2, 3, 4, 5]
-> False :  {'low_bnd': [(-3, 2)], 'up_bnd': [(6, 11)]}
---> variable :  low_bnd
---> values :  [-3, -2, -1, 0, 1]
---> variable :  up_bnd
---> values :  [6, 7, 8, 9, 10]

-> index :  2
-> Condition 3 :  up_bnd == 3 and low_bnd == 4
-> True :  {'up_bnd': [(3, 4)], 'low_bnd': [(4, 5)]}
---> variable :  up_bnd
---> values :  [3]
---> variable :  low_bnd
---> values :  [4]
-> False :  {'up_bnd': [(-2, 3), (4, 9)], 'low_bnd': [(-1, 4), (5, 10)]}
---> variable :  up_bnd
---> values :  [-2, -1, 0, 1, 2, 4, 5, 6, 7, 8]
---> variable :  low_bnd
---> values :  [-1, 0, 1, 2, 3, 5, 6, 7, 8, 9]

-> index :  3
-> Condition 4 :  up_bnd == 3 and up_bnd <= 5
-> True :  {'up_bnd': [(3, 4)]}
---> variable :  up_bnd
---> values :  [3]
-> False :  {'up_bnd': [(-2, 3), (4, 11)]}
---> variable :  up_bnd
---> values :  [-2, -1, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10]

```

## CodeFlow

![](https://github.com/Palani-SN/LogExAn/blob/main/LogExAnCodeFlow.PNG?raw=true)
