import ray
from csdfs.ray_cluster.node import CSDFSNode

class CSDFSCluster:
    def __init__(self, n_nodes=4, dim=16):
        ray.init(ignore_reinit_error=True)

        self.nodes = [
            CSDFSNode.remote(dim, seed=i)
            for i in range(n_nodes)
        ]

    def step(self, beta, lam):
        futures = [node.step.remote(self.get_global(), beta, lam)
                   for node in self.nodes]
        return ray.get(futures)

    def get_global(self):
        import torch
        states = [ray.get(n.step.remote(torch.zeros(16), 0, 0))["state"]
                  for n in self.nodes]
        return torch.stack(states).mean(0)
