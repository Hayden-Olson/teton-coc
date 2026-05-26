# bank_account.py

def create_account(name, opening_balance=0):
    """
    Return a new account represented as a dict:
      {"name": name, "balance": int, "transactions": list}
    If opening_balance != 0, record ("opening_balance", opening_balance).
    Notice this is a TUPLE () rather than a LIST []. 
    A tuple is just an immutable version of a list.
    """
    # TODO: validate name and opening_balance when appropriate
    acct = {
        "name": name,
        # store integer balance
        "balance": 0,
        # transaction list
        "transactions": [],
    }
    if opening_balance != 0:
        # TODO: apply opening balance and record transaction
        raise NotImplementedError("TODO: apply opening_balance")
    return acct

def deposit(account, amount):
    """
    Add amount to account["balance"] and record ("deposit", amount).
    - amount must be a positive integer; otherwise raise ValueError.
    - modify account in-place and return True.
    """
    # TODO: implement deposit rules
    raise NotImplementedError("TODO: implement deposit")

def withdraw(account, amount):
    """
    Subtract amount from account["balance"] and record ("withdraw", amount).
    - amount must be a positive integer and <= balance; otherwise raise ValueError.
    - modify account in-place and return True.
    """
    # TODO: implement withdraw
    raise NotImplementedError("TODO: implement withdraw")

def transfer(from_account, to_account, amount):
    """
    Transfer amount from from_account to to_account.
    - both accounts must be valid account dicts (created by create_account)
    - amount must be positive integer and <= from_account balance
    - on success: mutate both accounts, record ("transfer_out", amount)
      in from_account and ("transfer_in", amount) in to_account, then return True.
    - on failure: raise ValueError without mutating accounts.
    """
    # TODO: implement transfer safely (validate before mutating)
    raise NotImplementedError("TODO: implement transfer")

def account_str(account):
    """
    Return a readable single-line summary like "Alice: 100"
    """
    # TODO: create and return the string
    raise NotImplementedError("TODO: implement account_str")