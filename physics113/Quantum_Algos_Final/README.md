# Quantum Speed-Up: Testing Algorithmic Advantages and Potential Applications

#### Authors: Ivan Ge and Devin Gupta

#### Course: Physics 113 (Computational Physics)

---

## Motivation

This project explores the practical advantages of quantum algorithms over classical counterparts in the fields of factorization and search. Quantum computing has shown promise in solving specific types of problems more efficiently than classical computing. By investigating Shor's algorithm for factorization and Grover's algorithm for search, we aim to understand the computational benefits and potential applications of quantum algorithms.

## Project Overview

### Factorization (Shor's Algorithm)

Shor's algorithm is a quantum algorithm for integer factorization, which has profound implications for cryptography. Classical algorithms for factoring large integers are inefficient and time-consuming, making them infeasible for very large numbers. Shor's algorithm, on the other hand, can factorize integers in polynomial time, posing a significant threat to classical encryption methods that rely on the difficulty of factorization, such as RSA.

#### Key Notes:

- **3 implementations**: Here we compare a fully classical factorization method, a classical implementation of Shor's factorization method and a semi-quantum implementation of Shor's Factorization method.
- **Comparision Parameters:** We primarily compare the three implementations of factorization on their time for inputs of various sizes.
- **Folder Structure**: As you explore the Shor's implementations, try to remain primarily in the shor.ipynb notebook. This includes the majority of our contribution, and from this runner we've imported some updated/enhanced implementations of *Pavón*'s Quantum Shor.

#### Potential Applications:

Here we considered a contrived example in which a group of physicist engineers attempt to build a multi-dimensional animal stable. As we target some specific square footage (ex. 781 sq ft), we consider how can we maximize the number of dimensions our stable exists in, while minimizing the length of each side of our stable (including dimensional floors). As a result, factorization allows us to find the smallest lengths, increase the dimensions and consider larger and larger square footages.

### Search (Grover's Algorithm)

Grover's algorithm is designed for unstructured search problems, providing a quadratic speedup over classical search algorithms. While classical algorithms need \(O(N)\) time to search an unsorted database of \(N\) entries, Grover's algorithm can find the desired entry in \(O(\sqrt{N})\) time.

#### Key Notes:

* **Grover’s Implementation**: Code was built on various basic implementations of Grover’s algorithm using Qiskit, primarily using Qiskit’s GroverOperator library to perform iterations of Grover’s algorithm. Various add-ons are included to test code on Qiskit’s QASM simulator, fake backends, as well as on real IBM quantum hardware.

## Citations/References

1. **Shor's Algorithm**:

   - *Circuit for Shor's algorithm using 2n+3 qubits* by *Stephane Beauregard*: [https://arxiv.org/abs/quant-ph/0205095](https://arxiv.org/abs/quant-ph/0205095).
   - *Quantum Shor's algorithm* by *Juan Manuel Pavón*: [https://github.com/jmpr1991/Shor_algorithm](https://github.com/jmpr1991/Shor_algorithm).
   - *Second Quantum Shor's algorithm* by *Mattia Mancassola*: [https://github.com/mett29/Shor-s-Algorithm?tab=readme-ov-file](https://github.com/mett29/Shor-s-Algorithm?tab=readme-ov-file).
   - *Shor’s Algorithm (for Dummies)* by *Kaustubh Rakhade*: [https://kaustubhrakhade.medium.com/shors-factoring-algorithm-94a0796a13b1](https://kaustubhrakhade.medium.com/shors-factoring-algorithm-94a0796a13b1).
   - *Sympy Classical Factorization* in *Number Theory Library*: [https://github.com/sympy/sympy/blob/79d7b3ef4b5e2796da6458effa7fb3427a73f2c9/sympy/ntheory/factor_.py#L1052](https://github.com/sympy/sympy/blob/79d7b3ef4b5e2796da6458effa7fb3427a73f2c9/sympy/ntheory/factor_.py#L1052).
2. **Grover's Algorithm**:

- *Concepts of Grover's Algorithm* by *Microsoft Azure Quantum*: [https://learn.microsoft.com/en-us/azure/quantum/concepts-grovers](https://learn.microsoft.com/en-us/azure/quantum/concepts-grovers).
- *Fundamentals of Quantum Algorithms: Grover's Algorithm* by *IBM Quantum*: [https://learning.quantum.ibm.com/course/fundamentals-of-quantum-algorithms/grovers-algorithm](https://learning.quantum.ibm.com/course/fundamentals-of-quantum-algorithms/grovers-algorithm).
- *Grover's Algorithm Implementation* in *Qiskit Textbook*: [https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/grover.ipynb](https://github.com/Qiskit/textbook/blob/main/notebooks/ch-algorithms/grover.ipynb).
- *Image Processing with FRQI and NEQR* in *Qiskit Textbook*: [https://github.com/Qiskit/textbook/blob/main/notebooks/ch-applications/image-processing-frqi-neqr.ipynb](https://github.com/Qiskit/textbook/blob/main/notebooks/ch-applications/image-processing-frqi-neqr.ipynb).
- *Grover’s Algorithm: Quantum Database Search* by *IEEE*: [https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&amp;arnumber=8622457](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8622457).

---

By understanding and implementing Shor's and Grover's algorithms, this project demonstrates the potential of quantum computing to solve complex problems more efficiently than classical methods. Through our exploration, we aim to contribute to and explore the growing field of computational physics and the development of quantum technologies.
