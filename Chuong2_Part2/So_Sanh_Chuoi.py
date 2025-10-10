def so_sanh (s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print (s1, "dai hon", s2)
    elif len1 <len2:
        print (s1, "ngan hon", s2)
    else:
        print (s1, "bang", s2)