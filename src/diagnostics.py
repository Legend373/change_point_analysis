import arviz as az
import matplotlib.pyplot as plt

def summarize(trace):
    print(az.summary(trace))


def plot_trace(trace):
    az.plot_trace(trace)
    plt.show()


def plot_tau(trace):
    tau_samples = trace.posterior["tau"].values.flatten()

    plt.hist(tau_samples, bins=50)
    plt.title("Posterior Change Point Distribution")
    plt.xlabel("Index")
    plt.ylabel("Frequency")
    plt.show()
