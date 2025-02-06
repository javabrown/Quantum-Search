from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a quantum circuit with 1 qubit & 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put qubit in superposition (like flipping a coin)
qc.h(0)

# Measure the qubit (collapse to 0 or 1)
qc.measure(0, 0)

# Run the circuit on a quantum simulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=100).result()

# Get results
counts = result.get_counts()
print("Quantum Coin Flip Results:", counts)
