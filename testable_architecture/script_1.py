import os
import pandas as pd


def main(input_data_reference, intermediary_data_reference):
    """
    Transform input data and output to intermediary location.

    Parameters:
    ------------
    input_data_reference: str
        Filepath of a csv containing input data.
    intermediary_data_reference: str
        Filepath where a csv containing intermediary data
        will be written.

    Returns:
    ---------
    None

    """

    print(f'Reading input file {input_data_reference}.')
    input_df = pd.read_csv(input_data_reference)

    intermediary_df = input_df * 2

    intermediary_df.to_csv(intermediary_data_reference, index=False)
    print(f'Wrote intermediary file {intermediary_data_reference}.')


if __name__ == "__main__":
    main(
        input_data_reference=os.environ["INPUT_DATA_REFERENCE"],
        intermediary_data_reference=os.environ["INTERMEDIARY_DATA_REFERENCE"],
    )
