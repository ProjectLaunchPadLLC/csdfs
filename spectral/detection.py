import numpy as np

class SpectralClusterDetector:
    def detect(self, eig_series):
        history = np.array(eig_series)
        clusters = []

        for i in range(history.shape[1]):
            var = np.var(history[:, i])
            persistence = np.mean(history[:, i] > 0.1)

            if var < 0.02 and persistence > 0.8:
                clusters.append(i)

        return clusters
