def keep_numbers(l1):
    """This function keeps the numbers in a list and doesn't keep strings or characters"""
    l2=[l1[i] for i in range(len(l1)) if isinstance(l1[i],int)]
    return l2