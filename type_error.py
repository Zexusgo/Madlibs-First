def check_string(x):
    try:
        if not isinstance(x,str):
            raise ValueError ("Please enter a name!")

        if not x.isalpha():
            raise ValueError ("Please enter a name!")
    
        return True
    except ValueError:
        
        print("Please enter a name")

        return False