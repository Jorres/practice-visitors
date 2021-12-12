## How to run

Application has zero python dependencies and should run both on 
Python 2* and 3*. Just run:

```
python main.py
```

The application will read from a file called `input.txt` which should
be in the same directory as `main.py` file.

For examples of expressions see `examples.txt`.

## Demonstrating `State` pattern

The finite state automata that tokenizes input resides in `tokenizer.py`

## Demonstrating `Visitor` pattern

Three different visitors reside in `visitors` folder.

Note how in the `main.py` I just run over `tokens` array and all I do 
is call `accept` on a token with different visitors. 

