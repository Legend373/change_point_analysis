import numpy as np

def summarize_impact(trace, df):

    tau_samples = trace.posterior["tau"].values.flatten()
    mu1_samples = trace.posterior["mu1"].values.flatten()
    mu2_samples = trace.posterior["mu2"].values.flatten()

    change_index = int(np.median(tau_samples))
    change_date = df.iloc[change_index]["Date"]

    mu1 = mu1_samples.mean()
    mu2 = mu2_samples.mean()

    impact = (mu2 - mu1) / abs(mu1)

    print("Estimated change date:", change_date)
    print("Mean before:", mu1)
    print("Mean after:", mu2)
    print("Relative change:", impact)
