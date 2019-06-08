#!/usr/local/bin/python3
import sys, timeit

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
  
def QuickSort(ini, fim, vetor):
  pos_pivo, i, j = int()
  if(fim-ini<2):
    if(fim-ini==1):
      if(vetor[ini]>vetor[fim]):
        trocar(vetor, ini, fim)
  else:
    pos_pivo = encontrar_pivo(vetor, ini, fim)
    troca(vetor, ini, fim)
    i = ini
    j = fim-1
    while(j>=i):
      while((i<=j) and (vetor[i]<vetor[fim])):
        i += 1
      while((j>=i)and(vetor[j]>vetor[fim])):
        j -= 1
      if(j>=i):
        troca(vetor, i, j)
        i += 1
        j -= 1
    trocar(vetor, i, fim)
    QuickSort(ini, i-1, vetor)
    QuickSort(i+1, fim, vetor)
    
def imprimeVetor(ptr):
   for i in range(ptr):
    print(i)
    
    
#leitura de dados
arr = [int(x) for x in input().split()]

#medição de tempo
print(timeit.timeit('QuickSort(0, len(arr)-1, arr)', number=1, globals=globals()), file=sys.stderr, end="S\n")

