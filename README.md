# Coursera: Data Structures and Algorithms Specialization

Solutions for [Data Structures and Algorithms Specialization](https://www.coursera.org/specializations/data-structures-algorithms)

Author: [Huy Vo](https://www.github.com/huyvohcmc)

The below solutions is **for reference only**. Please design and implement your own algorithms to pass the courses.

---

## [Course 1. Algorithmic Toolbox](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithmic-toolbox)

#### Week 1. Introduction

Upon completing this programming assignment you will be able to:

1. Implement solutions that work much more faster than straightforward solutions for the following com-
   putational problems:
   (a) compute a small Fibonacci number;
   (b) compute the last digit of a large Fibonacci number;
   (c) compute a huge Fibonacci number modulo m;
   (d) compute the greatest common divisor of two integers;
   (e) compute the least common multiple of two integers.
2. See the huge difference between a slow algorithm and a fast one.
3. Implement algorithms covered in the lectures, design new algorithms.
4. Practice implementing, testing, and debugging your solution. In particular, you will find out how in
   practice, when you implement an algorithm, you bump into unexpected questions and problems not
   covered by the general description of the algorithm. You will also check your understanding of the
   algorithm itself and most probably see that there are some aspects you did not think of before you
   had to actually implement it. You will overcome all those complexities, implement the algorithms, test
   them, debug, and submit to the system. Remember the advice (link) we gave you in the first module
   about testing your programs and feel free to return to those videos or parts of them again while working
   on your assignment. In the end of this document you will find also general recommendations on solving
   algorithmic problems.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/01_introduction_problems.pdf)

- [Small Fibonacci Number](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/fib.py)
- [The Last Digit of a Large Fibonacci Number](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/fibonacci_last_digit.py)
- [Greatest Common Divisor](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/gcd.py)
- [Least Common Multiple](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/lcm.py)
- [Huge Fibonacci Number modulo m](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/1-intro-starter-files/fibonacci_huge.py)

#### Week 2. Greedy Algorithms

Upon completing this programming assignment you will be able to:

1. Apply greedy strategy to solve various computational problems. This will usually require you to design
   an algorithm that repeatedly makes the most profitable move to construct a solution. You will then
   need to show that the moves of your algorithm are safe, meaning that they are consistent with at least
   one optimal solution.
2. Implement an efficient algorithm to optimally pack your bag before going to a hike.
3. Design and implement a greedy algorithm for a novel computational problem.
4. Design and implement a greedy algorithm for changing money optimally.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/02_greedy_algorithms_problems.pdf)

- [Changing Money](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/change.py)
- [Fractional Knapsack](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/fractional_knapsack.py)
- [Minimum Dot Product](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/dot_product.py)
- [Covering Segments by Points](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/covering_segments.py)
- [Pairwise Distinct Summands](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/2_greedy_algorithms_starter_files/different_summands.py)

#### Week 3. Divide and Conquer

Upon completing this programming assignment you will be able to:

1. Apply the divide-and-conquer technique to solve various computational problems efficiently. This will
   usually require you to design an algorithm that solves a problem by splitting it into several disjoint
   subproblems, solving them recursively, and then combining their results to get an answer for the initial
   problem.
2. Implement the binary search algorithm that is used to search keys in sorted data.
3. Implement the quick sort algorithm which is one of the fastest and most commonly used in practice
   sorting algorithms.
4. Design and implement efficient divide-and-conquer algorithms for novel computational problems.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/3_divide_and_conquer_problems.pdf)

- [Binary Search](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/binary_search.py)
- [Majority Element](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/majority_element.py)
- [Sorting: 3-Way Partition](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/sorting.py)
- [Number of Inversions](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/inversions.py)
- [Points and Segments](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/points_and_segments.py)

#### Week 4. Dynamic Programming

Upon completing this programming assignment you will be able to:

1. Apply the dynamic programming technique to solve various computational problems. This will usu-
   ally require you to design an algorithm that solves a problem by solving a collection of overlapping
   subproblems (as opposed to the divide-and-conquer technique where subproblems are usually disjoint)
   and combining the results.
