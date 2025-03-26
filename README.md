# Simple Blockchain Simulation

This project demonstrates a basic blockchain simulation built in JavaScript. The simulation includes:

- **Block Structure:** Each block includes an index, timestamp, a list of transactions, previous block hash, current block hash, and a nonce.
- **Hashing:** SHA-256 is used to generate the block's hash.
- **Blockchain Class:** Includes methods to add new blocks and validate the chain's integrity.
- **Proof-of-Work:** A simple mining function requiring a hash with a certain number of leading zeros.
- **Tampering Detection:** The simulation shows how tampering with block data invalidates the chain.

## Repository Contents

- **backend/**: Contains the blockchain simulation code and its Dockerfile.
- **frontend/**: A simple static frontend (served via Nginx) to display information or act as a placeholder.
- **docker-compose.yml**: Sets up three services:
  - **backend**: Runs the Node.js blockchain simulation.
  - **frontend**: Serves a static webpage.
  - **db**: A MongoDB container (for demonstration purposes).

## Setup and Execution Instructions

### Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Running the Application

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/blockchain-simulation.git
   cd blockchain-simulation
