from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator

qc = QuantumCircuit(1)

qc.h(0)

qc.measure_all()

simulator = AerSimulator()

compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()


counts = result.get_counts()
print(counts)
