import sys

import time

from M2.ddi_vae import DdiVariationalAutoencoder

sys.path.extend(['/home/cdy/ykq/vae', '/home/cdy/ykq/vae/M2'])
from ddi.data_process import load_dataset
import utils

from M2.vae import VariationalAutoencoder
# from ddi.data_process import load_dataset
import numpy as np
import M2.data.mnist as mnist #https://github.com/dpkingma/nips14-ssl

##if __name__ == '__main__':
def train_ddi_vae(dim_z, hidden_layers_px, hidden_layers_qz, save_path):
    #############################
    ''' Experiment Parameters '''
    #############################

    num_batches = 100       #Number of minibatches in a single epoch, num_examples % self.num_batches == 0
    # dim_z = 50              #Dimensionality of latent variable (z)
    epochs = 3001           #Number of epochs through the full dataset
    learning_rate = 3e-3    #Learning rate of ADAM
    l2_loss = 1e-6          #L2 Regularisation weight
    seed = 31415            #Seed for RNG

    #Neural Networks parameterising p(x|z), q(z|x)
    # hidden_layers_px = [ 600, 1000, 800, 500 ]
    # hidden_layers_qz = [ 600, 1000, 800, 500 ]

    ####################
    ''' Load Dataset '''
    ####################

    # mnist_path = 'mnist/mnist_28.pkl.gz'
    # #Uses anglpy module from original paper (linked at top) to load the dataset
    # train_x, train_y, valid_x, valid_y, test_x, test_y = mnist.load_numpy(mnist_path, binarize_y=True)
    #
    # x_train, y_train = train_x.T, train_y.T
    # x_valid, y_valid = valid_x.T, valid_y.T
    # x_test, y_test = test_x.T, test_y.T

    x_train, y_train, x_valid, y_valid, x_test, y_test = load_dataset("/home/cdy/ykq/vae/ddi/train_dataset")
    utils.print_metrics(['x_train', x_train.shape[0], x_train.shape[1]],
                        ['y_train', y_train.shape[0], y_train.shape[1]],
                        ['x_valid', x_valid.shape[0], x_valid.shape[1]],
                        ['y_valid', y_valid.shape[0], y_valid.shape[1]],
                        ['x_test', x_test.shape[0], x_test.shape[1]],
                        ['y_test', y_test.shape[0], y_test.shape[1]],
                        )

    dim_x = x_train.shape[1]
    dim_y = y_train.shape[1]

    ######################################
    ''' Train Variational Auto-Encoder '''
    ######################################

    VAE = DdiVariationalAutoencoder(   dim_x = dim_x,
                                    dim_z = dim_z,
                                    hidden_layers_px = hidden_layers_px,
                                    hidden_layers_qz = hidden_layers_qz,
                                    l2_loss = l2_loss )

    #draw_img uses pylab and seaborn to draw images of original vs. reconstruction
    #every n iterations (set to 0 to disable)

    VAE.train(  x = x_train, x_valid = x_valid, epochs = epochs, num_batches = num_batches, save_path=save_path,
                learning_rate = learning_rate, seed = seed, stop_iter = 30, print_every = 10, draw_img = 0 )

    
if __name__ == '__main__':
    tmp_hidden_layers_px = [600]
    tmp_hidden_layers_qz = [600]
    dim_z = 500
    save_path = 'checkpoints/model_VAE_{}_{}.cpkt'.format(dim_z,
                                                          time.strftime("%m-%d-%H%M%S", time.localtime()))
    train_ddi_vae(dim_z, tmp_hidden_layers_px, tmp_hidden_layers_qz, save_path)