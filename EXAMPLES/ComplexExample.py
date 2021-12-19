from LogExAn.LogicalAnalyser import LogAn
import ast
import json

CondList = [ 

         " Var_new_1 > 5 ",
         " Var_new_1 < 5 ",

         " Var_new_1 == 5 ",
         " Var_new_1 != 5 ",
         
         " Var_new_1 >= 5 ",
         " Var_new_1 <= 5 ",

         "( ( Var_new_1 == 1 ) && ( ( Var_new_4 == 7 ) || ( Var_new_9 == 12 ) ) )",

         "( ( Var_new_8 < 8 && Var_new_8 > 1 && Var_new_1 < 8 && Var_new_1 > 1) || ( ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) || ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 == 8 ) ) )",
         "( ( Var_new_8 >= 8 || Var_new_8 <= 1 || Var_new_1 >= 8 || Var_new_1 <= 1) && ( ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) && ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 != 8 ) ) )"

           ];

for i in range(len(CondList)):

    LA = LogAn(CondList[i], True);
    DF_Out = LA.getDF()

    Expanded_Dict = {};
    for idx, row in DF_Out.iterrows():
        Result_Dict = ast.literal_eval(row['Result'])
        Var_Dict = {};
        for key, val in Result_Dict.items():
            Expanded_Range = []
            for tup in val:
                Expanded_Range += [*range(tup[0],tup[1])];
            Var_Dict[key] = Expanded_Range;
        Expanded_Dict[row['Condition']] = Var_Dict;

    Act_String = f""" 
{CondList[i]} True

{DF_Out.to_markdown()}

{json.dumps(Expanded_Dict, sort_keys=True, indent=4)}""";

    OutputFile = open(f'True_Condition{i+1}.log', "w");
    OutputFile.write(Act_String)
    OutputFile.close();

    print(f'True_Condition{i+1}.log : Done');


for i in range(len(CondList)):

    LA = LogAn(CondList[i], False);
    DF_Out = LA.getDF()

    Expanded_Dict = {};
    for idx, row in DF_Out.iterrows():
        Result_Dict = ast.literal_eval(row['Result'])
        Var_Dict = {};
        for key, val in Result_Dict.items():
            Expanded_Range = []
            for tup in val:
                Expanded_Range += [*range(tup[0],tup[1])];
            Var_Dict[key] = Expanded_Range;
        Expanded_Dict[row['Condition']] = Var_Dict;

    Act_String = f""" 
{CondList[i]} False

{DF_Out.to_markdown()}

{json.dumps(Expanded_Dict, sort_keys=True, indent=4)}""";

    OutputFile = open(f'False_Condition{i+1}.log', "w");
    OutputFile.write(Act_String)
    OutputFile.close();

    print(f'False_Condition{i+1}.log : Done');


