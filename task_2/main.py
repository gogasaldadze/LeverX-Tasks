from src.cli.runner import run


"""
 Student-room Data processor

 It handles:
    Command line argument parsing
    Data loading and merging
    Exporting results in specified formats such as json and xml.

    
Common OPTIONAL arguments:
   -f xml           # Output format (default: json)
   -o output.xml    # Custom output filename


To run the script, Use commands:
    1. for default json output use :  python main.py -s data/input/students.json -r data/input/rooms.json  -o data/output/result
    2. To generate xml file specify -f/--format :  python main.py -s data/input/students.json -r data/input/rooms.json -f xml  -o data/output/result


 
"""


if __name__ == "__main__":
    run()
