#initialization
import matplotlib.pyplot as plt
import numpy as np

# importing qiskit
from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QunatumRegister, execute
from qiskit.providers.ibmq import least_busy
from qiskit.quantum_info import Statevector

# import basic plot tools
from qiskit.visualization import plot_histogram

clause_list = [
            [0,1],
            [0,2],
            [1,3],
            [2,3]
            ] #the rows/columns we need to check and make sure they have different values

def XOR(qc, a, b, output):
    qc.cx(a, output)
    qc.cx(b, output) #will be used for above clausees. output bit is only flipped if the two vals are not equal

def sudoku_oracle(qc, clause_list, var_qubits, clause_qubits, cbits):
    # does above operations for all the pairs. final state is 1 if it is a solution
    i = 0
    for clause in clause_list:
        XOR(qc, clause[0], clause[1], clause_qubits[i])
        i += 1
    
    # Flip 'output' bit if all clauses are satisfied
    qc.mct(clause_qubits, output_qubit)

    # Uncompute clauses to reset clause-checking bits to 0
    i = 0
    for clause in clause_list:
        XOR(qc, clause[0], clause[1, clause_qubits[i]])
        i += 1

