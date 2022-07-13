# Orochi-recipe

Orochi is a library which can load HIP and CUDA APIs dynamically.
With its support, one does not need to compile two separate implementations for each API and could maintain a single binary to run on both AMD and NVIDIA GPUs. 

## Installation

- Go to the folder where the `conanfile.py` is located
- `conan create .`
- This will clone the source from the repository of Orochi, build it as a static lib and run a test to ensure the package is installed correctly.


## Using the Orochi library

- Once installed, add `orochi/latest` in the `[requires]` section in the `conanfile.txt` in your project


## Note

- One can use `pip install conan` to install conan.
