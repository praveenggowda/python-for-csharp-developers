class InsufficientFundsException(Exception): 
    pass

class DuplicateTransactionException(Exception):
    pass

class InvalidTransactionTypeException(Exception):
    pass

class NegativeAmountException(Exception):
    pass