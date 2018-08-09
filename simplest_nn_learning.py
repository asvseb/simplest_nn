import numpy as np

def sigmoid(x):
    return 1/(1+ np.exp(-x))

def dot(v,w):
    return sum( v_i * w_i for v_i, w_i in zip(v,w) )
#
#########################################################
#nn - list (layers) of
#             lists (neurons) of
#                    lists (weights)
#########################################################
def feedforward( layers_neurons_weights, input):
    outputs=[]
    for eachlayer in layers_neurons_weights:
        print ("eachlayer = " + str(eachlayer) )
        thislayeroutputlist=[]
        for eachneuron in eachlayer:
            print ("eachneuron =" + str(eachneuron) )
            input = input + [1]
            print("input = " + str(input))
            sumofprods =  dot ((eachneuron),input)
            print(sumofprods)
            activatedvalue=sigmoid(sumofprods)
            print('activatedvalue = ',activatedvalue)
            thislayeroutputlist.append(activatedvalue)
        input = thislayeroutputlist


simple_network = [# hidden layer
                [
                    [10, 20 ] # 'and' neuron
                ],
                # output layer
                [
                    [50]
                ]
              ] # '2nd input but not 1st input' neuron
#Layer looks like this
#######################
#   (input = 0)  ----10--- activation----( Neuron )  -----activation------( output)
#                      -
#                  -20
#   (input = 1) -
#######################

feedforward( simple_network,[0,1] )

