#!/usr/bin/env python3

"""
Toy Quantum 512-Qubit Hash-Like Circuit using latest Qiskit imports
-------------------------------------------------------------------
DISCLAIMER:
1. This is a conceptual demo, NOT a real SHA-512 implementation.
2. Not cryptographically secure.
3. Extremely resource-intensive for large numbers of qubits (512).
   Reduce qubits for an actual local run (e.g., 8, 16, 32).
"""

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator



def quantum_512_hash(input_bits):
    """
    input_bits: A string of 512 classical bits, e.g. '0101...'.
    
    Returns a 512-bit output string as the 'hashed' result
    from measuring the quantum state after a toy mixing circuit.
    
    NOTE: This will be infeasible to run on most machines because simulating
    512 qubits is extremely memory-intensive (2^512 state space).
    In practice, test with fewer qubits for demonstration.
    """

    # 1. Validate input length
    if len(input_bits) != 512:
        raise ValueError("Input must be exactly 512 bits long.")

    # 2. Create a quantum circuit with 512 qubits + 512 classical bits
    qc = QuantumCircuit(512, 512, name="quantum_512_hash_demo")
    
    # 3. Initialize qubits based on the input bits
    #    For each '1' bit in the input, apply an X gate to set qubit to |1>
    for i, bit in enumerate(input_bits):
        if bit == '1':
            qc.x(i)
    
    # 4. Toy "hash-like" mixing routine
    # 4a. Apply Hadamard to all qubits
    qc.h(range(512))
    
    # 4b. Add simplistic CNOTs across pairs of qubits
    for i in range(0, 512, 2):
        if i + 1 < 512:
            qc.cx(i, i+1)
    
    # 4c. Arbitrary phase rotations (just to scramble)
    for i in range(512):
        angle = (i + 1) * 0.01  # arbitrary angle
        qc.rz(angle, i)
    
    # 4d. Another layer of Hadamards
    qc.h(range(512))
    
    # 5. Measure all qubits
    for i in range(512):
        qc.measure(i, i)
    
    # 6. Use AerSimulator to run the circuit
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)  # single shot => single 512-bit result
    result = job.result()
    
    # 7. Extract the measurement result
    counts = result.get_counts(compiled_circuit)
    # 'counts' might look like {'1010...': 1} for 1 shot
    measured_str = list(counts.keys())[0]  # e.g., '101010...'
    
    # Qiskit typically places the 0th qubit at the right end of the bitstring.
    # Reverse the string so that qubit 0 is on the left:
    hashed_bits = measured_str[::-1]
    
    return hashed_bits

if __name__ == "__main__":
    # Print out Qiskit versions for confirmation
    #check_qiskit_versions()

    # -------------------------------------------------------------------------
    # Because 512 qubits is huge, we demonstrate with a smaller example
    # (like 8 qubits) so you can actually run it locally:
    # -------------------------------------------------------------------------
    num_demo_qubits = 8
    demo_input = "01" * (num_demo_qubits // 2)  # e.g. '01010101' for 8 bits
    
    print(f"[TEST] Running a small demonstration with {num_demo_qubits} qubits...")
    
    # Build a smaller circuit
    qc_demo = QuantumCircuit(num_demo_qubits, num_demo_qubits, name="demo_hash")
    
    # Initialize qubits
    for i, bit in enumerate(demo_input):
        if bit == '1':
            qc_demo.x(i)
    
    # Some trivial "mixing"
    qc_demo.h(range(num_demo_qubits))
    for i in range(0, num_demo_qubits, 2):
        if i+1 < num_demo_qubits:
            qc_demo.cx(i, i+1)
    qc_demo.h(range(num_demo_qubits))
    
    # Measure
    for i in range(num_demo_qubits):
        qc_demo.measure(i, i)
    
    # Transpile & simulate
    sim = AerSimulator()
    cqc = transpile(qc_demo, sim)
    job = sim.run(cqc, shots=1)
    res = job.result()
    counts = res.get_counts()
    measured_demo_str = list(counts.keys())[0]
    hashed_demo_bits = measured_demo_str[::-1]
    
    print(f"Demo Input  ({num_demo_qubits} bits): {demo_input}")
    print(f"Demo Output ({num_demo_qubits} bits): {hashed_demo_bits}")
    
    # -------------------------------------------------------------------------
    # If you really want to try 512 qubits (not recommended for normal machines),
    # you'd do something like below (commented out to avoid memory crashes):
    #
    # real_512_input = "01" * 256  # 512 bits
    # hash_output = quantum_512_hash(real_512_input)
    # print(f"[INFO] 512-bit hash output: {hash_output}")
    # -------------------------------------------------------------------------
