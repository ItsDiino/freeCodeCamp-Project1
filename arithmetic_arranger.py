def arithmetic_arranger(problems, solve=False):

    # Checks if there are more than 5 problems
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    top = ""
    bottom = ""
    lines = ""
    totals = ""

    for p in problems:
      fnumber = p.split()[0]
      operator = p.split()[1]
      snumber = p.split()[2]

      # Error checking
      if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."
      elif len(fnumber) > 4 or len(snumber) > 4:
        return "Error: Numbers cannot be more than four digits."
      else:
        try:
          int(fnumber)
          int(snumber)
        except:
          return 'Error: Numbers must only contain digits.'
          
      # Get total of correct function
      total = f'{int(fnumber)} {operator} {int(snumber)}'
      total = eval(total)
      # Get distance for longest operator
      operatorDistance = max(len(fnumber), len(snumber)) + 2

      snumber = operator + snumber.rjust(operatorDistance - 1)
      top = top + fnumber.rjust(operatorDistance) + (4 * " ")
      bottom = bottom + snumber + (4 * " ")
      lines = lines + len(snumber) * "-" + (4 * " ")
      totals = totals + str(total).rjust(operatorDistance) + (4 * " ")

      
    arranged_problems = f'{top}\n{bottom}\n{lines}'
    if solve == True:
      arranged_problems = f'{arranged_problems}\n{totals}'

    return arranged_problems