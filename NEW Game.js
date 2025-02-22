
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input {
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .message {
            margin-top: 20px;
            font-size: 18px;
            color: green;
        }
    </style>
</head>
<body>
    <h1>Number Guessing Game</h1>
    <p>I have chosen a number between 1 and 100. Can you guess what it is?</p>
    <input type="number" id="guessInput" placeholder="Enter your guess">
    <button onclick="checkGuess()">Submit Guess</button>
    <p class="message" id="message"></p>

    <script>
        // Generate a random number between 1 and 100
        const secretNumber = Math.floor(Math.random() * 100) + 1;
        let attempts = 0;

        function checkGuess() {
            // Get the user's guess
            const guessInput = document.getElementById('guessInput');
            const message = document.getElementById('message');
            const guess = parseInt(guessInput.value);

            // Validate the input
            if (isNaN(guess) {
                message.textContent = "Please enter a valid number!";
                return;
            }

            attempts++;

            // Check if the guess is correct
            if (guess === secretNumber) {
                message.textContent = `Congratulations! You guessed the number in ${attempts} attempts.`;
                message.style.color = "green";
                guessInput.disabled = true;
            } else if (guess < secretNumber) {
                message.textContent = "Too low! Try again.";
                message.style.color = "red";
            } else {
                message.textContent = "Too high! Try again.";
                message.style.color = "red";
            }

            // Clear the input field
            guessInput.value = '';
        }
    </script>
</body>
</html>