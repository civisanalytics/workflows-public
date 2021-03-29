import os
import pandas as pd
import civis


def main(input_filepath, intermediary_tbname, db_name):
    """
    Transform input data and output to intermediary table.

    Parameters:
    ------------
    input_filepath: str
        Filepath of a csv containing input data.
    intermediary_tbname: str
        schema.tablename where intermediary data
        will be written.
    db_name: str
        Name of the database on which `intermediary_tbname`
        will be written.

    Returns:
    ---------
    None

    """

    input_df = pd.read_csv(input_filepath)
    print(f"Read input file {input_filepath}:\n{input_df}")

    intermediary_df = input_df * 2
    print(f"Intermediary data:\n{intermediary_df}")

    civis.io.dataframe_to_civis(
        df=intermediary_df, database=db_name, existing_table_rows="drop"
    )
    print(
        f"Wrote intermediary data to table {intermediary_tbname} on database {db_name}."
    )


if __name__ == "__main__":
    main(
        input_filepath=os.environ["INPUT_FILEPATH"],
        intermediary_tbname=os.environ["INTERMEDIARY_TBNAME"],
        db_name=os.environ["DB_NAME"],
    )
