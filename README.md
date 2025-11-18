# Final Project: IBM AI Enterprise Workflow Specialization

## Author
This project was created by Esteban M. Cruz Seoane.

## What is this project?
This is a simple API that makes predictions using a model. It also logs predictions and includes tests to verify everything works.

## Important Files
- **app.py**: The API implementation.
- **model.py**: The model that makes predictions.
- **logger.py**: Handles logging.
- **data_ingestion.py**: Manages data.
- **run_tests.py**: Tests to verify functionality.
- **requirements.txt**: List of dependencies to install.
- **Dockerfile**: For using Docker (optional).

## Folders
- **sample_data/**: Example data.
- **models/**: Saved models.
- **logs/**: Log files.
- **tests/**: Tests.

## What do you need to get started?
1. **Python**: Make sure you have Python 3.8 or newer.
2. **pip**: To install the required dependencies.
3. **Docker** (optional): If you want to use containers.

## Steps to use it
1. **Download the project**:
   ```bash
   git clone https://github.com/pinkbunnies/curso-ibm.git
   ```
2. **Navigate to the folder**:
   ```bash
   cd curso-ibm/capstone-solution
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the API**:
   ```bash
   python app.py
   ```
5. **Test the API**:
   Open your browser or use Postman to go to:
   ```
   http://127.0.0.1:5000
   ```

## How to test it?
Run the tests:
```bash
python run_tests.py
```

## What if I want to use Docker?
1. **Build the image**:
   ```bash
   docker build -t capstone-solution .
   ```
2. **Run the container**:
   ```bash
   docker run -p 5000:5000 capstone-solution
   ```