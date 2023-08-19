def arithmetic_arranger(problems):

    
  
    if len(problems) > 5:
      return 'Error: Too many problems.'
    else:
      x = 0
      while x < len(problems):
        if problems[x].split()[1] != '+' and problems[x].split()[1] != '-':
          return "Error: Operator must be '+' or '-'."
        else:
          x += 1
          try:
            int(problems[x].split()[0])
            int(problems[x].split()[2])
          except:
            return 'Error: Numbers must only contain digits.'
          
      pb0 = eval(problems[0])
      arranged_problems = f'    {problems[0].split()[0]}\n{problems[0].split()[1]}  {problems[0].split()[2]}\n------\n   {pb0}'

      return arranged_problems