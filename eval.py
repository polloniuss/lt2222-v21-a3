import argparse
import numpy as np
import torch
import train
from train import a as pre_process
from train import g
from train import b as instances

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_model", type=str, help="A model produced by train.py.") 
    parser.add_argument("test_data", type=str, help="A test data txt file.")
    parser.add_argument("output_filename", type=str, help="Path and filename for the output data.")
    
    args = parser.parse_args()
    
    vowels = train.vowels
    
    #Load a model produced by train.py. (Take a look at model.py.)
    train_model = torch.load(args.train_model)
    train_model.eval()
    
    #Load the test data.
    processed_test_data = pre_process(args.test_data)
    
    #Create evaluation instances compatible with the training instances.
    test_features, test_classes = instances(processed_test_data[0], processed_test_data[1])
    
    #Use the model to predict instances.
    pred_instances = train_model(test_features.unsqueeze(0))
    predicted = pd.Series(pred_instances.squeeze(0).argmax(dim=1).numpy())
    truth = pd.Series(test_classes.numpy())
    
    #Write the text with the predicted (as opposed to the real) vowels back into an output file.
    file_text = []
    i = 0
    for ch in processed_test_data[0]:
        if ch in vowels:
            file_text.append(vowels[i])
            i += 1
        else:
            file_text.append(ch)
    
    with open(args.output_filename, "w") as file:
        file.write(''.join(file_text))
    
    #Print the accuracy of the model to the terminal.
    tp_tn = 0
    for j in range(len(predicted)):
        if predicted[j] == truth[j]:
            tp_tn += 1
    
    accuracy = len(tp_tn) / len(truth)
    print("Accuracy of the model: ", accuracy)
    