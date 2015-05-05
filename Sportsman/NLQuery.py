

from pyparsing import *
# populate ingredients->recipes "database"
recipes = "Tuna casserole/Hawaiian pizza/Chicken a la King/"\
 "Pepperoni pizza/Baked ham/Tuna melt/Eggs Benedict"\
 .split("/")
ingredients = "eggs/pineapple/pizza crust/pepperoni/ham/bacon/"\
 "English muffins/noodles/tuna/cream of mushroom soup/chicken/"\
 "mixed vegetables/cheese/tomato sauce/mayonnaise/Hollandaise sauce"\
 .split("/")
recipe_ingredients_map = [
 (0,8),(0,9),(0,7),(1,2),(1,1),(1,4),(2,7),(2,9),(2,10),(2,11),
 (3,3),(3,2),(3,12),(3,13),(4,1),(4,4),(5,6),(5,8),(5,14),(5,12),
 (6,6),(6,0),(6,12),(6,4),(6,15),
 ]
recipesByIngredient = dict((i,[]) for i in ingredients)
for recIndex,ingIndex in recipe_ingredients_map:
 recipesByIngredient[ ingredients[ingIndex] ].append( recipes[recIndex] )
# classes to be constructed at parse time, from intermediate ParseResults
class UnaryOperation(object):
    def __init__(self, t):
        self.op, self.a = t[0]
class BinaryOperation(object):
    def __init__(self, t):
        self.op = t[0][1]
        self.operands = t[0][0::2]
class SearchAnd(BinaryOperation):
    def generateSetExpression(self):
        return "(%s)" % \
        " & ".join(oper.generateSetExpression() for oper in self.operands)
    def __repr__(self):
        return "AND:(%s)" % (",".join(str(oper) for oper in self.operands))
class SearchOr(BinaryOperation):
    def generateSetExpression(self):
        return "(%s)" % \
        " | ".join(oper.generateSetExpression() for oper in self.operands)
    def __repr__(self):
        return "OR:(%s)" % (",".join(str(oper) for oper in self.operands))
class SearchNot(UnaryOperation):
    def generateSetExpression(self):
        return "(set(recipes) - %s)" % self.a.generateSetExpression()
def __repr__(self):
    return "NOT:(%s)" % str(self.a)
class SearchTerm(object):
    def __init__(self, tokens):
        self.term = tokens[0]
    def generateSetExpression(self):
        if self.term in recipesByIngredient:
            return "set(recipesByIngredient['%s'])" % self.term
        else:
            return "set()"
    def __repr__(self):
        return self.term


class QueryString():
    def __init__(self, t):
        self.sports = t.sports
        self.inexpr = t.inexpr
        self.withexpr = t.withexpr
        self.rangeexpr= t.rangeexpr

#    def 

    def gen_query(self):
        filter = self.rangeexpr or self.withexpr
        query ={}
        if filter:
            query['query'] = {
    "filtered" : {
        "query" : {
            "match_all" : {}
        },
        "filter" : {
            "geo_distance" : {
                "distance" : "200km",
                "geo_location" : {
                    "lat" : 40,
                    "lon" : -70
                }
            }
        }
    }
}
        else:
            query['query']={"match": {"activity_types": self.map_sports(self.sports)}}

# define the grammar
and_ = CaselessLiteral("and")
or_ = CaselessLiteral("or")
not_ = CaselessLiteral("not")
lookahead=oneOf("in with within near")
locationExpr = OneOrMore(Word(alphas) | ',')
sportsExpr = Group(OneOrMore(~lookahead + Word(alphas)))
nearExpr = Group(CaselessKeyword("near") + (CaselessKeyword("me") | locationExpr))
inExpr = CaselessKeyword("in") + locationExpr

units = oneOf("km m mile miles ac")
valueExpr = Word(nums).addParseAction(lambda term: int(t[0])) + Optional(units)
withinExpr = Group(CaselessKeyword("within") + valueExpr)
#withinExpr.setParseAction(WithinExpr)
searchTerm = Word(alphas) | quotedString.setParseAction( removeQuotes )
searchTerm.setParseAction(SearchTerm)
condExpr = searchTerm + Group(oneOf('< > >= <= =') | oneOf('more less') + 'than' )  + valueExpr | (oneOf('more less') + 'than') + Word(nums) + searchTerm | searchTerm
searchExpr = operatorPrecedence( condExpr,
 [
 (not_, 1, opAssoc.RIGHT, SearchNot),
 (and_, 2, opAssoc.LEFT, SearchAnd),
 (or_, 2, opAssoc.LEFT, SearchOr),
 ])
withExpr = CaselessKeyword("with") + searchExpr
queryString = sportsExpr('sports') + Optional(inExpr)('inexpr') + Optional(withExpr)('withexpr') + Optional(withinExpr | nearExpr)('rangeexpr')
queryString.addParseAction(QueryString)
# test the grammar and selection logic
test = """\
 ski resorts within 20miles
 ski places near me
 ski places in MA
 ski places with more than 100 trails""".splitlines()
for t in test:
 try:
  evalStack = (queryString + stringEnd).parseString(t)
 except ParseException, pe:
  print "Invalid search string"
  continue
 print "Search string:", t
 print "Eval stack: ", evalStack
 #evalExpr = evalStack.generateSetExpression()
# print "Eval expr: ", evalExpr