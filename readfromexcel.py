from typing import List
import pandas
from models import Movie, Link, Rating, Tag


def readmovies(name: str) -> List:
    excelData = pandas.read_csv(name)
    lst = []

    for element in excelData.iloc:
        movie = Movie(element[0], element[1], element[2])
        lst.append(str(movie.__dict__))

    return lst


def readratings(name: str) -> List:
    excelData = pandas.read_csv(name)
    lst = []

    for element in excelData.iloc:
        rating = Rating(element[0], element[1], element[2], element[3])
        lst.append(str(rating.__dict__))

    return lst


def readlinks(name: str) -> List:
    excelData = pandas.read_csv(name)
    lst = []

    for element in excelData.iloc:
        link = Link(element[0], element[1], element[2])
        lst.append(str(link.__dict__))

    return lst


def readtags(name: str) -> List:
    excelData = pandas.read_csv(name)
    lst = []

    for element in excelData.iloc:
        tag = Tag(element[0], element[1], element[2], element[3])
        lst.append(str(tag.__dict__))

    return lst
