Task 3  
Report


Part One :
In Part 1 , we used GraphInterface setting to implement the DiGraph class , we further implemented Edge class and Node class for implementing DiGraph Class.DiGraph class has following significant functions
•	add_node
•	remove_node
•	remove_edge
•	add_edge
•	all_out_edges_of_node
•	all_in_edges_of_node
In DiGraphtest.py  we checked every function we implemented in DiGraph class and showed using UnitTesting. 

Part Two :
In Part 2 , we implemented GraphAlgo using GraphAlgoInterface class to calculate the 
•	shortest_path
•	connected_component
•	connected_components
Shortest Path is calculated using Dijkstrra algorithm , this function takes two function and returns the Tuple[float, list]
In samilar way , other two functions were implemented.

Part Three :
In Part 3 , we make comparisons with pyhton based NetworkX library implementation of the three functions , java based implementation in task.2 and our this implementation.
Java based approach was relatively found slow and NetworkX based approach performed better in all three functions .
