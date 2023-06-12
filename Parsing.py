# Script in ArcGIS

def notDigit(n):
    result = ''.join([i for i in n if not i.isdigit()])
    return result



def ParsCat1_num(add_cat):
    result_pars = add_cat.split("; ")[0]
    result_pars_n = result_pars.split(" '")[0]
    return result_pars_n

def ParsCat1_cat(add_cat):
    result_pars = add_cat.split("; ")[0]
    result_pars_n = result_pars.split(" '")[1]
    return result_pars_n.replace("'", " ")


def ParsCat2_num(add_cat):
    result_pars = add_cat.split("; ")[1]
    result_pars_n = result_pars.split(" '")[0]
    return result_pars_n

def ParsCat2_cat(add_cat):
    result_pars = add_cat.split("; ")[1]
    result_pars_n = result_pars.split(" '")[1]
    return result_pars_n.replace("'", " ")