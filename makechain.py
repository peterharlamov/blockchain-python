from main import Blockchain

# Connect the class blockchain to the blockchain object
blockchain = Blockchain()

# Create blockchain transaction
blockchain.new_transaction("Alice", "Bob", 10)

# Mine a new block
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)

blockchain.new_transaction(sender="0", recipient="Alice", amount=1)
previous_hash = blockchain.hash(last_block)
block = blockchain.new_block(proof, previous_hash)

print(blockchain.chain)