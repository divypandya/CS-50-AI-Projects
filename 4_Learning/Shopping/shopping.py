import csv
import sys
import numpy as np
import time

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    print('Loading Data...')
    evidence, labels = load_data(sys.argv[1])
    time.sleep(1)
    print('Loaded Data.')
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    print('training model...')
    model = train_model(X_train, y_train)
    time.sleep(1)
    print('training completed.')
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    time.sleep(0.5)
    print('Report on Testing dataset: ')
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open('shopping.csv') as f:
        reader = csv.reader(f)
        cols = next(reader)

        int_cols =  ['Administrative', 'Informational', 'ProductRelated', 'OperatingSystems',
                    'Browser', 'Region', 'TrafficType']
        float_cols = ['Administrative_Duration', 'Informational_Duration',
                    'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay']

        int_col_idx = [cols.index(col_name) for col_name in cols if col_name in int_cols]
        float_col_idx = [cols.index(col_name) for col_name in cols if col_name in float_cols]
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        # index of 
        # month : 10
        # VisitorType : 15
        # Weekend : 16
        evidence = []
        labels = []
        for row in reader:
            temp = np.zeros(shape = (17,))
            temp_row = np.array(row)

            temp[int_col_idx] = list(temp_row[int_col_idx].astype(int))
            temp[float_col_idx] = list(temp_row[float_col_idx].astype(float))

            temp[10] = months.index(temp_row[10])
            temp[15] = 1 if temp_row[15] == 'Returning_Visitor' else 0
            temp[16] = 1 if temp_row[16] == 'TRUE' else 0
            
            evidence.append(list(temp))
            labels.append(1 if temp_row[17] == 'TRUE' else 0)
    
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(evidence, labels)
    return clf

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    y_true = np.array(labels)
    y_pred = np.array(predictions)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tpr = tp / (tp + fn)
    tnr = tn / (tn + fp)
    return (tpr, tnr)

if __name__ == "__main__":
    main()
