# Built-in modules
import math

# Imports from Qiskit
from qiskit_aer import Aer
from qiskit.providers.aer.noise import NoiseModel
from qiskit.providers.aer.noise.errors import depolarizing_error
from qiskit_aer.utils import transpile_noise_model
from qiskit import transpile, QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.visualization import plot_histogram

# To run on Aer simulator:
backend = Aer.get_backend('qasm_simulator')

def grover_oracle(marked_states):
    """Build a Grover oracle for multiple marked states

    Here we assume all input marked states have the same number of bits

    Parameters:
        marked_states (str or list): Marked states of oracle

    Returns:
        QuantumCircuit: Quantum circuit representing Grover oracle
    """
    if not isinstance(marked_states, list):
        marked_states = [marked_states]
    # Compute the number of qubits in circuit
    num_qubits = len(marked_states[0])

    qc = QuantumCircuit(num_qubits)
    # Mark each target state in the input list
    for target in marked_states:
        # Flip target bit-string to match Qiskit bit-ordering
        rev_target = target[::-1]
        # Find the indices of all the '0' elements in bit-string
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        # Add a multi-controlled Z-gate with pre- and post-applied X-gates (open-controls)
        # where the target bit-string has a '0' entry
        qc.x(zero_inds)
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        qc.x(zero_inds)
    return qc

marked_states = ["011", "100"]

oracle = grover_oracle(marked_states)

grover_op = GroverOperator(oracle)

optimal_num_iterations = math.floor(
    math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2**grover_op.num_qubits)))
)

qc = QuantumCircuit(grover_op.num_qubits)
# Create even superposition of all basis states
qc.h(range(grover_op.num_qubits))
# Apply Grover operator the optimal number of times
qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
# Measure all qubits
qc.measure_all()


# Defining noise models for gates above
def get_noise_model():
    # Error probs
    error_probs = {
        "reset": 0.03, 
        "x": 0.03,      
        "cx": 0.05      
    }

    # Create a depolarizing noise model
    noise_model = NoiseModel()
    for gate_name, prob in error_probs.items():
        noise_model.add_quantum_error(depolarizing_error(prob, 1))
    return noise_model

# Noise model
noise_model = get_noise_model()

circ_ = transpile(qc, backend)
circ_ = transpile_noise_model(circ_, noise_model) # Apply noise model
job = backend.run(circ_)
result = job.result()
counts = result.get_counts()

plot_histogram(counts)
print(counts)
