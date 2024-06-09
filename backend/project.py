import os

# Define directories and files
dirs = [
    "src",
    "tests"
]

files = [
    "src/__init__.py",
    "src/config.py",
    "src/google_places.py",
    "src/openai_integration.py",
    "src/data_processor.py",
    "src/main.py",
    "tests/__init__.py",
    "tests/test_google_places.py",
    "tests/test_openai_integration.py",
    "tests/test_data_processor.py",
    ".env",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass

print("Project structure created successfully.")
