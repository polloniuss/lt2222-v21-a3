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

- The optional argument `k` defines the hiddensize (default = 200).
- The optional argument `r` defines the number of epochs (default = 100).
- The argument `m` defines the file used to train the model.
- The argument `h` defines the file used to save the model, it's a PATH.

    
## Part 2

### Write eval.py and add it to the repository. 


## Part 3

### Describe what you do in README.md.  Train and evaluate the following models:

* Five different variations of the --k option, holding the --r option at its default.
python train.py svtrain.lower.txt modeltest.pt --k 50 // accuracy: 11.212697263208714
python train.py svtrain.lower.txt modeltest.pt --k 250 // accuracy: 8.229987025135028
python train.py svtrain.lower.txt modeltest.pt --k 250 // accuracy: 5.128089073956731
python train.py svtrain.lower.txt modeltest.pt --k 500 // accuracy: 15.056878187139796
python train.py svtrain.lower.txt modeltest.pt --k 600 // accuracy: 11.073896382124861

* Five different variations of the --r option, holding the --k option at its default.
python train.py svtrain.lower.txt modeltest.pt --r 50 // accuracy: 9.412811924806132
python train.py svtrain.lower.txt modeltest.pt --r 150 // accuracy: 9.592347847077638
python train.py svtrain.lower.txt modeltest.pt --r 250 // accuracy: 5.398147309978577
python train.py svtrain.lower.txt modeltest.pt --r 400 // accuracy: 9.729640022932319
python train.py svtrain.lower.txt modeltest.pt --r 500 // accuracy: 4.568359433933798

Include the best model and output text in your repository with its parameters.  Describe any patterns you see, if there are any.  Look at the output texts and make qualitative comments on the performances of the model.

The best model has an accuracy of 15%, a hiddensize of 500 and a default epoch.
The best model is "model.pt" and its output is "output.txt".
There is several "à" in the text which not seems to be in the Swedish alphabet. It may be caused by a french influence. For example in this sentence:
"à 17: 24, räg 10: à 9: 12, karn 9: 12 à 8 rdr"
In french we would say "à 17:24" to say "at 17:24".
Nevertheless, according to wikipedia, "á is a Swedish (old-fashioned) letter". Then my understanding might be wrong as it can be an old letter mistranslated.

However I'm unfamiliar with Swedish, and even with Google Translate's help, I'm unable to imagine how the word was supposed to be accentuated and what it currently means.

## Bonuses

## Other notes
