# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.
class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return a String representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These Strings
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName().
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(String givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will#not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # @param problem the RavensProblem your agent should solve
    # @return your Agent's answer to this problem
    def Solve(self,problem):
        print ''
        print '***************************************************************'
        print 'Problem Name:   ' + problem.getName()

        problemType = problem.getProblemType()
        print 'Problem Type:   ' + problemType
        print 'Correct Answer: ' + problem.correctAnswer

        figures = problem.getFigures()
        figureA = figures.get("A")
        figureB = figures.get("B")
        figureC = figures.get("C")
        
        objectsA = figureA.objects
        objectsB = figureB.objects
        objectsC = figureC.objects
        
        d = getProblemDictionary(problem)
        attributesA = d[figureA.getName()]
        attributesB = d[figureB.getName()]
        attributesC = d[figureC.getName()]


        if problemType == '2x1':
            pass

        elif problemType == '2x2':    
            pass

        elif problemType == '3x1':
            pass

        print '***************************************************************'
        print ''

        return "6"


def getProblemDictionary(problem):
    d = {}

    figures = problem.getFigures()
    for f in figures:
        objects = figures.get(str(f)).objects
        d[f] = {}

        for o in objects:
            attributes = o.attributes
            d[f][o.getName()] = {}

            for a in attributes:
                d[f][o.getName()][a.getName()] = a.getValue()

    return d