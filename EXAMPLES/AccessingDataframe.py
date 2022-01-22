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
