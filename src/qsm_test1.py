import qiskit.qasm2
program = '''
    OPENQASM 2.0;
    include "qelib1.inc";
    qreg q[2];
    creg c[2];
 
    h q[0];
    cx q[0], q[1];
 
    measure q -> c;
'''
circuit = qiskit.qasm2.loads(program)
circuit.draw()