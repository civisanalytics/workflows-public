import os
import pandas as pd


def main(intermediary_data_reference, output_data_reference):
    """
    Transform intermediary data and output to final destination.

    Parameters:
    ------------
    intermediary_data_reference: str
        Filepath of a csv containing intermediary data.
    output_data_reference: str
        Filepath where a csv containing output data
        will be written.

    Returns:
    ---------
    None

    """

    print(f'Reading intermediary file {intermediary_data_reference}.')
    intermediary_df = pd.read_csv(intermediary_data_reference)

    output_df = intermediary_df * 10
    print(f'Output data:\n{output_df}')

    output_df.to_csv(output_data_reference, index=False)
    print(f'Wrote output file {output_data_reference}.')


if __name__ == "__main__":
    main(
        intermediary_data_reference=os.environ["INTERMEDIARY_DATA_REFERENCE"],
        output_data_reference=os.environ["OUTPUT_DATA_REFERENCE"],
    )
