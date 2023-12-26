# Search methods
# "Hello"
import search
import time

def srch(problem):
    first = time.time()
    print("BFS")
    print(search.breadth_first_graph_search(problem).path())
    second = time.time()
    print("DFS")
    print(search.depth_first_graph_search(problem).path())
    third = time.time()
    print("BnB")
    print(search.branch_and_bound_search(problem).path())
    fourth = time.time()
    print("BnB+Subestimación")
    print(search.branch_and_bound_subestimation_search(problem).path())
    fifth = time.time()

    print('\nFirst search = {:.8f}, Second search = {:.8f}'.format(float(second-first), float(third-second)))
    print('Third search = {:.8f}, Fourth search = {:.8f}'.format(float(fourth-third), float(fifth-fourth)))
print("----- A B")
srch(search.GPSProblem('A', 'B', search.romania))
print("----- O E")
srch(search.GPSProblem('O', 'E', search.romania))
print("----- G Z")
srch(search.GPSProblem('G', 'Z', search.romania))
print("----- N D")
srch(search.GPSProblem('N', 'D', search.romania))
print("----- M F")
srch(search.GPSProblem('M', 'F', search.romania))


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
