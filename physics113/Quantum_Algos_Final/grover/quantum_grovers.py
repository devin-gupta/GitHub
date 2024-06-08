# Import necessary modules and libraries
import math
import time
import timeit
# Imports from Qiskit
from qiskit_aer import Aer, AerSimulator
from qiskit_aer.utils import transpile_noise_model
from qiskit import transpile, QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_aer.primitives import EstimatorV2
from qiskit_aer.noise import NoiseModel
from qiskit_ibm_runtime.fake_provider import FakeVigo
from qiskit_ibm_runtime.fake_provider import FakeTorontoV2
from qiskit_ibm_runtime.fake_provider import FakeTokyo
from qiskit_ibm_runtime.fake_provider import FakeCasablanca, FakeGuadalupeV2, FakeMelbourneV2, FakeKyiv, FakeOsaka

# Number of qubits for various backends
num_of_qubits = {'Vigo' : 5, 'TorontoV2' : 27, 'Tokyo' : 20, 'Casablanca' : 7, 'GuadalupeV2' : 16, 'MelbourneV2' : 17, 'FakeKyiv' : 127, 'FakeOsaka' : 127, 'Qasm' : 0}

# Generate list of backends to use
backends = {
    'Qasm' : Aer.get_backend('qasm_simulator'),
    'Vigo': FakeVigo(),
    'TorontoV2': FakeTorontoV2(),
    'Tokyo': FakeTokyo(),
    'Casablanca': FakeCasablanca(),
    'GuadalupeV2': FakeGuadalupeV2(),
    'MelbourneV2': FakeMelbourneV2(),
    'Kyiv' : FakeKyiv(),
    'Osaka' : FakeOsaka()
}

### CODE TO RUN ON BACKEND SIMUALTOR ###
#backend = Aer.get_backend('qasm_simulator')
backend = FakeKyiv()

### CODE TO RUN ON IBM QUANTUM SIMUALTOR ###
# token = '' #API token redacted
# QiskitRuntimeService.save_account(channel="ibm_quantum", token=token, overwrite=True)
# service = QiskitRuntimeService(channel="ibm_quantum")
# backend = service.least_busy(operational=True, simulator=False)
# backend.name

## Code drawn from IBM Qiskit Tutorials and slightly modified to fit new versions of Qiskit and improved functionality
## https://learning.quantum.ibm.com/tutorial/grovers-algorithm
## https://qiskit-community.github.io/qiskit-algorithms/tutorials/06_grover.html

def grover_oracle(marked_states): 
    num_qubits = len(marked_states[0]) # calculate number of qubits in system

    qc = QuantumCircuit(num_qubits)
    
    # Oracle marks each target state by flipping the sign of that specific state
    for target in marked_states:
        rev_target = target[::-1] # Reverse order initial state because Qiskit uses little endian
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)] # find 0 elements within encoded state
        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
        # where the target bit-string has a '0' entry
        qc.x(zero_inds)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        qc.x(zero_inds)
    return qc

def grovers(marked_states, backend):
    oracle = grover_oracle(marked_states)
    grover_op = GroverOperator(oracle) # initialize Grover diffusion operator
    
    # Calculates appropriate number of iterations needed of the reflection/diffusion operator to minimize angle between qubit state and target state
    optimal_num_iterations = math.floor(
        math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2**grover_op.num_qubits)))
    )

    print(optimal_num_iterations)
    
    qc = QuantumCircuit(grover_op.num_qubits)
    
    # Create even superposition of all basis states by applying a Hadamard gate
    qc.h(range(grover_op.num_qubits))
    # Apply Grover operator the optimal number of times
    qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
    # Measure all qubits
    qc.measure_all()
    
    # Updated from Qiskit tutorial to reflect new updates in Qiskit 1.00
    # Utilizes transpile instead of execute
    circ_ = transpile(qc, backend)
    job = backend.run(circ_)
    result = job.result()
    counts = result.get_counts()
    
    # Print out dictionary of counts
    print(counts) 
    # Print out time it took to execute job
    #print(job.usage_estimation)
    return counts

# Test grovers function
#grovers(['10101'], backend)

### CODE UTILIZED TO BENCHMARK FAKE BACKENDS ###

# Before running, must edit grovers() function to also take in appropriate backend 

# def test_grover_on_all_backends():
#     predefined_states = ["10", "01", "00"]  # Defining various marked states. Can adjust to appropriate number of qubits
#     results = {}

#     for backend_name, backend in backends.items():
        
#         # Store backend results
#         backend_results = []
        
#         # iterate through predefined states
#         for state in predefined_states:
#             # get counts dictionary
#             counts = grovers([state], backend)
#             # sum total number of shots
#             total_counts = sum(counts.values())
#             # get the number of counts for the predefined state from dictionary
#             correct_counts = counts.get(state, 0)
#             # calculate proportion and append
#             proportion = correct_counts / total_counts
#             backend_results.append(proportion)
            
#         average_proportion = sum(backend_results) / len(backend_results) # calculate proportion of correct results across all tested states
#         results[backend_name] = average_proportion
        
#         print(f"Backend: {backend_name}, Average Proportion: {str(average_proportion)}")

#     return results

# results = test_grover_on_all_backends()
# print(results)

### TIMING CLASSICAL AND QUANTUM BENCHMARKING ###

# define states we want to search for
states = ['10', '100', '1000', '10000', '100000', '1000000', '10000000', '100000000', '1000000000']
times_classical = []
times_grover = []

# classical search in O(N) time by just iterating through
def classical(n):
  for i in range(2**n):
    if (i == 2**n - 1):
      print(i)
      

for i in range(2, 11):
    times_grover.append(timeit.timeit(f"grovers([states[i - 2]], backend)", globals = globals(), number = 1))
    times_classical.append(timeit.timeit(f"classical(i)", globals = globals(), number = 1))

print(times_classical)
print(times_grover)
