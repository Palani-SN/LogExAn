# LogExAn (Logical Expression Analysis)

- A Solver for Solving any Logical Expressions with respect to the results expected, shortly Reverse calculations of logical expressions with respect to Boolean results(True/False).
- Check out the example code in repo ( https://github.com/Palani-SN/LogExAn ) for reference

## LogAn

- Generate a Output of type DataFrame from any Logical expression.
- Sample usage of the file is as given below (Refer Examples in the repo for detailed Usage)

```python
from LogExAn.LogicalAnalyser import LogAn
import ast

ConditionsList = [
        " Var_new_1 > 5 ",
        " Var_new_1 < 5 ",

        " Var_new_1 == 5 ",
        " Var_new_1 != 5 ",
        
        " Var_new_1 >= 5 ",
        " Var_new_1 <= 5 "
];

ResultList = [
        True,
        False
]

for Cond in ConditionsList:
    
    for Res in ResultList:
        print()

        LA = LogAn(Cond, Res);
        DF_Out = LA.getDF()

        Range_List = ast.literal_eval(DF_Out.loc[0, 'Result'])['Var_new_1']
        Actual_List = [];
        for tup in Range_List:
            Actual_List += [*range(tup[0], tup[1])]

        print(f'Cond : {Cond}', '|' ,f'Res : {Res}');
        print()
        print(DF_Out.to_markdown())
        print()
        print(f"Actual list from DF_Out['Result'] {Actual_List}")

```
- The Output of the above code looks as follows

```output
Cond :  Var_new_1 > 5  | Res : True

|    | Condition     | Result                   |
|---:|:--------------|:-------------------------|
|  0 | Var_new_1 > 5 | {'Var_new_1': [(6, 11)]} |

Actual list from DF_Out['Result'] [6, 7, 8, 9, 10]

Cond :  Var_new_1 > 5  | Res : False

|    | Condition     | Result                  |
|---:|:--------------|:------------------------|
|  0 | Var_new_1 > 5 | {'Var_new_1': [(0, 6)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4, 5]

Cond :  Var_new_1 < 5  | Res : True

|    | Condition     | Result                  |
|---:|:--------------|:------------------------|
|  0 | Var_new_1 < 5 | {'Var_new_1': [(0, 5)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4]

Cond :  Var_new_1 < 5  | Res : False

|    | Condition     | Result                   |
|---:|:--------------|:-------------------------|
|  0 | Var_new_1 < 5 | {'Var_new_1': [(5, 11)]} |

Actual list from DF_Out['Result'] [5, 6, 7, 8, 9, 10]

Cond :  Var_new_1 == 5  | Res : True

|    | Condition      | Result                  |
|---:|:---------------|:------------------------|
|  0 | Var_new_1 == 5 | {'Var_new_1': [(5, 6)]} |

Actual list from DF_Out['Result'] [5]

Cond :  Var_new_1 == 5  | Res : False

|    | Condition      | Result                           |
|---:|:---------------|:---------------------------------|
|  0 | Var_new_1 == 5 | {'Var_new_1': [(0, 5), (6, 11)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

Cond :  Var_new_1 != 5  | Res : True

|    | Condition      | Result                           |
|---:|:---------------|:---------------------------------|
|  0 | Var_new_1 != 5 | {'Var_new_1': [(0, 5), (6, 11)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]

Cond :  Var_new_1 != 5  | Res : False

|    | Condition      | Result                  |
|---:|:---------------|:------------------------|
|  0 | Var_new_1 != 5 | {'Var_new_1': [(5, 6)]} |

Actual list from DF_Out['Result'] [5]

Cond :  Var_new_1 >= 5  | Res : True

|    | Condition      | Result                   |
|---:|:---------------|:-------------------------|
|  0 | Var_new_1 >= 5 | {'Var_new_1': [(5, 11)]} |

Actual list from DF_Out['Result'] [5, 6, 7, 8, 9, 10]

Cond :  Var_new_1 >= 5  | Res : False

|    | Condition      | Result                  |
|---:|:---------------|:------------------------|
|  0 | Var_new_1 >= 5 | {'Var_new_1': [(0, 5)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4]

Cond :  Var_new_1 <= 5  | Res : True

|    | Condition      | Result                  |
|---:|:---------------|:------------------------|
|  0 | Var_new_1 <= 5 | {'Var_new_1': [(0, 6)]} |

Actual list from DF_Out['Result'] [0, 1, 2, 3, 4, 5]

Cond :  Var_new_1 <= 5  | Res : False

|    | Condition      | Result                   |
|---:|:---------------|:-------------------------|
|  0 | Var_new_1 <= 5 | {'Var_new_1': [(6, 11)]} |

Actual list from DF_Out['Result'] [6, 7, 8, 9, 10]

```

## Logan (Advanced Example)

- The Solver can be able to solve complex logical expressions as well like the expression given below.

```C
( 
    ( Var_new_8 >= 8 || Var_new_8 <= 1 || Var_new_1 >= 8 || Var_new_1 <= 1) 
    && 
    ( 
        ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) 
        && 
        ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 != 8 ) 
    ) 
)

```

- The Output of the above code looks as follows (for recursive condition the expansion of the conditions are done and the output value ranges is provided for each variable)

```

Result Expected : True

|    | Condition                                                                                                                                                              | Result                                                                                                                                                                                            |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Var_new_8 >= 8 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_8': [(9, 14)], 'Var_new_1': [(1, 2)], 'Var_new_2': [(2, 3)], 'Var_new_3': [(3, 4)], 'Var_new_4': [(4, 5)], 'Var_new_5': [(5, 6)], 'Var_new_6': [(6, 7)], 'Var_new_7': [(7, 8)]}         |
|  1 | Var_new_8 <= 1 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_8': [(-4, 2)], 'Var_new_1': [(1, 2)], 'Var_new_2': [(2, 3)], 'Var_new_3': [(3, 4)], 'Var_new_4': [(4, 5)], 'Var_new_5': [(5, 6)], 'Var_new_6': [(6, 7)], 'Var_new_7': [(7, 8)]}         |
|  2 | Var_new_1 >= 8 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_1': [], 'Var_new_2': [(2, 3)], 'Var_new_3': [(3, 4)], 'Var_new_4': [(4, 5)], 'Var_new_5': [(5, 6)], 'Var_new_6': [(6, 7)], 'Var_new_7': [(7, 8)], 'Var_new_8': [(3, 8), (9, 14)]}       |
|  3 | Var_new_1 <= 1 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_1': [(1, 2)], 'Var_new_2': [(2, 3)], 'Var_new_3': [(3, 4)], 'Var_new_4': [(4, 5)], 'Var_new_5': [(5, 6)], 'Var_new_6': [(6, 7)], 'Var_new_7': [(7, 8)], 'Var_new_8': [(3, 8), (9, 14)]} |

Result Expected : False

|    | Condition                                                                                                                                                              | Result                                                                                                                                                                                                                                                    |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Var_new_8 >= 8 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_8': [(3, 9)], 'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_2': [(-3, 2), (3, 8)], 'Var_new_3': [(-2, 3), (4, 9)], 'Var_new_4': [(-1, 4), (5, 10)], 'Var_new_5': [(0, 5), (6, 11)], 'Var_new_6': [(1, 6), (7, 12)], 'Var_new_7': [(2, 7), (8, 13)]}  |
|  1 | Var_new_8 <= 1 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_8': [(2, 14)], 'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_2': [(-3, 2), (3, 8)], 'Var_new_3': [(-2, 3), (4, 9)], 'Var_new_4': [(-1, 4), (5, 10)], 'Var_new_5': [(0, 5), (6, 11)], 'Var_new_6': [(1, 6), (7, 12)], 'Var_new_7': [(2, 7), (8, 13)]} |
|  2 | Var_new_1 >= 8 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_1': [(-4, 14)], 'Var_new_2': [(-3, 2), (3, 8)], 'Var_new_3': [(-2, 3), (4, 9)], 'Var_new_4': [(-1, 4), (5, 10)], 'Var_new_5': [(0, 5), (6, 11)], 'Var_new_6': [(1, 6), (7, 12)], 'Var_new_7': [(2, 7), (8, 13)], 'Var_new_8': [(8, 9)]}         |
|  3 | Var_new_1 <= 1 and Var_new_1 == 1 and Var_new_2 == 2 and Var_new_3 == 3 and Var_new_4 == 4 and Var_new_5 == 5 and Var_new_6 == 6 and Var_new_7 == 7 and Var_new_8 != 8 | {'Var_new_1': [(-4, 1), (2, 7)], 'Var_new_2': [(-3, 2), (3, 8)], 'Var_new_3': [(-2, 3), (4, 9)], 'Var_new_4': [(-1, 4), (5, 10)], 'Var_new_5': [(0, 5), (6, 11)], 'Var_new_6': [(1, 6), (7, 12)], 'Var_new_7': [(2, 7), (8, 13)], 'Var_new_8': [(8, 9)]}  |

```

## CodeFlow

![](https://github.com/Palani-SN/LogExAn/blob/main/LogExAnCodeFlow.PNG?raw=true)
