import re
import sys
import csv

def importData(fileName):
    # The CSV file contains the lastname, firstname, [ list of lastnames of co-authors]
    data = []
    with open(fileName, 'r') as csvfile:
        spamreader = csv.reader(csvfile, skipinitialspace=True, delimiter=',', quotechar='|')
        for row in spamreader:
            # removing empty entries
            while (len(row) > 0 and row[-1] == ''):
                row.pop()
            if (len(row) > 0):
                data.append(row)
    return data

def cleanupData(data):
    # create a list of authors (' lastname)
    authors = []
    for i in data:
        authors.append(i[0])

    collaborators = []
    collaboratorsGraph = []
    for row in data:
        row.pop(0)  # remove first row (lastname)
        row.pop(0)  # remove second row (firstname), which now is the first row
        collaborators.append(row)


    for collaborator in collaborators:
        edges = []
        for i in range(len(collaborator)):
            for j in range(len(authors)):
                if(collaborator[i]==authors[j]):
                    edges.append(j)
        collaboratorsGraph.append(edges)

    return authors, collaborators, collaboratorsGraph

def main():
    fileName = r"collaborationData.csv"
    data = importData(fileName)
    authors, collaborators, graph = cleanupData(data);
    print(authors)
    print(collaborators)
    print(graph)
if  __name__ =='__main__':main()
