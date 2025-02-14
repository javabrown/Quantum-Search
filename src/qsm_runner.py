from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Load the QSM (QASM) file
qc = QuantumCircuit.from_qasm_file("simple1.qsm")

sim = AerSimulator()
qc_compiled = transpile(qc, sim)
job = sim.run(qc_compiled, shots=1024)
result = job.result()

print(result.get_counts(qc_compiled))
