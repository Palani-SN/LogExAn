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

