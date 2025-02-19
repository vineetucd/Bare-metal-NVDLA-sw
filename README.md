# Bare-metal-NVDLA-sw
Bare-metal software generation to configure NVDLA for an arbitrary neural network  

## Run the following command to generate the configuration file (`output.txn`) and RISC-V assembly code (`riscv_updated.s`) to configure NVDLA:
```bash
python3 assembly_code_generation/assembly.py

## Run the following command to extract weights (weights.dat):
```bash
python3 weights_extraction/weights.py
