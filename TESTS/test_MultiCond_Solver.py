from LogExAn.LogicalAnalyser import LogAn
import pytest
import ast
import json
from conftest import DEBUG

CondList = [ 

         "( ( Var_new_8 == 8 && Var_new_1 == 1 ) || ( ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) || ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 == 8 ) ) )",
         "( ( ( Var_new_8 == 8 ) && ( Var_new_1 == 1 ) ) || ( ( ( Var_new_1 == 1 ) && ( Var_new_2 == 2 ) && ( Var_new_3 == 3 ) && ( Var_new_4 == 4 ) ) || ( ( Var_new_5 == 5 ) && ( Var_new_6 == 6 ) && ( Var_new_7 == 7 ) && ( Var_new_8 == 8 ) ) ) )",

         "( ( (Var_new_8 == 8) || (Var_new_1 == 1) ) && ( ( (Var_new_1 == 1) || (Var_new_2 == 2) || (Var_new_3 == 3) || (Var_new_4 == 4) ) && ( (Var_new_5 == 5) || (Var_new_6 == 6) || (Var_new_7 == 7) || (Var_new_8 == 8) ) ) )",
         "( ( Var_new_8 == 8 || Var_new_1 == 1 ) && ( ( Var_new_1 == 1 || Var_new_2 == 2 || Var_new_3 == 3 || Var_new_4 == 4 ) && ( Var_new_5 == 5 || Var_new_6 == 6 || Var_new_7 == 7 || Var_new_8 == 8 ) ) )",

         "( ( Var_new_8 < 8 && Var_new_8 > 1 && Var_new_1 < 8 && Var_new_1 > 1) || ( ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) || ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 == 8 ) ) )",
         "( ( Var_new_8 >= 8 || Var_new_8 <= 1 || Var_new_1 >= 8 || Var_new_1 <= 1) && ( ( Var_new_1 == 1 && Var_new_2 == 2 && Var_new_3 == 3 && Var_new_4 == 4 ) && ( Var_new_5 == 5 && Var_new_6 == 6 && Var_new_7 == 7 && Var_new_8 != 8 ) ) )"

           ];

CondsvsFiles = [ tuple([CondList[i], f'Solver_MultiCondition{i+1}.log']) for i in range(len(CondList))]

Cond_In = None;
DF_Out = None;
Ref_File = None;

@pytest.fixture(autouse = True, scope="function")
def fix_function():

    global Cond_In;
    global DF_Out;
    global Ref_File;
    
    yield
    
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
{Cond_In} 

{json.dumps(Expanded_Dict, sort_keys=True, indent=4)}

{DF_Out.to_markdown()}""";

    if(DEBUG):
        OutputFile = open(f'res_files/{Ref_File}', "w");
        OutputFile.write(Act_String)
        OutputFile.close();

    file = open(f'ref_files/{Ref_File}', 'r');
    Ref_String = file.read();
    print(Act_String)

    assert(Ref_String == Act_String)

##########################################################################################################
## Multi condition based tests for Solver 
##########################################################################################################

@pytest.mark.parametrize("Condition, Filename", CondsvsFiles)
def test_MultiCondition(Condition, Filename):

    global Cond_In;
    global DF_Out;
    global Ref_File;

    Cond_In = Condition;
    print(Cond_In)

    LA = LogAn(Cond_In, True);
    DF_Out = LA.getDF()

    Ref_File = Filename;
