# Search methods
# "Hello"
import search
import time

ab = search.GPSProblem('A', 'B'
                       , search.romania)

first = time.time()
print(search.breadth_first_graph_search(ab).path())
second = time.time()
print(search.depth_first_graph_search(ab).path())
third = time.time()
print(search.branch_and_bound_search(ab).path())
fourth = time.time()
print(search.branch_and_bound_subestimation_search(ab).path())
fifth = time.time()

print('First search = {:.8f}, Second search = {:.8f}'.format(float(second-first), float(third-second)))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
