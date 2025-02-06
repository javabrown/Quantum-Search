# Use the official Python 3.10 image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /workspace

# Install system dependencies required for Qiskit Aer
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libgfortran5 \
    libblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Qiskit and its components
RUN pip install --no-cache-dir \
    qiskit \
    qiskit-aer \
    qiskit-ibm-runtime

# Install additional Python libraries
RUN pip install --no-cache-dir jupyterlab numpy scipy matplotlib

# Copy the verification script into the container
COPY ./verify_qiskit_install.py /workspace/verify_qiskit_install.py

# Expose Jupyter Notebook port
EXPOSE 8888

# Default command: Start Jupyter Notebook
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
