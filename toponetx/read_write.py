"""Read/write utilities."""

import pickle


def to_pickle(obj, filename: str) -> None:
    """Write object to a pickle file.

    Parameters
    ----------
    obj : object
        Object to write.
    filename : str
        Filename.
    """
    with open(filename, "wb") as f:
        pickle.dump(obj, f)


def load_from_pickle(filepath):
    """Return object from file.

    Parameters
    ----------
    filepath : str
        Filepath.

    Returns
    -------
    object
        Object.
    """
    with open(filepath, "rb") as f:
        temp = pickle.load(f)
    return temp
