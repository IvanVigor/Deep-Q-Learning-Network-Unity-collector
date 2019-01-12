import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Agent of the banana env"""

    def __init__(self, state_size, action_size, seed, hidden_1=64, hidden_2=64):
        """Init function of neural model.
        Parameteres
        ======
            state_size (int): Space of possible values, 37 different input dimensions
            action_size (int): Number of possible actions, 4 possible actions
            seed (int): Random seed
            hidden_1 (int): Number of units in first hidden layer, default 64
            hidden_2 (int): Number of units in second hidden layer, default 64
	    
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, hidden_1)
        self.fc2 = nn.Linear(hidden_1, hidden_2)
        self.fc3 = nn.Linear(hidden_2, action_size)

    def forward(self, state):

        input_elem = F.relu(self.fc1(state))
        input_elem = F.relu(self.fc2(input_elem))
        return self.fc3(input_elem)

