"""
utils.py
"""

class ListUtil:
    """
    Generic functions on lists
    """

    @staticmethod
    def permute(inputlist):
        """
        Create all permutations of a given list (include strings)
        """
        if len(inputlist) <= 1:
            yield inputlist
        else:
            chunk = inputlist[0]
            for item in ListUtil.permute(inputlist[1:]):
                for i in range(0, len(item)+1):
                    yield item[0:i] + chunk + item[i:]
