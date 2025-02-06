from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2, 2)

# Put both qubits into superposition (considering all values of X & Y at once)
qc.h([0, 1])

# Apply XOR condition (CNOT gate simulates "X XOR Y")
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Run on Quantum Simulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()

# Get the results
counts = result.get_counts()
print("🔄 Parallel Processed Results:", counts)
