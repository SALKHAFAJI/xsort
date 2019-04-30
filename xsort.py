
class xsort():

    # to find the max number in list we can 
    # use max() function in python
    
    def findMax(_list):

        mout = _list[0]
        for i in _list:
            if i >= mout:
                mout = i
        return mout

    def run(_list):

        list_ = []

        for i in range(len(_list)):

            #find biggest number in list
            big = xsort.findMax(_list)

            #add the biggest number to new list at position [0]
            list_.insert(0, big)

            #remove the bigest number from old list
            _list.remove(big)

        return list_



test_list = [55,1,69,55,2,63,96,3,41,-5,-55,88,100,-9]

if __name__ == "__main__":
    print(xsort.run(test_list))

