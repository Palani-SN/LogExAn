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
