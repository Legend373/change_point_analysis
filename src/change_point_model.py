import pymc as pm
import numpy as np

def build_model(returns):

    returns = returns.astype("float32")

    n = len(returns)
    time_idx = np.arange(n)

    with pm.Model() as model:

        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)

        mu1 = pm.Normal("mu1", mu=0, sigma=0.05)
        mu2 = pm.Normal("mu2", mu=0, sigma=0.05)

        sigma = pm.HalfNormal("sigma", sigma=0.05)

        mu = pm.math.switch(time_idx < tau, mu1, mu2)

        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

    return model


def sample_model(model):
    with model:
        trace = pm.sample(
            draws=1000,
            tune=500,
            chains=2,
            cores=2,
            target_accept=0.9,
            progressbar=True,
            return_inferencedata=True
        )
    return trace
