import argparse


def get_parser():
    """
    Defining default parameters to generate the signal.

    Returns:
        class: parser with all required input to the signal generation
    """
    parser = argparse.ArgumentParser(
        description="Set optional parameters, List of frequencies and phases must be the same length."
    )

    parser.add_argument(
        "--fList",
        type=float,
        nargs="+",
        default=[10.0, 50.0],
        help="List of the signals frequencies [Hz] [default: %(default)s ]",
    )
    parser.add_argument(
        "--phaseList",
        type=float,
        nargs="+",
        default=[0.0, 90.0],
        help="List of phases [deg] [default: %(default)s ]",
    )
    parser.add_argument(
        "--ampList",
        type=float,
        nargs="+",
        default=[1.0, 1.0],
        help="List of amplitudes [default: %(default)s ]",
    )
    parser.add_argument(
        "--fSamp",
        type=float,
        default=1000.0,
        help="Sampling frequency [Hz] [default: %(default)s ]",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=1.0,
        help="Duration of signal [s] [default: %(default)s ]",
    )
    parser.add_argument(
        "--offset",
        type=float,
        default=0.0,
        help="Offset [] [default: %(default)s ]",
    )
    parser.add_argument(
        "--sigma",
        type=float,
        default=0.1,
        help="Noise assumed to be normal distrubuted with standard deviation [default: %(default)s ]",
    )
    parser.add_argument(
        "--mean",
        type=float,
        default=0.0,
        help="Noise assumed to be normal distrubuted centered at [default: %(default)s ]",
    )
    return parser.parse_args()