2. Implement an efficient algorithm to optimally fill in a box with bars of gold.
3. Implement an efficient algorithm to compute the difference between two files or strings. Such algorithms
   are widely used in spell checking programs and version control systems.
4. Implement a more advanced algorithm for computing the maximum value of an arithmetic expression.
5. Design and implement a dynamic programming algorithm for a novel computational problem.
6. See two examples of an optimization problem where a natural greedy strategy produces a non-optimal
   result. You will see that a natural greedy move for these problems is not safe.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/04_dynamic_programming_problems.pdf)

- [Primitive Calculator](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/primitive_calculator.py)
- [Take as Much Gold as Possible](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/knapsack.py)
- [Compute the Edit Distance Between Two Strings](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/edit_distance.py)
- [Maximize the Value of an Arithmetic Expression](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/placing_parentheses.py)
- [Longest Common Subsequence of Three Sequences](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/4-dynprog-starter-files/lcs3.py)

---

## [Course 2. Data Structures](https://github.com/huyvohcmc/coursera-dsa/tree/master/data-structures)

#### Week 1. Basic Data Structures

Upon completing this programming assignment you will be able to:

1. Apply the basic data structures you’ve just studied to solve the given algorithmic problems.
2. Given a piece of code in an unknown programming language, check whether the brackets are used
   correctly in the code or not.
3. Implement a tree, read it from the input and compute its height.
4. Simulate processing of computer network packets.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA1/_cf0138d143798bcef9fc6c036499066f_Programming-Assignment-1.pdf)

- [Check brackets in the code](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA1/check_brackets.py)
- [Compute tree height](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA1/tree-height.py)
- [Network packet processing simulation](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA1/process_packages.py)

#### Week 2. Priority Queues and Disjoint Sets

Upon completing this programming assignment you will be able to:

1. Apply priority queues and disjoint sets to solve the given algorithmic problems.
2. Convert an array into a heap.
3. Simulate a program which processes a list of jobs in parallel.
4. Simulate a sequence of merge operations with tables in a database.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA2/_bef36cc5a64d08ee09d3da280ab6784f_Programming-Assignment-2.pdf)

- [Convert array into heap](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA2/build_heap.py)
- [Parallel processing](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA2/job_queue.py)
- [Merging tables](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA2/merging_tables.py)

#### Week 3. Hash Tables and Hash Functions

Upon completing this programming assignment you will be able to:

1. Apply hashing to solve the given algorithmic problems.
2. Implement a simple phone book manager.
3. Implement a hash table using the chaining scheme.
4. Find all occurrences of a pattern in text using RabinKarp's algorithm.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA3/_d11e054a8f57521f60e584860cbc752c_Programming-Assignment-3.pdf)

- [Phone book](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA3/phone_book.py)
- [Hashing with chains](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA3/hash_chains.py)
- [Find pattern in text](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA3/hash_substring.py)

#### Week 4. Binary Search Trees

Upon completing this programming assignment you will be able to:

1. Apply binary search trees to solve the given algorithmic problems.
2. Implement in-order, pre-order and post-order traversal of a binary tree.
3. Implement a data structure to compute range sums.
4. Implement a data structure that can store strings and quickly cut parts and patch them back.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA4/_e30b0d9dce7c168f24fb39cd26fa7624_Programming-Assignment-4.pdf)

- [Binary tree traversals](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA4/tree-orders.py)
- [Set with range sums](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA4/set_range_sum.py)
- [Rope](https://github.com/huyvohcmc/coursera-dsa/blob/master/data-structures/Starters%20PA4/rope.py)

---

## [Course 3. Algorithms on Graphs](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs)

#### Week 1. Decomposition of Graphs 1

Upon completing this programming assignment you will be able to:

1. find an exit from a maze;
2. find the number of exits needed for a maze;

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%201/09_graph_decomposition_problems_1.pdf)

