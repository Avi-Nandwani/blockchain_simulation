import hashlib
import time

# Block Class
class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concatenate block data and calculate SHA-256 hash
        block_data = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.prev_hash)
        return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

# Blockchain Class
class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty  # Set difficulty for Proof of Work
        self.create_genesis_block()

    def create_genesis_block(self):
        # Genesis block (first block)
        genesis_block = Block(0, time.time(), ["Genesis Block"], "0")
        self.chain.append(genesis_block)

    def proof_of_work(self, block):
        # Proof of Work: find a hash that starts with 'difficulty' number of zeros
        while not block.hash.startswith('0' * self.difficulty):
            block.timestamp = time.time()  # Update timestamp for each attempt
            block.hash = block.calculate_hash()

    def add_block(self, transactions):
        # Add a new block with given transactions
        prev_block = self.chain[-1]  # Previous block
        new_block = Block(len(self.chain), time.time(), transactions, prev_block.hash)
        self.proof_of_work(new_block)  # Apply Proof of Work
        self.chain.append(new_block)

    def validate_chain(self):
        # Validate the blockchain's integrity
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            # Check if the block hash matches the calculated hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.prev_hash != prev_block.hash:
                print(f"Block {current_block.index} is not properly linked to the previous block!")
                return False

        print("Blockchain is valid!")
        return True

    def display_chain(self):
        # Print details of each block in the blockchain
        for block in self.chain:
            print(f"Block #{block.index} - Hash: {block.hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.prev_hash}")
            print("="*50)

# Main Simulation
if __name__ == "__main__":
    # Create a blockchain instance
    blockchain = Blockchain()

    # Add blocks with dummy transactions
    blockchain.add_block(["Alice sends 2 BTC to Bob", "Bob sends 1 BTC to Charlie"])
    blockchain.add_block(["Charlie sends 0.5 BTC to Alice", "Alice sends 0.1 BTC to Bob"])

    # Display the blockchain
    blockchain.display_chain()

    # Validate the blockchain's integrity
    blockchain.validate_chain()

    # Tampering example (modify data in the second block)
    print("\nSimulating Tampering...")
    blockchain.chain[1].transactions = ["Malicious transaction"]
    
    # Revalidate the blockchain
    blockchain.validate_chain()
