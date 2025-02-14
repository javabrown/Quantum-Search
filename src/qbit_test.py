from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService

import os

token = os.environ.get("IBM_QUANTUM_TOKEN")

print(token)

service = QiskitRuntimeService(token=token, channel="ibm_quantum", instance="ibm-q/open/main")
backend = service.least_busy(simulator=False, operational=True)

qc = QuantumCircuit(1,1)

qc.h(0)
qc.measure(0,0)


print(qc.draw())