# Simple Arithmetic App

This project is a simple arithmetic practice application built using Streamlit. It allows users to practice addition and subtraction through a series of questions and provides feedback on their performance.

## Project Structure

```
simple-arithmetic-app
├── src
│   ├── app.py        # Entry point of the application
│   ├── game.py       # Contains game logic for generating questions and checking answers
│   └── utils.py      # Utility functions for the application
├── tests
│   └── test_game.py  # Unit tests for the game logic
├── requirements.txt   # Lists the dependencies required for the project
├── README.md          # Documentation for the project
└── .gitignore         # Specifies files to be ignored by Git
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-arithmetic-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the App

To run the application, execute the following command:
```
streamlit run src/app.py
```

## Usage

The app will present the user with three arithmetic questions (addition and subtraction). After answering, the app will display the number of correct answers.

## Testing

To run the unit tests, navigate to the `tests` directory and run:
```
pytest test_game.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.