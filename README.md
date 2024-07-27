# Crypto Currency Blockchain Project

## Overview

This project implements a basic cryptocurrency blockchain. It includes functionalities for creating and managing transactions, blocks, and wallets. It also incorporates digital signatures for transaction verification and a mining mechanism for block validation.

## Project Structure

-   **signature.py**: Handles the generation and verification of digital signatures.
-   **Miner.py**: Contains the logic for mining new blocks.
-   **Blockchain.py**: Manages the blockchain, including adding new blocks and maintaining the chain.
-   **Wallet.py**: Manages wallet operations including balance checking and transaction creation.
-   **Transaction.py**: Defines the structure and functionality of transactions.
-   **TxBlock.py**: Defines transaction blocks used in the blockchain.

## File Descriptions

### signature.py

Includes functions for generating keys, signing messages, and verifying signatures.

-   **generate_keys()**: Generates a new pair of public and private keys.
-   **sign(message, private_key)**: Signs a message using the provided private key.
-   **verify(message, signature, pu_serialized)**: Verifies a signature using the provided public key.

### Miner.py

Contains the logic for mining new blocks, including proof of work and block validation.

### Blockchain.py

Manages the blockchain by maintaining the chain of blocks, validating new blocks, and ensuring the integrity of the chain.

### Wallet.py

Handles wallet operations such as creating new wallets, checking balances, and creating transactions.

### Transaction.py

Defines the structure and functionality of transactions, including creating and validating transactions.

### TxBlock.py

Defines transaction blocks, which are used to store transactions in the blockchain. Handles adding transactions to blocks and managing block data.

## Getting Started

### Prerequisites

-   Python 3.x

### Running the Project

1. **Generate Keys**:
    ```python
    from signature import generate_keys
    public_key, private_key = generate_keys()
    ```
2. **Create a Transaction**:
    ```python
    from Transaction import Transaction
    tx = Transaction(sender, recipient, amount)
    ```
3. **Sign a Transaction**:
    ```python
    from signature import ssign
    signed_tx = ssign(tx, private_key)
    ```
4. **Verify a Transaction**:
    ```python
    from signature import verify
    is_valid = verify(tx, signed_tx, public_key)
    ```
5. **Mine a Block**:
    ```python
    from Miner import mine_block
    block = mine_block(transactions)
    ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out for any questions or contributions. Enjoy building your blockchain project!
