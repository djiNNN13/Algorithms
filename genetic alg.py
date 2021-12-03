import networkx as nx   
from generate_graph import generate_arr
import random

class Individual (object):
    def __init__(self, gen, graph):

        self.gen = gen
        self.graph = graph

    def check_is_sulution(self):
        check_set={i for i in range(300)}
        check_set_2 = set()
        for i in range(len(self.gen)):
            if self.gen[i] == 1:
                check_set_2.add(i)
                for j in range(300):
                    if self.graph[i][j]==1:
                        check_set_2.add(j)

        return (check_set==check_set_2)


    def cross_person_1(self, parent):
        #1 point
        new_genome = self.gen[: round(len(self.gen)/2)] + parent[-round(len(parent)/2):]
        new_genome1 = parent[: round(len(self.gen)/2)] +  self.gen[-round(len(parent)/2):]
       
        #generate mutation
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome)-1)
            new_genome[select_gen] = 1 if new_genome[select_gen]==0 else 0
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome1)-1)
            new_genome1[select_gen] = 1 if new_genome1[select_gen]==0 else 0

        #create persons
        
        new_person = Individual(new_genome, self.graph)
        new_person1 = Individual(new_genome1, self.graph)

        return new_person, new_person1


    def cross_person_2(self, parent):
        #2 points
        new_genome = self.gen[: round(len(self.gen)/3)] +parent[round(len(parent)/3):round(len(parent)*2/3)]+ self.gen[-round(len(self.gen)/3):]
        new_genome1 = parent[: round(len(parent)/3)] +self.gen[round(len(self.gen)/3):round(len(self.gen)*2/3)]+ parent[-round(len(parent)/3):]
       
        #generate mutation
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome)-1)
            new_genome[select_gen] = 1 if new_genome[select_gen]==0 else 0
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome1)-1)
            new_genome1[select_gen] = 1 if new_genome1[select_gen]==0 else 0

        #create persons
        
        new_person = Individual(new_genome, self.graph)
        new_person1 = Individual(new_genome1, self.graph)

        return new_person, new_person1


    def cross_person_3(self, parent):
        #3 points
        new_genome = self.gen[: round(len(self.gen)/4)] + parent[round(len(parent)/4) : round(len(parent)/2)] + self.gen[round(len(self.gen)/2) : round(3*len(self.gen)/4)] + parent[-round(len(parent)/4):]
        new_genome1 = parent[: round(len(self.gen)/4)] +  self.gen[round(len(parent)/4) : round(len(parent)/2)] + parent[round(len(self.gen)/2) : round(3*len(self.gen)/4)] +  self.gen[-round(len(parent)/4):]
       
        #generate mutation
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome)-1)
            new_genome[select_gen] = 1 if new_genome[select_gen]==0 else 0
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome1)-1)
            new_genome1[select_gen] = 1 if new_genome1[select_gen]==0 else 0

        #create persons
        
        new_person = Individual(new_genome, self.graph)
        new_person1 = Individual(new_genome1, self.graph)

        return new_person, new_person1
    
    def cross_person_4(self, parent):
        #4 points
        new_genome = self.gen[: round(len(self.gen)/5)] + parent[round(len(parent)/5):round(len(parent)*2/5)] + self.gen[round(len(self.gen)*2/5):round(len(self.gen)*3/5)] + parent[round(len(parent)*3/5):round(len(parent)*4/5)] + self.gen[-round(len(self.gen)/5):]
        new_genome1 = parent[: round(len(parent)/5)] +  self.gen[round(len(self.gen)/5):round(len(self.gen)*2/5)] + parent[round(len(parent)*2/5):round(len(parent)*3/5)] + self.gen[round(len(self.gen)*3/5):round(len(self.gen)*4/5)]+ parent[-round(len(parent)/5):]
       
        #generate mutation
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome)-1)
            new_genome[select_gen] = 1 if new_genome[select_gen]==0 else 0
        if random.randint(1, 100)%20==0:
            select_gen = random.randint(0, len(new_genome1)-1)
            new_genome1[select_gen] = 1 if new_genome1[select_gen]==0 else 0

        #create persons
        
        new_person = Individual(new_genome, self.graph)
        new_person1 = Individual(new_genome1, self.graph)

        return new_person, new_person1


def generate_start_genome(graph, size=300):

    connect  = []
    for i in range(size):
        for j in range(i, size):
            connect.append((i,j))
    return connect

def generate_connection (graph):
    population = []

    for i in range (300):
        genome = [0]*300
        genome[i] = 1
        ind = Individual(genome, graph)

        population.append(ind)

    return population


