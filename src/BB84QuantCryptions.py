import os
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

# === STEP 1: Connect to IBM Quantum ===
token = os.environ.get("IBM_QUANTUM_TOKEN")  # Ensure your token is set

# Initialize the Qiskit Runtime Service
service = QiskitRuntimeService(channel="ibm_quantum", token=token)

# Select the least busy backend
backends = service.backends(simulator=False, operational=True)
backend = sorted(backends, key=lambda b: b.status().pending_jobs)[0]  # Pick backend with least jobs
print(f"Running on backend: {backend.name}")

# === STEP 2: Generate Quantum Key Using BB84 Protocol ===
def generate_quantum_key(n_bits):
    """Generates a secure quantum key using the BB84 protocol."""
    alice_bits = np.random.randint(0, 2, size=n_bits)  # Alice's random bits
    alice_bases = np.random.randint(0, 2, size=n_bits)  # Alice's random bases

    # Create the quantum circuit
    qc = QuantumCircuit(n_bits, n_bits)
    for i in range(n_bits):
        if alice_bits[i] == 1:
            qc.x(i)  # Encode bit
        if alice_bases[i] == 1:
            qc.h(i)  # Apply Hadamard for X-basis encoding

    # Bob chooses random bases
    bob_bases = np.random.randint(0, 2, size=n_bits)
    for i in range(n_bits):
        if bob_bases[i] == 1:
            qc.h(i)  # Match Alice's basis
        qc.measure(i, i)  # Measure qubit

    # Transpile for the selected IBM backend
    transpiled_qc = transpile(qc, backend)

    # Execute the circuit on the IBM Quantum backend
    with Session(service=service, backend=backend) as session:
        sampler = Sampler(session=session)
        job = sampler.run(circuits=transpiled_qc, shots=1)
        result = job.result()
        bob_results = list(result.quasi_dists[0].keys())[0]

    # Alice & Bob compare bases and extract matching bits
    matching_bases = alice_bases == bob_bases
    alice_key = alice_bits[matching_bases]
    bob_key = np.array([int(bit) for bit in bob_results])[matching_bases]

    if not np.array_equal(alice_key, bob_key):
        raise ValueError("Quantum key mismatch detected. Potential eavesdropping!")

    return alice_key

# === STEP 3: Encrypt & Decrypt Messages ===
def encrypt_message(message, key):
    """Encrypts a string message using XOR with a quantum-generated key."""
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    key = np.resize(key, len(binary_message))
    encrypted_bits = np.array([int(b) for b in binary_message]) ^ key
    return ''.join(map(str, encrypted_bits))

def decrypt_message(encrypted_bits, key):
    """Decrypts a message using XOR with the quantum key."""
    key = np.resize(key, len(encrypted_bits))
    decrypted_bits = np.array([int(b) for b in encrypted_bits]) ^ key
    return ''.join(chr(int(''.join(map(str, decrypted_bits[i:i+8])), 2)) for i in range(0, len(decrypted_bits), 8))

# === MAIN EXECUTION ===
if __name__ == "__main__":
    message = "Quantum Security!"  # Message to encrypt
    print(f"🔹 Original Message: {message}")

    # Generate a quantum key
    key_length = len(message) * 8  # Each character requires 8 bits
    quantum_key = generate_quantum_key(key_length)
    print(f"🔑 Quantum Key: {quantum_key}")

    # Encrypt the message
    encrypted_msg = encrypt_message(message, quantum_key)
    print(f"🔒 Encrypted Message (Binary): {encrypted_msg}")

    # Decrypt the message
    decrypted_msg = decrypt_message(encrypted_msg, quantum_key)
    print(f"🔓 Decrypted Message: {decrypted_msg}")

    # Verify decryption correctness
    assert message == decrypted_msg, "Decryption failed! The decrypted message does not match the original."
