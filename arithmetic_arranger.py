import re

class Error(Exception):
    '''raise this when there's a error'''
    pass

def arithmetic_arranger(problems, boolean=False):
  
  lst_first = []
  lst_second = []
  lst_dashes = []
  lst_result = []

  assert type(problems) == list
  assert len(problems) > 0
  
  if len(problems) > 5:
    raise Error('Too many problems.')

  for problem in problems:
    if re.search(r'[\+\-]', problem) is None:
      raise Error("Operator must be '+' or '-'.")
    elif re.search(r'[^\+\-\d\s]', problem) is not None:
      raise Error("Numbers must only contain digits.")
    elif re.search(r'\d{5}', problem) is not None:
      raise Error("Numbers cannot be more than four digits.")

    lst_problem = problem.split()

    n_chars = len(max(lst_problem, key=len))+2   
    
    lst_first.append(lst_problem[0].rjust(n_chars))
    lst_second.append(lst_problem[1]+lst_problem[2].rjust(n_chars-1))
    lst_dashes.append('-'*n_chars)

    lst_result.append(str(eval(problem)).rjust(n_chars))

  arranged_problems = f"""\
{'    '.join(lst_first)}
{'    '.join(lst_second)}
{'    '.join(lst_dashes)}"""
  if boolean:
    arranged_problems = arranged_problems + f"\n{'    '.join(lst_result)}"

  return arranged_problems