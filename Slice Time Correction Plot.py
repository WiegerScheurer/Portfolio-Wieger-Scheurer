slice_data = np.load('stc_data.npy')
print("Slice data is of shape (time x slices): %s" % (slice_data.shape,))

stc_data = np.zeros(slice_data.shape)

# YOUR CODE HERE
TR = 3
exp_time = 60
vols = exp_time // TR
n_slices = 32
dt = TR / n_slices

onset_s16 = np.linspace(dt * 15, exp_time + dt * 15, vols, endpoint=False)

slice_onsets_acr_vol = np.zeros((vols, n_slices))

plt.figure(figsize=(15, 8))
plt.subplot(2, 1, 1)

for i in range(n_slices):
    t_slice_todo = np.linspace(dt * i, exp_time + dt * i, vols, endpoint=False)
    slice_onsets_acr_vol[:, i] = t_slice_todo
    plt.plot(onset_s16, slice_data[:, i])
    plt.grid()
    plt.ylabel("Activation (A.U.)", fontsize=20)
    plt.title("Original slicewise responses", fontsize=25)

plt.subplot(2, 1, 2)
for i in range(slice_data.shape[1]):
    resampler = interp1d(slice_onsets_acr_vol[:, i], slice_data[:, i], kind='cubic', fill_value='extrapolate')
    stc_data[:, i] = resampler(onset_s16)
    plt.plot(onset_s16, stc_data[:, i])
    plt.grid()
    plt.title("Slice-time corrected data", fontsize=25)
    plt.xlabel("Time (seconds)", fontsize=20)
    plt.ylabel("Activation (A.U.)", fontsize=20)

plt.tight_layout()
plt.show()

