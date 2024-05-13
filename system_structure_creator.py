import os

# Define the project directory and create it if it doesn't exist
project_dir = "LakeshorePy"
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Create the virtual environment
os.system(f"python -m venv {project_dir}/venv")

# Activate the virtual environment
if os.name == "nt":
    activate_path = f"{project_dir}/venv/Scripts/activate.bat"
else:
    activate_path = f"{project_dir}/venv/bin/activate"
os.system(f"source {activate_path}")

# Install the necessary libraries
os.system(f"pip install pyvisa pytest numpy pandas simpy")

# Define the Lakeshore models to create files for
models = ["218", "224", "336"]

# Loop through the models and create a Python file for each one
for model in models:
    file_name = f"{project_dir}/lakeshore_{model}.py"
    with open(file_name, "w") as f:
        f.write(f"class Lakeshore{model}:")
