def re_base(base: object):
    return base 


re_base(object)
re_base(10)
re_base('String')
re_base(bool)


def re_base_feat(base: str):
    return abs(len(base) / 2.5)
    
re_base_feat('Hey')
re_base_feat('Hommie')
re_base_feat('What is')
re_base_feat('Crackin`?')