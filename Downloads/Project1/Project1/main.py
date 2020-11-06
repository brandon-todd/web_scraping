"""
    Searches deep inside a directory structure, looking for duplicate file.
    Duplicates aka copies have the same content, but not necessarily the same name.
"""
__author__ = ""
__email__ = ""
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time
# noinspection PyUnresolvedReferences
from p1utils import all_files, compare


def search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a dictionary, where each key contains files with the same content

    Basic search strategy goes like this:
    - until the provided list is empty.
    - remove the 1st item from the provided file_list
    - search for its duplicates in the remaining list and put the item and all its duplicates into a new list
    - if that new list has more than one item (i.e. we did find duplicates) save the list in the list of lists
    As a result we have a list, each item of that list is a list,
    each of those lists contains files that have the same content
    """
    lol = {}
    while 0 < len(file_list):
        i = file_list.pop(0)  # pops last item in lst
        for k in file_list:
            if compare(i, k):
                if i not in list(lol.keys()):
                    lol.update({i: []})
                lol[i].append(k)

    return lol



def faster_search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a dictionary, where each key contains files with the same content

    Here's an idea: executing the compare() function seems to take a lot of time.
    Therefore, let's optimize and try to call it a little less often.
    """
    lol = {}
    lst1 = sorted(file_list, key = getsize)
    lst2 = sorted(file_list, key = getsize)
    #while 0 < len(file_list):
    #   i = file_list.pop(0)  # pops last item in lst  #6 seconds slower for some reason
    for i in lst1:
        if i in lst2:
            lst2.remove(i)
        for k in lst2:
            if getsize(k) <= getsize(i):
                if getsize(k) == getsize(i):
                    if compare(i, k):
                        if i not in list(lol.keys()):
                            lol.update({i: []})
                        lol[i].append(k)
                        lst1.remove(k)
                else:
                    lst2.remove(k)
            else:
                break

    return lol


def report(lol):
    """ Prints a report
    :param lol: dictionary (each containing files with equal content)
    :return: None
    Prints a report:
    - longest list, i.e. the files with the most duplicates
    - list where the items require the largest amount or disk-space
    """
    lst3 = list(lol.keys())
    print("== == Duplicate File Finder Report == ==")
    amount = list(lol[max(lol, key = lol.get)])
    print(f"{max(lol, key  = lol.get)} has the most duplicates: {len(amount)} ")
    print(f"The duplicates are: \n{amount}")
    most = ('', 0)
    for i in range(len(lst3)):
        if getsize(lst3[i])*len(list(lol.get(lst3[i]))) > most[1]:
            most = (f'{lst3[i]}', (getsize(lst3[i])*len(lol.get(lst3[i]))))
    print(f"{most[1]} total space could be save by deleting duplicates of {most[0]}")
    print(f"The {len(list(lol.get(most[0])))} copies are: \n{list(lol.get(most[0]))}")


if __name__ == '__main__':
    path = join(".", "images")
    # measure how long the search and reporting takes:
    t0 = time()
    report(search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")

    print("\n\n .. and now w/ a faster search implementation:")

    # measure how long the search and reporting takes:
    t0 = time()
    report(faster_search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")
