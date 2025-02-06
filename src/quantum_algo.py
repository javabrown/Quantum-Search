from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create a simple quantum circuit
qc = QuantumCircuit(2, 2)
qc.h(0)  # Apply Hadamard gate on qubit 0
qc.cx(0, 1)  # Apply CNOT gate to entangle qubit 0 and 1
qc.measure([0, 1], [0, 1])  # Measure the qubits

# Initialize the Aer simulator
simulator = AerSimulator()

# Transpile the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Execute the circuit on the simulator
result = simulator.run(compiled_circuit, shots=1024).result()

# Get the result counts
counts = result.get_counts()
print("Quantum Circuit Results:", counts)

# Save output to file
with open("/workspace/output/results.txt", "w") as f:
    f.write(str(counts))
