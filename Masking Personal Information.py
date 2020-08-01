def maskPII( S: str) -> str:
    if "@" in S:  # Email
        new = S.split("@")
        name1 = new[0]
        mask = "*****"
        return(name1[0].lower() + mask + name1[len(name1)-1].lower() + "@" + new[1])

    else:  #Phone number
        new = S
        remove = ['-','(',')','+',' ']
        for i in remove:
            new = new.replace(i, "")
        Last4 = new[-4:]

        if len(new) == 10:
            return ("***-***-"+ Last4)
        elif len(new) == 11:
            return ("+*-***-***-" + Last4)
        elif len(new) == 12:
            return ("+**-***-***-" + Last4)
        elif len(new) == 13:
            return ("+***-***-***-" + Last4)


print(maskPII("86-(10)12345678"))
