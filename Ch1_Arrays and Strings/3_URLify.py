
def URLify(st):

    # li1 takes each word according to the spaces, so in the list it is known that after each ele there is a space
    li1 = st.split()
    li2 = []

    for i, w in enumerate(li1):
        if(i == len(li1)-1):
            li2.append(w)
        else:
            li2.append(w)
            li2.append("%20")

    res = ''.join(li2)

    return res


st = "I am Sim"
print(URLify(st))
