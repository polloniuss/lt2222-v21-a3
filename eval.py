import argparse
import numpy as np
import pandas as pd
import torch
import train
from train import a as pre_process

def alter_g(x, p, correct_len):
    z = np.zeros(correct_len)
    z[p.index(x)] = 1
    return z

def alter_b(u, p, correct_len):
    gt = []
    gr = []
    for v in range(len(u) - 4):
        if u[v+2] not in vowels:
            continue
        
        h2 = vowels.index(u[v+2])
        gt.append(h2)
        r = np.concatenate([alter_g(x, p, correct_len) for x in [u[v], u[v+1], u[v+3], u[v+4]]])
        gr.append(r)

    return np.array(gr), np.array(gt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_model", type=str, help="A model produced by train.py.") 
    parser.add_argument("train_data", type=str, help="A train data txt file.")
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
    processed_train_data = pre_process(args.train_data)
    correct_len = len(processed_train_data[1])
    test_features, test_classes = alter_b(processed_test_data[0], processed_test_data[1], correct_len)
    
    #Use the model to predict instances.
    tf = torch.from_numpy(test_features)
    tc = torch.from_numpy(test_classes)
    
    pred_instances = train_model(tf.float())
    predicted = pred_instances.argmax(dim=1).numpy()
    truth = tc.numpy()
    
    #Write the text with the predicted (as opposed to the real) vowels back into an output file.
    file_text = []
    i = 0
    for ch in processed_test_data[0]:
        if ch in vowels:
            file_text.append(vowels[predicted[i]])
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
    
    accuracy = tp_tn / len(truth)
    print("Accuracy of the model: ", accuracy)
    