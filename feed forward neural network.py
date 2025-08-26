import numpy as np

# Activation function: Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Feedforward neural network class
class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases with random values
        self.W1 = np.random.randn(hidden_size, input_size)   # weights for input to hidden
        self.b1 = np.random.randn(hidden_size, 1)            # biases for hidden layer
        self.W2 = np.random.randn(output_size, hidden_size)  # weights for hidden to output
        self.b2 = np.random.randn(output_size, 1)            # biases for output layer

    def forward(self, x):
        # Convert input to 2D column vector
        x = x.reshape(-1, 1)

        # Input to hidden
        self.z1 = np.dot(self.W1, x) + self.b1
        self.a1 = sigmoid(self.z1)

        # Hidden to output
        self.z2 = np.dot(self.W2, self.a1) + self.b2
        self.a2 = sigmoid(self.z2)

        return self.a2

# Example usage
if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)

    # Define network
    input_size = 3   # Number of input features
    hidden_size = 4  # Number of hidden neurons
    output_size = 2  # Number of outputs

    nn = FeedforwardNeuralNetwork(input_size, hidden_size, output_size)

    # Example input (3 features)
    x_input = np.array([0.5, 0.1, 0.9])

    # Perform forward propagation
    output = nn.forward(x_input)

    print("Output of the neural network:")
    print(output)
