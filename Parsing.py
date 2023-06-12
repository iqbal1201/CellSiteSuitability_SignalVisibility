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
    result_pars = add_cat.split("; ")[0]
    result_pars_n = result_pars.split(" '")[0]
    return result_pars_n



def ParsCat2_cat(add_cat):
    result_pars = add_cat.split("; ")[1]
    result_pars_n = result_pars.split(" '")[1]
    return result_pars_n.replace("'", " ")



# Correct Function for Parsing POI
def parsing_num(fieldcat, no_order):
    if ';' in fieldcat:
         if no_order -1 < len(fieldcat.split("; ")):
              result_pars = fieldcat.split("; ")[no_order - 1]
              result_pars_n = result_pars.split(" '")[0]
              return result_pars_n
         else:
              return None
    else:
         if no_order != 1:
              return None
         else:
              result_pars_n = fieldcat.split(" '")[0]
              return result_pars_n


def parsing_cat(fieldcat, no_order):
     if ';' in fieldcat:
          if no_order -1 < len(fieldcat.split("; ")):
               result_pars = fieldcat.split("; ")[no_order -1]
               result_pars_n = result_pars.split(" '")[1]
               return result_pars_n.replace("'", "")
          else:
              return None
     else:
          if no_order != 1:
               return None
               
          else:
              result_pars_n = fieldcat.split(" '")[1]
              return result_pars_n.replace("'", "")
         