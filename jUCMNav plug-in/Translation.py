#Translation.py
# Modified by Amal Ahmed Anda
from sympy import *
from MathToJava import *
from MathToC import *
from MathToCpp import *
from MathToJS import *
from MathToPython import *
from MathToMatlab import *
from MathToR import *
from MathToLang import *
init_printing()

''' translate Sympy formula into target language
	Java
	Matlab
	C
	C++
	JavaScript
	Python
    R
'''

def Translate(formula,dep,args,Type):

    i = 0
    for arg in args:
        arg = str(arg)+"="+"Symbol"+"("+"'"+str(arg)+"'"+")"
        i = i+1
        exec(arg)
        
    func = simplify(eval(formula)).evalf(4)
    #print "after func"
    #func=formula
    if ( "java" in Type):  #Type == "java" or Type == "All":
        convertToJava(jcode(func),dep,args).writeMath()
        print ('java')
        #if Type != "All":
        #   return
    if ( "python" in Type): #Type == "python"  or Type == "All":
        print ("python")
        from sympy.printing.pycode import (PythonCodePrinter,pycode)
        pr = PythonCodePrinter()
        convertToPy( pr.doprint(func),dep,args).writeMath()
        #if Type != "All":
        #   return
    if ( "javascript" in Type): #Type == "javascript"  or Type == "All":
        convertToJS(jscode(func),dep,args).writeMath()
        print ('js')
        #if Type != "All":
        #   return
    if ( "matlab" in Type): #Type == "matlab"  or Type == "All":
        print ('matlab')
        convertToMatlab(octave_code(func),dep,args).writeMath()
        #if Type != "All":
         #  return

    if ( "c" in Type): #Type == "c"  or Type == "All":
        convertToC(ccode(func),dep,args).writeMath()
        print ('c')
        #if Type != "All":
        #   return
    if ( "c++" in Type): #Type == "c++"  or Type == "All":
        convertToCpp(cxxcode(func),dep,args).writeMath()
        print ("c++")
        #if Type != "All":
         #  return
    if ( "r" in Type): #f Type == "r"  or Type == "All":
        convertToR(rcode(func),dep,args).writeMath()
        print ("R")
        #if Type != "All":
        #   return



'''
test
print Translate('E1=Min(E2,E3)',"Java")'''
