iterations = 1000

import numpy as np
import matplotlib.pyplot as plt

def simulate_data_fixed_ISI(N=420):
    dg_hrf = glover_hrf(tr=1, oversampling=1)

    # Create indices in regularly spaced intervals (9 seconds, i.e. 1 sec stim + 8 ISI)
    stim_onsets = np.arange(10, N - 15, 9)
    stimcodes = np.repeat([1, 2], stim_onsets.size / 2)  # create codes for two conditions
    np.random.shuffle(stimcodes)  # random shuffle
    stim = np.zeros((N, 1))

    c = np.array([[0, 1, 0], [0, 0, 1]])

    # Fill stim array with codes at onsets
    for i, stim_onset in enumerate(stim_onsets):
        stim[stim_onset] = 1 if stimcodes[i] == 1 else 2

    stims_A = (stim == 1).astype(int)
    stims_B = (stim == 2).astype(int)

    reg_A = np.convolve(stims_A.squeeze(), dg_hrf)[:N]
    reg_B = np.convolve(stims_B.squeeze(), dg_hrf)[:N]
    X_fix = np.hstack((np.ones((reg_B.size, 1)), reg_A[:, np.newaxis], reg_B[:, np.newaxis]))
    dvars = [(c[i, :].dot(np.linalg.inv(X_fix.T.dot(X_fix))).dot(c[i, :].T))
             for i in range(c.shape[0])]
    eff_fix = c.shape[0] / np.sum(dvars)
    return X_fix, eff_fix


def simulate_data_jittered_ISI(N=420):
    dg_hrf = glover_hrf(tr=1, oversampling=1)

    stim_onsets = np.arange(10, N - 15, 9)
    stimcodes = np.repeat([1, 2], stim_onsets.size / 2)
    np.random.shuffle(stimcodes)

    # Here, we pick some *deviations* from the standard ISI (i.e., 8),
    # so possible ISIs are (8 - 2, 8 - 1, 8 - 0, 8 + 1, 8 + 2)
    ISIs = np.repeat([-2, -1, 0, 1, 2], repeats=11)
    np.random.shuffle(ISIs)

    stim = np.zeros((N, 1))
    c = np.array([[0, 1, 0], [0, 0, 1]])

    for i, stim_onset in enumerate(stim_onsets):
        # We subtract the stim-onset with -2, -1, 0, 1, or 2 (from ISIs)
        # to simulate jittering
        stim[stim_onset - ISIs[i]] = 1 if stimcodes[i] == 1 else 2

    stims_A = (stim == 1).astype(int)
    stims_B = (stim == 2).astype(int)
    reg_A = np.convolve(stims_A.squeeze(), dg_hrf)[:N]
    reg_B = np.convolve(stims_B.squeeze(), dg_hrf)[:N]
    X_jit = np.hstack((np.ones((reg_B.size, 1)), reg_A[:, np.newaxis], reg_B[:, np.newaxis]))

    # Loop over the two contrasts
    dvars = [(c[i, :].dot(np.linalg.inv(X_jit.T.dot(X_jit))).dot(c[i, :].T))
             for i in range(c.shape[0])]
    eff_jit = c.shape[0] / np.sum(dvars)
    return X_jit, eff_jit


# simulate_data_fixed_ISI(N = 420)

simulate_data_jittered_ISI(N=420)
a = np.zeros((2, iterations))
for i in range(iterations):
    a[0, i] = simulate_data_jittered_ISI(N=420)[1]
    a[1, i] = simulate_data_fixed_ISI(N=420)[1]

bins = np.linspace(np.amin(a), np.amax(a), 32)
plt.hist([a[0], a[1]], bins, label=['Jittered ISI', 'Fixed ISI'])
plt.legend(loc='upper right')
plt.xlabel('Efficiency')
plt.ylabel('Simulated sample count')
plt.title('ISI type efficiency comparison')
plt.show()


