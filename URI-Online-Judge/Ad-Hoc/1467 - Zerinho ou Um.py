while True:
  try:
    A, B, C = input().split()

    if A != B and B == C:
    	print("A")
    elif B != A and A == C:
    	print("B")
    elif C != A and A == B:
    	print("C")
    else:
    	print("*")
    

  except EOFError:
    break
