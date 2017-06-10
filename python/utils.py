class ListUtil:
    def permute(input):
        if len(input) <= 1:
            yield input
        else:
            chunk = input[0]
            for item in ListUtil.permute(input[1:]):
                for i in range(0,len(item)+1):
                    yield item[0:i] + chunk + item[i:]
