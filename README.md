# Restaurant Dietary Information Extractor

Discover restaurants that align with your dietary needs! This project leverages the power of Google Places API and OpenAI API to help users find dining options that cater to specific dietary preferences, including vegan, vegetarian, and gluten-free. By gathering and analyzing restaurant reviews, the system extracts and structures dietary information, ensuring you can make informed choices about where to eat. The project also integrates MongoDB for data storage and Redis for caching, enhancing performance and data management.


## Setup Instructions
Follow these steps to set up and run the project:

### 1. Create and Activate a Virtual Environment
Create a virtual environment to manage your project's dependencies.
```bash```

python -m venv venv
source venv/bin/activate 

### 2. Install Required Libraries
Next, install the necessary Python libraries using the requirements.txt file.

Install the required libraries using pip.
pip install -r requirements.txt

### 3. Set up MongoDB 
Ensure MongoDB is installed and running on your machine. You can install MongoDB using Homebrew.

brew tap mongodb/brew
brew install mongodb-community@6.0
brew services start mongodb/brew/mongodb-community
```bash```
brew services stop mongodb/brew/mongodb-community

### 4. Set up Redis

brew install redis
brew services start redis
```bash```
brew services stop redis


## Run the Project

Finally, execute the main script to start the project.
python src/main.py

