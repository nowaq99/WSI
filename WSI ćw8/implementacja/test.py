# author: Adam Nowakowski

from reasoning import Fact, Clause, reasoning


cl1 = Clause(str_clause='A or B or C')
cl2 = Clause(str_clause='not A or D')
cl3 = Clause(str_clause='not B or D')
cl4 = Clause(str_clause='not C or not E or F')
cl5 = Clause(str_clause='D or E or F')
cl6 = Clause(str_clause='A or not F')
cl7 = Clause(str_clause='not D or not E')
clauses = [cl1, cl2, cl3, cl4, cl5, cl6, cl7]
obs1 = Fact(str_fact='not A')
obs2 = Fact(str_fact='B')
obs_facts = [obs1, obs2]
unobs_fact = Fact(str_fact='C')
reasoning(clauses, obs_facts, unobs_fact)
