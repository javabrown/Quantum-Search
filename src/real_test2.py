
import qiskit
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler
import os

token = os.environ.get("IBM_QUANTUM_TOKEN")
print(token);

# 1. Initialize the Qiskit Runtime Service
service = QiskitRuntimeService(token=token, channel="ibm_quantum", instance="ibm-q/open/main")

backend = service.least_busy(simulator=False, operational=True)
print(f'Running on {backend.name}')

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure(0, 0)
qc.measure(1, 1)
print(qc)
qc_measured = qc.measure_all(inplace=False)

from qiskit.primitives import StatevectorSampler
sampler = StatevectorSampler()
job = sampler.run([qc_measured], shots=1000)
result = job.result()

print(f" > Counts: {result[0].data['meas'].get_counts()}")