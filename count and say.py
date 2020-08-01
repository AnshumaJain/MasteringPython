
def countAndSay(n) :

    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    else:
        val = countAndSay(n-1)
        prev = 0
        cur = 1
        count = 1
        output = ""
        while 1:
            if val[prev] == val[cur]:
                count += 1
                if cur == (len(val)-1):
                    output += str(count) + str(val[prev])
                    return output
            else:
                output += str(count) + str(val[prev])
                count = 1
                if cur == (len(val) - 1):
                    output += str(count) + str(val[cur])
                    return output
            prev = cur
            cur += 1



print(countAndSay(5))