- [Finding an Exit from a Maze](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%201/reachability.py)
- [Adding Exits to a Maze](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%201/connected_components.py)

#### Week 2. Decomposition of Graphs 2

Upon completing this programming assignment you will be able to:

1. check consistency of Computer Science curriculum;
2. find an order of courses that is consistent with prerequisite dependencies;
3. check whether any intersection of a city is reachable from any other intersection.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%202/_ad976e670709c6bf7d7d12c33f3353b3_09_graph_decomposition_problems_2.pdf)

- [Checking Consistency of CS Curriculum](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%202/acyclicity.py)
- [Determining an Order of Courses](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%202/toposort.py)
- [Checking Whether Any Intersection in a City is Reachable from Any Other](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Decomposition%20of%20Graphs%202/strongly_connected.py)

#### Week 3. Paths in Graphs 1

Upon completing this programming assignment you will be able to:

1. compute the minimum number of flight segments to get from one city to another one;
2. check whether a given graph is bipartite.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Most%20Direct%20Route/_39569bafe56d93c9b089abdb092f8ea9_10_paths_in_graphs_problems_1.pdf)

- [Computing the Minimum Number of Flight Segments](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Most%20Direct%20Route/bfs.py)
- [Checking whether a Graph is Bipartite](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Most%20Direct%20Route/bipartite.py)

#### Week 4. Paths in Graphs 2

Upon completing this programming assignment you will be able to:

1. compute the minimum cost of a flight from one city to another one;
2. detect anomalies in currency exchange rates;
3. compute optimal way of exchanging the given currency into all other currencies.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Fastest%20Route/_ce9cda3b7147b43293eb494336e89f84_10_paths_in_graphs_problems_2.pdf)

- [Computing the Minimum Cost of a Flight](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Fastest%20Route/dijkstra.py)
- [Detecting Anomalies in Currency Exchange Rates](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Fastest%20Route/negative_cycle.py)
- [Exchanging Money Optimally](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Fastest%20Route/shortest_paths.py)

#### Week 5. Minimum Spanning Trees

Upon completing this programming assignment you will be able to:

1. connect the given cities by roads of minimum total length such that there is a path between any two
   cities;
2. compute an optimal clustering of the given set of objects.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Minimum%20Spanning%20Trees/_8b8222a155c976cc2eec60a2dba332a4_11_spanning_trees_problems.pdf)

- [Clustering](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Minimum%20Spanning%20Trees/clustering.py)
- [Building Roads to Connect Cities](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Minimum%20Spanning%20Trees/connecting_points.py)

#### Week 6. Advanced Shortest Paths Project (Optional)

Upon completing this programming assignment you will be able to:

1. implement Bidirectional Dijkstra and use it to compute distances in social networks very quickly;
2. implement A* search algorithm and apply it to compute distances in road networks faster than the
   classic algorithms do;
3. implement Contraction Hierarchies algorithm and apply it to preprocess large road networks and then
   compute distances in them much faster;
4. implement even more heuristics speeding up Contraction Hierarchies and solve even bigger road net-
   works;
5. use your Contraction Hierarchies implementation to go further and solve the classical logistics problem
   (called Travelling Salesman Problem): find the optimal path for a truck leaving the depot to visit a list
   of stores, deliver the goods to them and return to the depot.

[Instruction](https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/_102641bd38de305aa091c117fd776343_Advanced-Shortest-Paths.pdf)

- [Friend Suggestion](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/friend_suggestion)
- [Compute Distance Faster Using Coordinates](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/dist_with_coords)
- [Compute Distance with Preprocessing](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/dist_preprocess_small)
- [Compute Distance with Preprocessing on Larger Road Networks](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/dist_preprocess_large)
- [Travelling Salesman Problem](https://github.com/huyvohcmc/coursera-dsa/tree/master/algorithms-on-graphs/Advanced%20Shortest%20Paths/travelling_salesman_problem)

---

## Contributing

If you have tips to improve something e.g. README, code refactoring, etc., don't hesitate to create a pull request.
