# collaborationGraphVisualization
    This repo contains a code for drawing collaboration graphs from a CSV file using NetworkX package.
    The output will look like this:
    ![Collaboration Graph](https://github.com/ahmadyan/collaborationGraphVisualization/raw/master/collaborations.jpg)
    The python program requires NetworkX and Mathplotlib libraries to be installed.

    The input file is a CSV file, with the the following format
    lastname, firstname, [lastname of co-authors]
    Example:
    * Smith, John, Einestein, Erdos, Turing
    * Einestein, Albert, Smith

    A full example is provided in collaborationData.csv
