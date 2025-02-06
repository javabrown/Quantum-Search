import random
import time
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_algorithms import Grover, AmplificationProblem
from qiskit.circuit.library import PhaseOracle

# ================= CLASSICAL SEARCH =================
class ClassicalSearch:
    def __init__(self, dataset_size=10**6):
        self.dataset_size = dataset_size
        self.dataset = ["ITEM_" + str(i) for i in range(self.dataset_size)]
        self.target = "TARGET"

        # Place TARGET randomly in the dataset
        self.dataset[random.randint(0, self.dataset_size - 1)] = self.target

    def search(self):
        """Brute-force search for the TARGET."""
        start_time = time.time()
        for i, item in enumerate(self.dataset):
            if item == self.target:
                end_time = time.time()
                print(f"🎯 Classical Search Found '{self.target}' at index {i}")
                print(f"⏳ Classical Search Time: {end_time - start_time:.4f} seconds")
                return i
        return -1

# ================= QUANTUM SEARCH =================
class QuantumSearch:
    def __init__(self):
        """Initialize quantum search with Grover’s Algorithm."""
        # Define a valid Boolean logic expression
        self.oracle_expression = "(x0 & ~x1) | (x1 & x2 & ~x0)"

    def search(self):
        """Perform quantum search using Grover's Algorithm."""
        start_time = time.time()

        # Create the PhaseOracle using the Boolean expression
        oracle = PhaseOracle(self.oracle_expression)

        # Define the problem for Grover's Algorithm
        problem = AmplificationProblem(oracle)

        # Initialize Grover's Algorithm
        grover = Grover()

        # Construct the Grover circuit with the problem
        grover_circuit = grover.construct_circuit(problem)

        # Add measurement operations
        grover_circuit.measure_all()

        # Run on Quantum Simulator
        simulator = AerSimulator()
        compiled_circuit = transpile(grover_circuit, simulator)
        result = simulator.run(compiled_circuit, shots=1024).result()

        # Retrieve and display the results
        quantum_result = result.get_counts()
        end_time = time.time()

        print(f"🎯 Quantum Search Found: {quantum_result}")
        print(f"⚡ Quantum Search Time: {end_time - start_time:.4f} seconds")

# ================= RUN BOTH SEARCHES =================
if __name__ == "__main__":
    print("\n🔍 Running Classical Search...")
    classical_search = ClassicalSearch()
    classical_search.search()

    print("\n🚀 Running Quantum Search...")
    quantum_search = QuantumSearch()
    quantum_search.search()
