import pathlib

def fileToList(filename):

    pfilename = pathlib.Path(filename)
    filelist = []

    try:
        fin = open(pfilename, 'r')

        for line in fin:

            if line == "":
                return filelist

            else:
                nstr = line.strip()
                filelist.append(nstr)

        fin.close()

    except IOError:
        return filelist

    return filelist

def returnFirstString(strings):

    emstr = ''

    for i in range(len(strings)):

        if i >= 0:
            return strings[0]

    return emstr

def strandsAreNotEmpty(strand1, strand2):

    strndlen1 = len(strand1)
    strndlen2 = len(strand2)

    if strndlen1 >= 1 and strndlen2 >= 1:
        return True
    elif strndlen2 < 1 or strndlen1 < 1:
        return False

def strandsAreEqualLengths(strand1, strand2):

    strndlen1 = len(strand1)
    strndlen2 = len(strand2)

    if strndlen1 == strndlen2:
        return True
    else:
        return False


def candidateOverlapsTarget(target, candidate, overlap):
    return target[len(target)-overlap:] == candidate[:overlap]


def findLargestOverlap(target, candidate):

    count = 0

    if not strandsAreNotEmpty(target, candidate):
        return -1

    if not strandsAreEqualLengths(target, candidate):
        return -1

    for i in range(len(target)+1):

        if candidateOverlapsTarget(target, candidate, i):
            count = i

    return count


def findBestCandidate(target, candidates):

    beststrand = ""
    bestoverlap = 0

    for i in range(len(candidates)):
        overlap = findLargestOverlap(target, candidates[i])

        if overlap > bestoverlap:
            bestoverlap = overlap

            beststrand = candidates[i]

    return (beststrand, bestoverlap)


def joinTwoStrands(target, candidate, overlap):

    newstrand = target + candidate[overlap:]

    return newstrand

def main():

    target = input("Enter the target DNA strand text File -> ")
    candidate = input("Enter the candidate DNA strand text File -> ")

    newtarget =  fileToList(target)
    newcandidate = fileToList(candidate)

    target2 = returnFirstString(newtarget)

    bestcandidate = findBestCandidate(target2, newcandidate)

    print(target2)

    print(joinTwoStrands(target2,bestcandidate[0],bestcandidate[1]))


if __name__ == '__main__':
    main()
