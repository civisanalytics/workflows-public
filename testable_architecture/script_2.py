import os
import pandas as pd


def main(intermediary_data_reference, output_data_reference):
    intermediary_df = pd.read_csv(intermediary_data_reference)
    output_df = intermediary_df * 10
    output_df.to_csv(output_data_reference, index=False)


if __name__ == "__main__":
    main(
        intermediary_data_reference=os.environ["INTERMEDIARY_DATA_REFERENCE"],
        output_data_reference=os.environ["OUTPUT_DATA_REFERENCE"],
    )
