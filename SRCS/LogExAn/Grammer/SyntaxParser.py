from lark import Lark, Transformer, v_args
from lark.tree import Tree
from lark.lexer import Token
import copy
import itertools

LA_Grammer = """
        ?start: molecule                            -> getstatement

        !molecule: "(" molecule+ ")"                -> getmolecule
                 |  atom* LOGIC*

        ?atom: NAME RELATION VALUE                  -> getatom
             | "(" NAME RELATION VALUE ")"          -> getatom

        NAME: CNAME
        RELATION: ">"|"<"|">="|"<="|"=="|"!="
        LOGIC: "&&"|"||"
        VALUE: SIGNED_NUMBER

        %import common.CNAME
        %import common.SIGNED_NUMBER
        %import common.WS_INLINE
        %ignore WS_INLINE 

    """

@v_args(inline=True)    
class LA_Parser(Transformer):

    def __init__(self):
        self.__ID = [64, 96];
        self.__LeafDict = {};

    def getUniqueVar(self):

        if(96 < self.__ID[1] < 122):
            self.__ID[1] = self.__ID[1]+1
        else:
            self.__ID[0] = self.__ID[0]+1;
            self.__ID[1] = 97
        RetStr = chr(self.__ID[0])+chr(self.__ID[1]);
        return RetStr;

    def getatom(self, name, relation, value):

        dict_val = tuple([name.value, relation.value, value.value])
        if(dict_val in self.__LeafDict.values()):
            dict_key = list(self.__LeafDict.keys())[list(self.__LeafDict.values()).index(dict_val)]
        else:
            dict_key = self.getUniqueVar();
            self.__LeafDict[dict_key] = tuple([name.value, relation.value, value.value])
        return dict_key;

    def OR_Op(self, arg1, arg2):

        if( isinstance(arg1, list) and isinstance(arg2, list) ):
            Retval = arg1+arg2;
        elif( isinstance(arg1, list) and isinstance(arg2, str) ):
            Retval = arg1+[[arg2]];
        elif( isinstance(arg1, str) and isinstance(arg2, list) ):
            Retval = [[arg1]]+arg2;
        else:
            Retval = [[arg1],[arg2]];

        return Retval

    def AND_Op(self, arg1, arg2):

        if( isinstance(arg1, list) and isinstance(arg2, list) ):
            CalcVal = [ list(itertools.chain.from_iterable(val)) for val in list( itertools.product(arg1, arg2 ) ) ] # issue persists : to be modified 
        elif( isinstance(arg1, list) and isinstance(arg2, str) ):
            CalcVal = [ list(itertools.chain.from_iterable(val)) for val in list( itertools.product(arg1, [[arg2]] ) ) ] # issue persists : to be modified
        elif( isinstance(arg1, str) and isinstance(arg2, list) ):
            CalcVal = [ list(itertools.chain.from_iterable(val)) for val in list( itertools.product([[arg1]], arg2 ) ) ] # issue persists : to be modified
        else:
            CalcVal = [[arg1,arg2]];

        CalcVal = [ sorted(list(set(val))) for val in CalcVal ]
        RetVal = [];
        for val in CalcVal:
            if(val not in RetVal):
                RetVal.append(val);

        return RetVal

    def getmolecule(self, *args,**kwargs):

        Conditions = [];
        Operators = [];

        molecule_indices = [i for i in range(len(args)) if isinstance(args[i], Tree) and args[i].data == "molecule"]

        for i in range(len(args)):
            if(i in molecule_indices):
                for j in range(len(args[i].children)):
                    if(isinstance(args[i].children[j], Token)):
                        Operators.append(args[i].children[j].value)
                    else:
                        Conditions.append(args[i].children[j])

        Operator = list(set(Operators));
        if(len(Operator) == 1):
            if(Operator[0] == '||'):
                RetVal = Conditions[0];
                for cond in Conditions[1:]:
                    RetVal = self.OR_Op(RetVal, cond);
            if(Operator[0] == '&&'):
                RetVal = Conditions[0];
                for cond in Conditions[1:]:
                    RetVal = self.AND_Op(RetVal, cond);
        else:
            assert 0, " Only One operator to be present within a single () "

        return Tree('molecule', [RetVal]);

    def getstatement(self, molecule):

        Solved_List = [[molecule.children[0]]] if isinstance(molecule.children[0], str) else molecule.children[0];
        Solved_Dict = self.__LeafDict;
        return [ tuple(val) for val in Solved_List ], Solved_Dict;




