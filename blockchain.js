const crypto = require('crypto');

class Block {
  constructor(index, timestamp, transactions, prevHash = '0') {
    this.index = index;
    this.timestamp = timestamp;
    this.transactions = transactions;
    this.prevHash = prevHash;
    this.hash = this.calculateHash();
  }

  calculateHash() {
    const blockData = this.index + this.timestamp + JSON.stringify(this.transactions) + this.prevHash;
    return crypto.createHash('sha256').update(blockData).digest('hex');
  }
}

class Blockchain {
  constructor(difficulty = 2) {
    this.chain = [];
    this.difficulty = difficulty;
    this.createGenesisBlock();
  }

  createGenesisBlock() {
    const genesisBlock = new Block(0, Date.now(), ["Genesis Block"], "0");
    this.chain.push(genesisBlock);
  }

  proofOfWork(block) {
    while (!block.hash.startsWith('0'.repeat(this.difficulty))) {
      block.timestamp = Date.now();
      block.hash = block.calculateHash();
    }
  }

  addBlock(transactions) {
    const prevBlock = this.chain[this.chain.length - 1];
    const newBlock = new Block(this.chain.length, Date.now(), transactions, prevBlock.hash);
    this.proofOfWork(newBlock);
    this.chain.push(newBlock);
  }

  validateChain() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const prevBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        console.log(`Block ${currentBlock.index} has been tampered with!`);
        return false;
      }

      if (currentBlock.prevHash !== prevBlock.hash) {
        console.log(`Block ${currentBlock.index} is not properly linked to the previous block!`);
        return false;
      }
    }
    console.log("Blockchain is valid!");
    return true;
  }

  displayChain() {
    this.chain.forEach(block => {
      console.log(`Block #${block.index} - Hash: ${block.hash}`);
      console.log(`Timestamp: ${block.timestamp}`);
      console.log(`Transactions: ${JSON.stringify(block.transactions)}`);
      console.log(`Previous Hash: ${block.prevHash}`);
      console.log("=" .repeat(50));
    });
  }
}


const blockchain = new Blockchain();


blockchain.addBlock(["Alice sends 2 BTC to Bob", "Bob sends 1 BTC to Charlie"]);
blockchain.addBlock(["Charlie sends 0.5 BTC to Alice", "Alice sends 0.1 BTC to Bob"]);

blockchain.displayChain();

blockchain.validateChain();

console.log("\nSimulating Tampering...");
blockchain.chain[1].transactions = ["Malicious transaction"];

blockchain.validateChain();
