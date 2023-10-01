import numpy as np


class SignalProcessing:
    """
    Process a signal to get characteristics of a signal
    """

    def __init__(
        self, input_signal: np.ndarray, sampling_frequency: float, n_samples: float
    ):
        """
        Args:
            input_signal (np.ndarray): Signal to process
            sampling_frequency (float): [Hz]
            n_samples (float): [-]
        """
        self.sampling_frequency = sampling_frequency
        self.n_samples = n_samples
        self.input_signal = input_signal

        # To be defined
        self.frequencies = np.zeros(self.n_samples)
        self.magnitude = np.zeros(self.n_samples)
        self.offset = 0.0

    def _compute_fft(self):
        """
        Compute FFT of the signal and only use the positive frequencies.

        Returns:
            np.ndarray: fft_result
        """
        fft_result = np.fft.fft(self.input_signal)[1 : self.n_samples // 2]
        self.frequencies = np.fft.fftfreq(
            self.n_samples, 1.0 / self.sampling_frequency
        )[1 : self.n_samples // 2]
        return fft_result

    def _get_magnitude(self, fft_result: np.ndarray):
        """
        Args:
            fft_result (np.ndarray): fft of the iput signal

        Returns:
            np.ndarray: magnitude
        """
        return 2.0 * np.abs(fft_result) / self.n_samples

    def process(self, n_main_frequencies: int):
        """
        Process the signal and get magnitude, phase and offset.

        Args:
            n_main_frequencies (int): Chose how many frequencies to include as the most important.

        Returns:
            tuple: frequency, magnitude and phase of the n main components
        """
        fft_result = self._compute_fft()
        self.magnitude = self._get_magnitude(fft_result)
        phase = np.angle(fft_result)
        self.offset = np.round(np.mean(self.input_signal), 1)

        main_frequency_index = np.flip(np.argsort(self.magnitude)[-n_main_frequencies:])
        main_frequencies = self.frequencies[main_frequency_index]
        main_magnitudes = self.magnitude[main_frequency_index]
        main_phases = phase[main_frequency_index]
        return main_frequencies, main_magnitudes, main_phases
