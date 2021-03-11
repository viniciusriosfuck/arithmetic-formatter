class Error(Exception):
    '''raise this when there's a error'''
    pass

def arithmetic_arranger(problems, boolean=False):
  arranged_problems = []

  assert type(problems) == list

  assert len(problems) > 0

  
  if len(problems) > 5:
    raise Error('Too many problems.')
 

  if boolean:
    # print(answer)
    pass





  


  return arranged_problems