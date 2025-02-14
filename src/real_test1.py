#!/usr/bin/env python3
"""
Short example using qiskit-ibm-runtime (the current recommended IBM Quantum interface).
"""

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
import os 
from qiskit.primitives import Sampler

def main():
  
    token = os.environ.get("IBM_QUANTUM_TOKEN")
    print(token);
    
    service = QiskitRuntimeService(
        token=token,
        channel="ibm_quantum",
        instance="ibm-q/open/main"
    )

    print ("App connected to IBM Quantum Infrastructure.\n Looking for available backend:\n---\n");


    all_backends = service.backends()

    for backend in all_backends:
        config = backend.configuration()
        status = backend.status()
        print(f"Name: {backend.name}")
        print(f"  Qubit count:     {config.n_qubits}")
        print(f"  Pending jobs:    {status.pending_jobs}")
        print(f"  Operational?:    {status.operational}")
        print("---")

    backends_eligible = [b for b in all_backends if b.configuration().n_qubits >= 127]
    # Sort by queue length (pending_jobs)
    sorted_backends = sorted(backends_eligible, key=lambda b: b.status().pending_jobs)

    # Pick the one with the fewest pending jobs
    best_backend = sorted_backends[0]
    print(f"Selected backend: {best_backend.name} with pending jobs = {best_backend.status().pending_jobs}")


if __name__ == "__main__":
    main()
