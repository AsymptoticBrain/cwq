import numpy as np
import matplotlib.pyplot as plt

from qiskit import (
    QuantumCircuit,
    execute,
    Aer)
from qiskit.visualization import plot_histogram

"""
    Example circuit from IBM's qiskit setup page, modified to work in an IDE.
    The draw functions build in qiskit only seem to work in a jupyter notebook.
"""

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H, Hadamard gate on qubit 0 which puts that cubit in a superposition state
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, this entangles qubit 0 and qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0, 1], [0, 1])

# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit
circuit.draw(output='mpl')
plt.show()

plot_histogram(counts)
plt.show()
