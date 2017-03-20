#import sys
import abc
import numpy

class NotAString(Exception):
    pass

class NotANumber(Exception):
    pass

class DenominatorIsZero(Exception):
    pass

class AbstractCalculator(object):
    __metaclass__ = abc.ABCmeta
    @abc.abstractmethod
    def Add(self,arg1,arg2):
        """adds two numbers"""
    def Sub(self,arg1,arg2):
        """substracts two numbers"""
    def Multiply(self,arg1,arg2):
        """multiplies two numbers"""
    def Div(self, arg1, arg2):
        """divides two numbers"""
    def Derivative(self,func,order):
        """returns derivative"""

class Calculator(AbstractCalculator):
    def Add(self,arg1,arg2):
        if not (self._is_number(arg1) or self._is_number(arg2)):
            raise NotANumber()
        return arg1+arg2
    def Sub(self,arg1,arg2):
        if not (self._is_number(arg1) or self._is_number(arg2)):
            raise NotANumber()
        return arg1-arg2
    def Multiply(self,arg1,arg2):
        if not (self._is_number(arg1) or self._is_number(arg2)):
            raise NotANumber()
        return arg1*arg2
    def Div(self,arg1,arg2):
        if not (self._is_number(arg1) or self._is_number(arg2)):
            raise NotANumber()
        eps=0.000001
        if ((arg2 < 0+eps) and (arg2 > 0-eps)):
            raise DenominatorIsZero()
        return arg1/arg2
    def Derivative(self,func,order):
        if not self._is_number(order):
            raise NotANumber()
        if not self._is_string(func):
            raise NotAString()
        return numpy.derivative(func, order)
    def _is_number(self,number):
        return isinstance(number,int)
    def _is_string(self,string):
        return isinstance(string,str)


