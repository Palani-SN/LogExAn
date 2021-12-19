from .Grammer.SyntaxParser import LA_Grammer, LA_Parser
from lark import Lark, Transformer, v_args
import pandas as pd
import numpy as np
import itertools
import json

class LogAn():

	def __init__(self, Condition, Output):

	    LA_Template = Lark(LA_Grammer, parser='lalr', transformer=LA_Parser())
	    Logan_Parser = LA_Template.parse

	    Stripped_Condition = ''.join(Condition.split('\n'))
	    Cond_List, Map_Dict = Logan_Parser(Stripped_Condition)
	    self.Output = Output;

	    df = pd.DataFrame();
	    df['Condition'] = np.nan;
	    df['Result'] = np.nan;
	    for idx in range(len(Cond_List)):
	    	Cond, Res = self.getConditionAndResult(Cond_List[idx], Map_Dict);
	    	df.loc[idx, 'Condition'] = Cond;
	    	df.loc[idx, 'Result'] = str(Res);

	    self.DF = df;

	def getConditionAndResult(self, Cond_List, Map_Dict):

		Dependency_List = [];
		Dependency_Dict = {};
		for val in Cond_List:
			atom = Map_Dict[val];
			Dependency_List.append(atom);
			if(atom[0] in Dependency_Dict.keys()):
				Dependency_Dict[atom[0]] += [*range(int(atom[2])-5, int(atom[2])+6)];
			else:
				Dependency_Dict[atom[0]] = [*range(int(atom[2])-5, int(atom[2])+6)];

		Cond_String = " and ".join([ " ".join(list(elem)) for elem in Dependency_List])

		Output_Dict = {};
		for dep, ranges in Dependency_Dict.items():
			Input_Condition = " and ".join([ " ".join(list(elem)) for elem in Dependency_List if elem[0] == dep]);
			Input_Range = sorted(list(set(Dependency_Dict[dep])));
			Output_Dict[dep] = self.NarrowDownRanges(dep, Input_Condition, Input_Range, self.Output);

		return Cond_String, Output_Dict;

	def GetRanges(self, Inplist):

	    for a, b in itertools.groupby(enumerate(Inplist), lambda pair: pair[1] - pair[0]):
	        
	        b = list(b)
	        yield b[0][1], b[-1][1]+1

	def NarrowDownRanges(self, Variable, Condition, Value, Output):

		Res_List = [];
		for val in Value:
			vars()[f'{Variable}'] = val;  
			if(eval(Condition) == Output):
				Res_List.append(val);

		Ret_List = list(self.GetRanges(Res_List));
		return Ret_List;

	def getDF(self):

		return self.DF;
