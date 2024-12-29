### GCP Cloud VM

---

### **Key Steps and Commands**

---

#### **1. Setting Up the Google Cloud Virtual Machine (VM)**

1. **Create a VM Instance**:
   - Navigate to **Compute Engine > VM Instances**.
   - Click **Create Instance**.
   - Configure the instance:
     - **Name**: Choose a descriptive name (e.g., `data-engineering-vm`).
     - **Region**: Select a nearby region for better performance.
     - **Machine type**: `e2-standard-4` (4 vCPUs, 16 GB RAM) is recommended.
     - **Boot disk**:
       - Change to **Ubuntu 20.04 LTS**.
       - Increase disk size to at least **30 GB** for sufficient storage.
   - Click **Create**.

2. **Generate SSH Keys**:
   - Open a terminal and navigate to the SSH directory:
     ```bash
     cd ~/.ssh
     ```
   - Generate SSH keys:
     ```bash
     ssh-keygen -t rsa -f <key-name> -C <username> -b 2048
     ```
   - Add the **public key** to GCP:
     - Navigate to **Metadata > SSH Keys**.
     - Paste the contents of `gcp_key.pub`.

3. **Access the VM**:
   - Use SSH to connect:
     ```bash
     ssh -i ~/.ssh/<key-name> username@<external-ip>
     ```

---
#### Another way to connect to the VM via VS Code SSH Extension

1. **Install the Remote - SSH Extension**:
   - Open **Visual Studio Code**.
   - Go to **Extensions** and search for **Remote - SSH**.
   - Click **Install**.

2. **Connect to the VM**:
   - Click on the **Remote Explorer** icon.
   - Click on the **SSH Targets** icon.
   - Click **+** and add a new SSH target.
   - Enter the SSH command:
     ```bash
     ssh -i ~/.ssh/<key-name> username@<external-ip>
     ```
   - Connect to the VM.

Or,

From the Remote Explorer, click on the Remote(Tunnel) icon and click on the `+` icon to add a new SSH target via config file. Add the following configuration to the `config` file:

```bash
Host GCP_VM
  HostName <external-ip>
  User username
  IdentityFile ~/.ssh/<key-name>
```

> Make sure to have the `.ssh` directory in the home directory of the user and `config` file in the `.ssh` directory.

Then, connect to the VM by selecting the `GCP_VM` from the Remote Explorer.

---

#### **2. Installing Tools on the VM**

**A. Install Anaconda (Python Environment)**:
1. Download Anaconda for Linux:
   ```bash
   wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
   ```
2. Install:
   ```bash
   bash Anaconda3-2024.10-1-Linux-x86_64.sh
   ```
3. Activate Anaconda:
   ```bash
   source ~/.bashrc
   ```

**B. Install Docker and Docker Compose**:
1. **Install Docker**:
   ```bash
   sudo apt update
   sudo apt install docker.io
   ```
   - Test Docker:
     ```bash
     docker --version
     ```

2. **Enable Docker without sudo**:
   ```bash
   sudo groupadd docker
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Install Docker Compose**:
   - Download Docker Compose binary:
     ```bash
     mkdir ~/bin
     wget -O ~/bin/docker-compose https://github.com/docker/compose/releases/download/v2.32.0/docker-compose-linux-x86_64
     chmod +x ~/bin/docker-compose
     ```
   - Add `~/bin` to PATH:
     ```bash
     echo 'export PATH=~/bin:$PATH' >> ~/.bashrc
     source ~/.bashrc
     ```
   - Test:
     ```bash
     docker-compose --version
     ```

**C. Install Terraform**:
1. Download Terraform binary:
   ```bash
   wget https://releases.hashicorp.com/terraform/1.5.0/terraform_1.5.0_linux_amd64.zip
   ```
2. Unzip and install:
   ```bash
   sudo apt install unzip
   unzip terraform_1.5.0_linux_amd64.zip
   sudo mv terraform /usr/local/bin/
   terraform --version
   ```

---

#### **3. Configuring the Environment**

**A. Forward Ports for Local Access**:
1. Use **Visual Studio Code** to forward ports for accessing services like Jupyter, PostgreSQL, or PGAdmin.
2. Install the **Remote - SSH** extension in VS Code.
3. Connect to the remote VM and forward ports:
   - Example: Forward PostgreSQL (`5432`) or Jupyter (`8888`) to your local machine.

**B. Clone the Course Repository**:
   ```bash
   git clone https://github.com/DataTalksClub/data-engineering-zoomcamp.git
   ```

**C. Test Docker Compose**:
   - Navigate to the course directory and start the containers:
     ```bash
     cd data-engineering-zoomcamp/week_1_basics_n_setup/docker_sql
     docker-compose up -d
     ```

Test it by installing the `pgcli` tool and connecting to the PostgreSQL container:

```bash
sudo apt install pgcli
pgcli -h localhost -U root -d ny_taxi
```

Or, using conda environment:

```bash
conda install -c conda-forge pgcli
pgcli -h localhost -U root -d ny_taxi
```

```
\dt; # List of relations
```


---

#### **4. Forwording Ports created from Docker Compose to Local Machine**

Open the `PORTS` from the terminal in VS Code and click on the `Forward Port` icon to forward the ports from the VM to the local machine.

The add the port `5432` for PostgreSQL and `8888` for Jupyter, port `8080` for PGAdmin.
---

#### **5. Best Practices for Managing the VM**

1. **Stop the VM**:
   - Use the GCP Console:
     - Navigate to **Compute Engine > VM Instances**.
     - Click **Stop** to save costs when the VM is idle.
   - Or use SSH:
     ```bash
     sudo shutdown now
     ```

2. **Delete the VM**:
   - Use the GCP Console:
     - Navigate to **Compute Engine > VM Instances**.
     - Click **Delete** to remove the VM and all associated data.

3. **Port Forwarding**:
   - Use VS Code to forward ports for seamless local access to services running on the VM.

---

### **Commands Cheat Sheet**

| **Command**                                    | **Purpose**                                                      |
|------------------------------------------------|------------------------------------------------------------------|
| `ssh-keygen -t rsa -b 4096 -f gcp_key`         | Generate SSH keys for secure access.                            |
| `ssh -i ~/.ssh/gcp_key username@<external-ip>` | SSH into the VM using the private key.                          |
| `sudo apt update && sudo apt install docker.io`| Install Docker.                                                 |
| `wget <url>`                                   | Download files from a URL (e.g., Anaconda, Terraform, Docker).  |
| `docker-compose up -d`                         | Start Docker Compose services in detached mode.                 |
| `sudo shutdown now`                            | Stop the VM from the command line.                              |

---

### **Key Takeaways**
1. **Efficient Resource Management**: Stop or delete the VM when not in use to minimize costs.
2. **Tool Installation**: Install essential tools (Anaconda, Docker, Terraform) for data engineering tasks.
3. **Secure Access**: Use SSH keys for secure and convenient access to the VM.
4. **Flexibility**: Use VS Code for seamless integration with the remote environment via port forwarding.
5. **Portable Setup**: Clone course resources and configure tools on the VM for a consistent learning environment.

This setup ensures a robust and cost-effective environment for completing the data engineering course.