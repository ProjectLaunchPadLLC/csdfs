import ray
import torch
from csdfs.core.energy import NeuralEnergyField
from csdfs.core.langevin import langevin_step
from csdfs.core.operators import sync_operator, individuality_operator

@ray.remote
class CSDFSNode:
    def __init__(self, dim, seed=0):
        torch.manual_seed(seed)
        self.x = torch.randn(dim)
        self.energy = NeuralEnergyField(dim)

    def step(self, global_state, beta, lam):
        E = self.energy(self.x)
        grad = torch.autograd.grad(E, self.x, retain_graph=True, allow_unused=True)[0]
        if grad is None:
            grad = torch.zeros_like(self.x)

        self.x = langevin_step(self.x, grad)
        self.x += sync_operator(global_state, beta)
        self.x += individuality_operator(self.x, global_state, lam)

        cov = torch.outer(self.x, self.x)
        eig = torch.linalg.eigvalsh(cov)

        return {
            "state": self.x,
            "eig": eig.tolist()
        }
