from LogExAn.LogicalAnalyser import LogAn
import ast
import json

ConditionsList = [ 

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

for i in range(len(ConditionsList)):
    
    LA = LogAn(ConditionsList[i]);

    Act_String = f""" 
{ConditionsList[i]}

{LA.solution('JSON')}

{LA.elaborate_solution('MARKDOWN')}""";

    OutputFile = open(f'Condition{i+1}.log', "w");
    OutputFile.write(Act_String)
    OutputFile.close();
    print(f'Condition{i+1}.log : Done');
        