import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

print("✅ Qiskit version:", qiskit.__version__)

# Check available modules
print("✅ Qiskit modules:", dir(qiskit))

# Check if compiler module and execute function exist
if hasattr(qiskit.compiler, "transpile"):
    print("✅ Qiskit.compiler.transpile is available")
else:
    print("❌ Qiskit.compiler.transpile is missing")

# Check if Qiskit Aer is working
try:
    simulator = AerSimulator()
    print("✅ Qiskit AerSimulator is available")
except Exception as e:
    print("❌ Error initializing Qiskit Aer:", str(e))

# Run a basic quantum circuit to validate execution
try:
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    print("✅ Quantum Circuit Execution Successful:", counts)
except Exception as e:
    print("❌ Error running Quantum Circuit:", str(e))
