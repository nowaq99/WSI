# author: Adam Nowakowski

class Fact:
    def __init__(self, str_fact=None, string=None):
        if string is None:
            string = str_fact.split()
        if len(string) == 1:
            self.name = string[0]
            self.is_true = True
        elif len(string) == 2:
            if string[0] == 'not':
                self.is_true = False
            else:
                raise ValueError('negation is called by "not"')
            self.name = string[1]
        else:
            raise ValueError('invalid name')

    def __eq__(self, other):
        return self.is_true == other.is_true and self.name == other.name

    def neg_fact(self):
        if self.is_true:
            return Fact(string=['not', self.name])
        else:
            return Fact(string=[self.name])


class Clause:
    def __init__(self, *args, str_clause=None):
        self.facts = list()
        for arg in args:
            self.facts.append(arg)
        if str_clause is not None:
            string = str_clause.split()
            for i in range(len(string)):
                if i == 0:
                    if string[i] == 'not':
                        self.facts.append(Fact(string=string[i:i+2]))
                    else:
                        self.facts.append(Fact(string=string[i]))
                if string[i] == 'or':
                    if string[i+1] == 'not':
                        self.facts.append(Fact(string=string[i+1:i+3]))
                    else:
                        self.facts.append(Fact(string=string[i+1]))

    def __add__(self, other):
        new_facts = list()
        exceptions = list()
        for i1 in range(len(self.facts)):
            f1 = self.facts[i1]
            for i2 in range(len(other.facts)):
                f2 = other.facts[i2]
                neg_fact = f1.neg_fact()
                if f2 == neg_fact:
                    exceptions.append((i1, i2, 'both'))
                if f1 == f2:
                    exceptions.append((i1, i2, 'one'))

        for i1 in range(len(self.facts)):
            flag = True
            for exception in exceptions:
                if i1 == exception[0]:
                    flag = False
            if flag:
                new_facts.append(self.facts[i1])
        for i2 in range(len(other.facts)):
            flag = True
            for exception in exceptions:
                if i2 == exception[1] and exception[2] == 'both':
                    flag = False
            if flag:
                new_facts.append(other.facts[i2])

        return Clause(*new_facts)

    def __sub__(self, other):
        position = -1
        for i in range(len(self.facts)):
            if self.facts[i] == other:
                position = i
                break
        if position >= 0:
            facts = self.facts[0:position] + self.facts[position+1:]
            return Clause(*facts)
        else:
            return None

    def del_fact(self, fact):
        position = -1
        for i in range(len(self.facts)):
            if self.facts[i] == fact:
                position = i
                break
        if position >= 0:
            self.facts.pop(position)

    def __eq__(self, other):
        flag = True
        if len(self.facts) == len(other.facts) and flag:
            for i in self.facts:
                find = False
                for j in other.facts:
                    if i.is_true == j.is_true and i.name == j.name:
                        find = True
                        break
                if not find:
                    flag = False
                    break
        else:
            flag = False
        return flag

    def is_atom(self):
        if len(self.facts) == 1:
            return True
        else:
            return False


def resolution(cl1, cl2):
    possible_facts = list()
    outs = list()
    for f1 in cl1.facts:
        for f2 in cl2.facts:
            neg_fact = f1.neg_fact()
            if f2 == neg_fact:
                possible_facts.append(f1)
    for fact in possible_facts:
        neg_fact = fact.neg_fact()
        out = (cl1-fact) + (cl2-neg_fact)
        if out.facts:
            outs.append((cl1-fact) + (cl2-neg_fact))
    return outs


def reasoning(clauses, obs_facts, unobs_fact):
    knowledge = clauses.copy()
    for fact in obs_facts:
        knowledge.append(Clause(fact))
    neg_fact = unobs_fact.neg_fact()
    knowledge.append(Clause(neg_fact))

    flag = True
    i = 0
    while flag:
        new_knowledge = knowledge.copy()
        for k in range(len(knowledge)):
            res_out = resolution(knowledge[i], knowledge[k])
            for out in res_out:
                if out not in new_knowledge:
                    new_knowledge.append(out)

        i = i+1
        if Clause(unobs_fact) in knowledge:
            print(unobs_fact.name, 'is', unobs_fact.is_true)
            flag = False
        if i >= len(new_knowledge) and flag:
            print(unobs_fact.name, 'is', unobs_fact.neg_fact().is_true)
            flag = False
        knowledge = new_knowledge
