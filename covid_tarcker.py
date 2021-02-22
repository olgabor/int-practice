"""Covid-19 tracking

We're doing COVID-19 tracking prototype.

We have several persons located in two-dimensional map.
Each person record has a unique PERSON, a set of (X, Y)
coordinates, and a `DISTANCE_RADIUS`. The `DISTANCE_RADIUS` represents the area
around the `PERSON` that will infect person if another `PERSON` in it's `DISTANCE_RADIUS`


Need to write a function which takes list of PERSON's and
determines which one of them may infect biggest number of people
The function should return person's name and the total number of posible
people infected

"""

from dataclasses import dataclass
from math import sqrt
from typing import Sequence

import pdb



@dataclass
class Person:
    name: str
    x: float
    y: float
    dictance_radius: float

    def distance(self, other: "Person") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)



persons = [
    Person("C", 7, 13, 3),
    Person("O", 6.5, 17, 5),
    Person("V", 12, 10, 4.5),
    Person("I", 14.5, 7, 3.5),
    Person("D", 17, 9, 2),
    Person("D1", 7, 11, 2.5),
    Person("D9", 8.5, 11.5, 3),
]


def most_persons(persons: Sequence[Person]) -> (str, int):
  """Finds the largest infection spread.

  Returns the name of the starting person, and the number of persons
  infeted.
  """


  graph={}
  #pdb.set_trace()

  #populating the dictionary with each person and distance (calculated by )
  #if it less than dictance_radius
  #{'C': []}
  #graph[orig_pc.name].append(all_pc.name) => {'C': ['D1', 'D9'], etc}
  for orig_pc in persons:
    graph[orig_pc.name]=[]
    for all_pc in persons:
      if orig_pc == all_pc:
        continue

      if orig_pc.distance(all_pc)<=orig_pc.dictance_radius:
#        pdb.set_trace()
        graph[orig_pc.name].append(all_pc.name)



 # pdb.set_trace()
  print("We got graph", graph)
  #{'C': ['C', 'D1', 'D9'], 'O': ['C', 'O'], 'V': ['V', 'I', 'D9'], 'I': ['I', 'D'],
  #'D': ['D'], 'D1': ['C', 'D1', 'D9'], 'D9': ['C', 'D1', 'D9']}
  chain={}
  for orig_pc in persons:
#    pdb.set_trace()
    q1=[]
    chain[orig_pc.name]=[]
    q1.append(orig_pc.name)
    while (q1):
      new_p=q1.pop()
      for p in graph[new_p]:
        if not p in chain[orig_pc.name]:
    #      pdb.set_trace()
          q1.append(p)
          chain[orig_pc.name].append(p)
  pdb.set_trace()

  return (sorted([(k,len(v)) for k,v in chain.items()], key=lambda x: x[1],reverse=True)[0])


print(most_persons(persons) == ("V", 5))


# chain
#{'C': ['C', 'D1', 'D9'], 'O': ['C', 'O', 'D1', 'D9'], 'V': ['V', 'I', 'D9', 'C', 'D1', 'D'],
# 'I': ['I', 'D'], 'D': ['D'], 'D1': ['C', 'D1', 'D9'], 'D9': ['C', 'D1', 'D9']}


#sorted([(k,len(v)) for k,v in chain.items()], key=lambda x: x[1],reverse=True)
#[('V', 6), ('O', 4), ('C', 3), ('D1', 3), ('D9', 3), ('I', 2), ('D', 1)]

# (sorted([(k,len(v)) for k,v in chain.items()], key=lambda x: x[1],reverse=True)[0])
#('V', 6)
