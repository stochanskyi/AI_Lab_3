import sklearn
import sklearn.datasets
import sklearn.model_selection
import sklearn.neighbors

newgroups_bunch = sklearn.datasets.fetch_20newsgroups_vectorized()

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    newgroups_bunch.data,
    newgroups_bunch.target,
    random_state=0)


def newgroups_target_names():
    return newgroups_bunch.target_names


def newgroups_data():
    return newgroups_bunch.data


def neighbours_classifier(neighbours_count):
    knn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=neighbours_count)
    knn.fit(x_train, y_train)
    return knn


def get_learning_score(knn):
    return knn.score(x_test, y_test)
