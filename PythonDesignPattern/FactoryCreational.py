# This allows interface or class to create an object but lets the subclass decide which instance to instantiate .

# In factory , the actors are :
# Factory Class(Creator Class) : which defines the rules to create an object . It is the abstract class or interface to be inherited by the Concrete Creator class .
# (Concrete Creator class) : Inherits the creator class and also returnt the concrete product after executing the corresponding factory method .


# instantiating a property
# business logic
# Polymorphism : If we have a factory that wraps the business logic for instantiation and that factory is an instance , then we can replace/swap that instance
# for another factory .



# PlanFactory Interface declares method recommend_insurance


# PlanFactory  - Factory class
# get_recommended_plan() - factory_method

# ComprehensiveFactory
# AccidentalConcreteFactory
# HeartInsuranceFactory
# PEDInsulinInsuranceFactory
# PEDNoninsulinInsuranceFactory


# Product - SuggestedPolicy

# ConcreteProduct -
# ComprehensivePolicy
# AccidentalConcreteFactory
# HeartInsuranceFactory
# PEDInsulinInsuranceFactory
# PEDNoninsulinInsuranceFactory
