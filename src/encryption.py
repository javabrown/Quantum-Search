from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

# Number of qubits (bits in the quantum key)
key_length = 5

# Generate Alice's random bit sequence (0s and 1s)
alice_bits = [random.randint(0, 1) for _ in range(key_length)]

# Generate Alice's random bases (0 for standard, 1 for Hadamard)
alice_bases = [random.randint(0, 1) for _ in range(key_length)]

# Bob chooses random measurement bases
bob_bases = [random.randint(0, 1) for _ in range(key_length)]

# Quantum Circuit to simulate transmission
qc = QuantumCircuit(key_length, key_length)

# Alice prepares qubits
for i in range(key_length):
    if alice_bits[i] == 1:  # Encode the bit
        qc.x(i)
    if alice_bases[i] == 1:  # Use Hadamard basis if chosen
        qc.h(i)

# Simulate Bob measuring in random bases
for i in range(key_length):
    if bob_bases[i] == 1:
        qc.h(i)  # Apply Hadamard gate before measurement
    qc.measure(i, i)

# Run on simulator
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1).result()

# Get Bob's measurement results
bob_results = list(result.get_counts().keys())[0]

# Generate final shared key (Only where Alice & Bob used the same bases)
shared_key = [
    alice_bits[i] for i in range(key_length) if alice_bases[i] == bob_bases[i]
]

print(f"Alice's bits     : {alice_bits}")
print(f"Alice's bases    : {alice_bases}")
print(f"Bob's bases      : {bob_bases}")
print(f"Bob's results    : {bob_results}")
print(f"Final Shared Key : {shared_key}")
