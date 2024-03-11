def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : ", object.__class__)
    elif object.__class__ is float:
        print("Cheese : ", object.__class__)
    elif object.__class__ is int:
        print("Zero : ", object.__class__)
    elif object.__class__ is str and len(object) == 0:
        print("Empty : ", object.__class__)
    elif object.__class__ is bool:
        print("Fake : ", object.__class__)
    else:
        print("Type not found")

    return 1