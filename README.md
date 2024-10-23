# Morphology Synthesis



Morphology Synthesis is a REST API for generating and analyzing morphological structures. It provides a variety of endpoints for handling morphology data and performing synthesis operations.

## Features

- Create, update, and retrieve morphology structures
- Perform morphological analysis
- Export synthesized morphology data in various formats

## Install

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/morphology-synthesis.git
    cd morphology-synthesis
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```


The server will be available at `http://127.0.0.1:8000`.


## Examples

Visit `http://localhost:8000/docs` after running the server to find documentation of the endpoints

## Acknowledgements

The development of this software was supported by funding to the Blue Brain Project, a research center of the École polytechnique fédérale de Lausanne (EPFL), from the Swiss government’s ETH Board of the Swiss Federal Institutes of Technology.

For license and authors, see LICENSE.txt and AUTHORS.txt respectively.

Copyright &copy; 2023-2024 Blue Brain Project/EPFL