Graf = {
  'S':[('U',10),('X',5)],
  'X':[('V',9),('Y',2),('U',3)],
  'U':[('V',1),('X',2)],
  'Y':[('V',6)],
  'V':[('Y',4)]
}

def Inicjalizacja(G,z): # juz rozumiem
  G1 = {}
  for elem in G:
    G1[elem] = float('inf')
  G1[z] = 0 
  return G1
  
def Extract_min(G,Q):
  mini = float('inf')
  smt = -1
  for s in G:
    if s in Q:
      if G[s] < mini:
        mini = G[s]
        smt = s
  return smt

def Izolacja_sasiadow(s,G):
  K = {}
  K[s] = []
  for elem in G[s]:
    K[s].append((elem[0],elem[1]))
  return K
  
def Relax(u,v,waga,G):
  if G[v] > waga + G[u]:
    G[v] = waga + G[u]
  return G
    
def Dijkstra(G,Z): 
  
  G1 = Inicjalizacja(G,Z)
  T = {}
  S = []
  Q = [elem for elem in G]
  
  while Q != [] :
    
    U = {v: G1[v] for v in G}
    u = Extract_min(U,Q)
    T = Izolacja_sasiadow(u,G)
    S.append(u)
    Q.remove(u)
    
    for v,waga in T[u]:
      G1 = Relax(u,v,waga,G1)
      
  return G1
  
print(Dijkstra(Graf,'S'))