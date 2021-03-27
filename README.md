# LT2222 V21 Assignment 3

Your name: Bérénice Le Glouanec

## Part 1

### You will explain what the functions a, b, and g do, as well as the meaning of the command-line arguments that are being processed via the argparse module. You will then run train.py on the training file.  train.py will save a model.

#### `a(f)`

The function `a(f)` takes a file as an argument and read it.
Then, an empty list is filled by each character in the file (which can either be a letter, a number, a punctuation, a space or a new line). It adds two start symbols `<s>` at the beginning and two end symbols `<e>` at the end of the list.
It returns this list `mm`, and the set of the elements of this list `list(set(mm))` (i.e. unique elements, a vocabulary).

#### `g(x, p)`

The function `g(x, p)` takes two arguments: `x` which is a single character and `p` which is a list of the vocabulary set.
It returns a matrix `z` filled with zeros of length `p`, and one `1` at the index of the element `x` in the list `p`.

#### `b(u, p)`

The function `b(u, p)` takes two arguments: `u` which is a list of single characters (`mm` in the function `a(f)`) and `p` which is a list of the vocabulary set (`list(set(mm))` in the function `a(f)`).
It goes through each item of `u` (excluding starts and ends symbols) and operates only on `vowels` (which is a list of vowels defined outside this function).
The empty list `gt` is filled with the index of each current vowel (in `u`) in the list `vowels`.
The empty list `gr` is filled with a concatenated matrix (which calls the function `g(x, p)` for the two characters `x` before and after the current character).
It returns a matrix `np.array(gr)` and a matrix `np.array(gt)`.

#### Command-line arguments

- parser.add_argument("--k", dest="k", type=int, default=200)
The optional argument `k` defines the hiddensize (default = 200).
- parser.add_argument("--r", dest="r", type=int, default=100)
The optional argument `r` defines the number of epochs (default = 100).
- parser.add_argument("m", type=str)
The argument `m` defines the file used to train the model.
- parser.add_argument("h", type=str)
The argument `h` defines the file used to save the model, it's a PATH.

    
## Part 2

### Write eval.py and add it to the repository.  What eval.py will do from the command line:

Load a model produced by train.py. (Take a look at model.py.)
Load the test data.
Create evaluation instances compatible with the training instances.  (A simplifying assumption for the purposes of the assignment: assuming that the neighbouring vowels are known as though the Fairy hadn't stolen them.)
Use the model to predict instances.
Write the text with the predicted (as opposed to the real) vowels back into an output file.
Print the accuracy of the model to the terminal.

## Part 3

### Describe what you do in README.md.  Train and evaluate the following models:

* Five different variations of the --k option, holding the --r option at its default.
* Five different variations of the --r option, holding the --k option at its default.
Include the best model and output text in your repository with its parameters.  Describe any patterns you see, if there are any.  Look at the output texts and make qualitative comments on the performances of the model.



## Bonuses

## Other notes
