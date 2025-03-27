# Quantum Search Project (Classical vs. Quantum Grover's Algorithm)

This project demonstrates the difference between **classical brute-force search** and **quantum search using Grover's Algorithm** in Qiskit. It is fully Dockerized and can be easily set up in any workspace.

## Project Setup Instructions

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/javabrown/quantum-search.git
cd quantum-search
```

### 2️⃣ **Build and Run the Docker Environment**
This project is **Dockerized** for easy setup. It includes:
✔ A **pre-configured Jupyter Notebook server**  
✔ **Qiskit, Qiskit Aer, and dependencies installed**  
✔ **Auto-mounted source code** for live development

To **build and launch the Docker environment**, run:
```bash
bash run_docker.sh
```

### 3️⃣ **Access Jupyter Notebook**
Once the container is running, access the Jupyter Notebook by opening:
```bash
http://localhost:8888
```
**Find the Jupyter token** in the Docker logs after running `run_docker.sh`.

### 4️⃣ **Run the Quantum Search Program**
Inside the container, execute the program:
```bash
python src/search_comparison.py
```
This runs both:
1. **Classical Brute Force Search**
2. **Quantum Grover’s Algorithm Search** (Qiskit)

---

## **Project Structure**
```
📚 quantum-search/
 ├️ 📚 src/                  # Source code
 │   ├️ search_comparison.py  # Main Python script
 │   ├️ quantum_search.ipynb  # Jupyter Notebook version
 ├️ 📚 output/               # Stores search results
 ├️ Dockerfile               # Docker setup instructions
 ├️ run_docker.sh            # Shell script to automate Docker launch
 ├️ requirements.txt         # Python dependencies
 ├️ README.md                # Project documentation
```

---

## **Docker Setup Details**
The `Dockerfile` installs all necessary quantum computing libraries:
```dockerfile
# Use an official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc g++ make \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose Jupyter Notebook port
EXPOSE 8888

# Run Jupyter Notebook by default
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
```

---

## ⚙️ **Shell Script: `run_docker.sh`**
This script automates the setup:
```bash
#!/bin/bash

# Define container and image name
CONTAINER_NAME="quantum_env"
IMAGE_NAME="quantum-env"

echo " Stopping and removing any existing container..."
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

echo " Removing old Docker image..."
docker rmi $IMAGE_NAME 2>/dev/null

echo " Building a fresh Docker image..."
docker build -t $IMAGE_NAME .

echo " Running the new Docker container..."
docker run -it --rm \
    -p 8888:8888 \
    -v $(pwd)/src:/workspace/src \
    -v $(pwd)/output:/workspace/output \
    --name $CONTAINER_NAME \
    $IMAGE_NAME
```
✔ **Rebuilds the image automatically**  
✔ **Mounts the `src/` directory** for live code changes  
✔ **Auto-removes old containers to avoid conflicts**

---

## 🏋️ **Installing Additional Packages**
If you need to install additional Python packages, do it **inside the running Docker container**:
```bash
docker exec -it quantum_env /bin/bash
pip install <package_name>
```
For example:
```bash
pip install matplotlib
```
 **For permanent installs**, add the package to `requirements.txt` and rebuild.

---

##  **Next Steps**
✔ **Extend Quantum Search** with real-world problems  
✔ **Deploy on Quantum Hardware** via **IBM Quantum Cloud**  
✔ **Optimize Quantum Circuits** for faster execution

 **Contribute & Extend:**  
Pull requests welcome! Feel free to extend and improve the quantum search algorithms.

---

##  **Resources**
- **Qiskit Documentation:** [qiskit.org/documentation](https://qiskit.org/documentation/)
- **Grover's Algorithm Overview:** [IBM Quantum Docs](https://quantum-computing.ibm.com/)
- **Docker Documentation:** [docker.com](https://docs.docker.com/)

---

