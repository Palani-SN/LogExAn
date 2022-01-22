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