import argparse
import numpy as np


class Signal:
    """
    Takes generates a cosine signal with multiple frequency components
    """

    def __init__(self, sampling_frequency: float, duration_signal: float):
        """
        Initialte the signal generation.

        Args:
            sampling_frequency (float): [Hz]
            duration_signal (float): [s]
        """
        self.sampling_frequency = sampling_frequency
        self.n_samples = int(duration_signal * sampling_frequency)
        self.time = np.linspace(0, duration_signal, self.n_samples)

    def _add_noise(self, mean: float, sigma: float):
        """
        Draws random samples from a normal distribution to account for noisy signals.

        Args:
            mean (float): center of normal distribution
            sigma (float): standard deviation of normal distribution

        Returns:
            float: scalar
        """
        return np.random.normal(mean, sigma, self.n_samples)

    def _get_sinus(self, frequency: float, phase: float, amplitude: float):
        """
        Generate a sinus signal with the time array initialized from the constructor.

        Args:
            frequency (float): [Hz]
            phase (float): [rad]
            amplitude (float): signal

        Returns:
            np.ndarray: array of samples
        """

        return np.array(
            [amplitude * np.sin(2.0 * np.pi * frequency * t + phase) for t in self.time]
        )

    def process(self, args: argparse.ArgumentParser):
        """
        Addition of frequency components in the signal.

        Args:
            args (argparse.ArgumentParser): Chosen variables in the parser.py

        Returns:
            np.ndarray: signal
        """

        cosine = np.zeros((self.n_samples,))
        for i, frequency in enumerate(args.fList):
            cosine[:] += self._get_sinus(
                frequency, np.deg2rad(args.phaseList[i]), args.ampList[i]
            ) + self._add_noise(args.mean, args.sigma)
        return cosine + args.offset