def calculate(civ_1, civ_2, civ_3, civ_4):
    min_1 = 301
    arr1=[]

    min_2 = 301
    arr2=[]

    min_3 = 301
    arr3=[]

    min_4 = 301
    arr4=[]


    while len(civ_1)>= 1 :
        index_1_1 = random.randint(0, len(civ_1)-1)
        el_1_1 = civ_1[index_1_1]
        del civ_1[index_1_1]
        index_1_2 = random.randint(0, len(civ_1)-1)
        el_1_2 = civ_1[index_1_2]
        del civ_1[index_1_2]
        new_person, new_person1 = el_1_1.cross_person_1(el_1_2.gen)
        arr1.append(new_person)
        arr1.append(new_person1)

        if new_person.check_is_sulution() and sum(new_person.gen) < min_1:
            min_1 = sum(new_person.gen) 
            print(min_1)
        if new_person1.check_is_sulution() and sum(new_person1.gen) < min_1:
            min_1 = sum(new_person1.gen) 
            print(min_1)

        if len(civ_1)==1:
            arr1.append(civ_1[0]) 

            civ_1 = arr1[:]
            arr1=[]

        elif len(civ_1)==0:
            civ_1 = arr1[:]
            arr1=[]

    print(min_1)

    while len(civ_2)>= 1 :
        index_2_1 = random.randint(0, len(civ_2)-1)
        el_2_1 = civ_2[index_2_1]
        del civ_2[index_2_1]
        index_2_2 = random.randint(0, len(civ_2)-1)
        el_1_2 = civ_1[index_1_2]
        del civ_2[index_2_2]
        new_person, new_person1 = el_2_1.cross_person_1(el_2_2.gen)
        arr2.append(new_person)
        arr2.append(new_person1)

        if new_person.check_is_sulution() and sum(new_person.gen) < min_2:
            min_2 = sum(new_person.gen) 
            print(min_2)
        if new_person2.check_is_sulution() and sum(new_person2.gen) < min_2:
            min_2 = sum(new_person2.gen) 
            print(min_2)

        if len(civ_2)==1:
            arr2.append(civ_2[0]) 

            civ_2 = arr2[:]
            arr2=[]

        elif len(civ_2)==0:
            civ_2 = arr2[:]
            arr2=[]

    print(min_2)


    while len(civ_3)>= 1 :
        index_3_1 = random.randint(0, len(civ_3)-1)
        el_3_1 = civ_3[index_3_1]
        del civ_3[index_3_1]
        index_3_2 = random.randint(0, len(civ_3)-1)
        el_3_2 = civ_3[index_3_2]
        del civ_3[index_3_2]
        new_person, new_person1 = el_3_1.cross_person_1(el_3_2.gen)
        arr3.append(new_person)
        arr3.append(new_person1)

        if new_person.check_is_sulution() and sum(new_person.gen) < min_3:
            min_3 = sum(new_person.gen) 
            print(min_3)
        if new_person3.check_is_sulution() and sum(new_person3.gen) < min_3:
            min_3 = sum(new_person3.gen) 
            print(min_3)

        if len(civ_3)==1:
            arr3.append(civ_3[0]) 

            civ_3 = arr3[:]
            arr3=[]

        elif len(civ_3)==0:
            civ_3 = arr3[:]
            arr3=[]

    print(min_3)

    while len(civ_4)>= 1 :
        index_4_1 = random.randint(0, len(civ_4)-1)
        el_4_1 = civ_4[index_4_1]
        del civ_4[index_4_1]
        index_4_2 = random.randint(0, len(civ_4)-1)
        el_4_2 = civ_4[index_4_2]
        del civ_4[index_4_2]
        new_person, new_person1 = el_4_1.cross_person_1(el_4_2.gen)
        arr4.append(new_person)
        arr4.append(new_person1)

        if new_person.check_is_sulution() and sum(new_person.gen) < min_4:
            min_4 = sum(new_person.gen) 
            print(min_4)
        if new_person4.check_is_sulution() and sum(new_person4.gen) < min_4:
            min_4 = sum(new_person4.gen) 
            print(min_4)

        if len(civ_4)==1:
            arr4.append(civ_4[0]) 

            civ_4 = arr4[:]
            arr4=[]

        elif len(civ_4)==0:
            civ_4 = arr4[:]
            arr4=[]

    print(min_4)

if __name__ == "__main__":
    arr = generate_arr()
    print(arr)
    calculate(generate_connection(arr), generate_connection(arr), generate_connection(arr), generate_connection(arr))