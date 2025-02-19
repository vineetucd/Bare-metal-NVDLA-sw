# Bare-metal-NVDLA-sw

Bare-metal software generation to configure NVDLA for an arbitrary neural network  

## Usage

### Generate Configuration File and RISC-V Assembly Code
Run the following command to generate the configuration file (`output.txn`) and RISC-V assembly code (`riscv_updated.s`) to configure NVDLA:

```bash
python3 assembly_code_generation/assembly.py
```

### Extract Weights
Run the following command to extract weights (`weights.dat`):

```bash
python3 weights_extraction/weights.py
```

### Convert Image into RISC-V Code
Run the following command to convert an image into RISC-V code to store the image in data memory:

```bash
python3 image_to_riscv_code/im2riscv.py
```
