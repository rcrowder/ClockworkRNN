
class Config(object):

    output_dir = "./output/"

    # Clockwork RNN parameters
    # periods     = [1, 2, 4, 8, 16, 32, 64, 128]   # P1
    periods     = [1, 4, 16, 64]                    # P2
    num_steps   = 256
    num_input   = 1
    num_hidden  = 64
    num_output  = 1

    # Optmization parameters
    num_epochs          = 64
    batch_size          = 256
    optimizer           = "rmsprop"
    max_norm_gradient   = 10.0

    # Learning rate decay schedule
    learning_rate       = 10e-4
    learning_rate_decay = 0.975
    learning_rate_step  = 256
    learning_rate_min   = 1e-5



