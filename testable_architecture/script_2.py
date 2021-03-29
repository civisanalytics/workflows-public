import os
import pandas as pd


def main(intermediary_tbname, output_tbname, db_name):
    """
    Transform intermediary data and output to final destination.

    Parameters:
    ------------
    intermediary_tbname: str
        schema.tablename containing intermediary data.
    output_tbname: str
        Filepath where a csv containing output data
        will be written.
    db_name: str
        Name of the database on which `intermediary_tbname`
        exists and `output_tbname` will be written.

    Returns:
    ---------
    None

    """

    intermediary_df = pd.read_csv(intermediary_tbname)
    print(f"Read intermediary table {intermediary_tbname}:\n{intermediary_df}")

    output_df = intermediary_df * 10
    print(f"Output data:\n{output_df}")

    output_df.to_csv(output_tbname, index=False)
    print(f"Wrote output data to table {output_tbname} on database {db_name}.")


if __name__ == "__main__":
    main(
        intermediary_tbname=os.environ["INTERMEDIARY_DATA_REFERENCE"],
        output_tbname=os.environ["OUTPUT_DATA_REFERENCE"],
        db_name=os.environ["DB_NAME"],
    )
