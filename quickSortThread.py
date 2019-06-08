import sys, timeit, threading

def encontra_pivo(vetor, ini, fim):
  meio = (int+fim)//2
  
  if(((vetor[meio]>vetor[ini]) and (vetor[meio]<vetor[fim])) or ((vetor[meio]>vetor[fim]) and (vetor[ini]<vetor[meio]))):
    return meio
  elif(((vetor[ini]>vetor[meio]) and (vetor[ini]<vetor[fim])) or ((vetor[ini]>vetor[fim] ) and (vetor[ini]<vetor[meio]))):
    return ini
  else:
    return fim
  
def trocar(arr, a, b):
  aux = arr[a]
  arr[a] = arr[b]
  arr[b] = aux
  
