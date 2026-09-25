# Deat

A neural network written completely by myself, without a ready-made ML library (only numpy for the math). There are neurons, layers and a network that is trained with backpropagation. To test it, I tried to teach it to sort and to add numbers.

## Why I built it

I wanted to understand how neural networks really work, instead of only using existing libraries.

## What I learned

- What weights, biases and the sigmoid function do
- How backpropagation and gradient descent work

## Run

Needs numpy (`pip install numpy`).

```sh
python sortNumbersAI.py
python emTestAI.py
```

## Note

`emTestAI.py` is supposed to learn 5 + 5, but it doesn't really work. Because of the sigmoid function, the output of the network is always between 0 and 1, so it can never reach 10 and the loss stays high. The network is just not built for this. `sortNumbersAI.py` (sorting values between 0 and 1) fits the sigmoid output much better and works well.

