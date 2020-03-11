"""Console script for codecounter."""
import argparse
import sys
from .codecounter import Counter
import os



def main():
    """Console script for codecounter."""
    parser = argparse.ArgumentParser(description=
                                     """
                                     This code looks a repository and inspects the number of lines in each file
                                     within that repository. It then outputs the results in the form of a csv with
                                     columns: FileType, File, Number_Of_Lines.

                                     The use case of this tool is determine how many lines, and where those lines exist
                                     (what type of files) in a repository).

                                     Later changes will most likely add some plotting and analysis. Currently (03/10/20)
                                     this tool is vey simple, analysis is to be done outside of this module.
                                     """)
    parser.add_argument('_', nargs='*')
    parser.add_argument('-s', '--source', metavar='SOURCE', type=str,
                        nargs=1, required=True,
                        help="Directory or Repository to Examine")
    parser.add_argument('-csv', '--output_file_destination', type=str,
                        required=True, help="This will be the destination folder where the "
                                            "code csv's will be written to. They will be named"
                                            "according to the directory given in --source.")
    args = parser.parse_args()

    print("Arguments: " + str(args._))

    if os.path.isdir(args.source):
        pass
    else:
        raise NotADirectoryError("{} is not a valid directory.".formate(args.source))
    if os.path.isdir(args.output_file_destination):
        pass
    else:
        raise NotADirectoryError("{} is not a valid directory.".format(args.output_file_destination))


    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
