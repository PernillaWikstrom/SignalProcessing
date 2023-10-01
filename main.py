import matplotlib.pyplot as plt
import src


def main():
    """
    Main file to generate and to process signal.
    Result is plotted below.
    """
    args = src.get_parser()

    signal = src.Signal(args.fSamp, args.duration)
    cosine = signal.process(args)

    processor = src.SignalProcessing(cosine, args.fSamp, signal.n_samples)
    n_main_components = len(args.fList)
    main_frequency, main_magnitude, main_phase = processor.process(n_main_components)

    # Plotting
    fig0, ax0 = plt.subplots()
    ax0.plot(
        signal.time,
        cosine,
        label=f"Phases: {', '.join('{:0.1f}'.format(i) for i in main_phase)} radians, offset: {processor.offset}",
    )
    ax0.set_xlabel("Time [s]")
    ax0.set_ylabel("Amplitude")
    ax0.set_title("Original signal")
    ax0.grid()
    ax0.legend()

    fig1, ax1 = plt.subplots()
    ax1.plot(
        processor.frequencies,
        processor.magnitude,
        label=f"Magnitudes:\n{', '.join('{:0.1f} at {:0.1f} Hz'.format(main_magnitude[i], main_frequency[i]) for i in range(n_main_components))}",
    )
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Magnitude")
    ax1.set_title("Frequency Domain\nMagnitude at identified frequencies")
    ax1.legend()
    ax1.grid()
    plt.show()


if __name__ == "__main__":
    main()
