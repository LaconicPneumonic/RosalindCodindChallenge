from collections import defaultdict
import functools
import multiprocessing


rnaCodonMapping = {'UUU': 'F',
                   'CUU': 'L',
                   'AUU': 'I',
                   'GUU': 'V',
                   'UUC': 'F',
                   'CUC': 'L',
                   'AUC': 'I',
                   'GUC': 'V',
                   'UUA': 'L',
                   'CUA': 'L',
                   'AUA': 'I',
                   'GUA': 'V',
                   'UUG': 'L',
                   'CUG': 'L',
                   'AUG': 'M',
                   'GUG': 'V',
                   'UCU': 'S',
                   'CCU': 'P',
                   'ACU': 'T',
                   'GCU': 'A',
                   'UCC': 'S',
                   'CCC': 'P',
                   'ACC': 'T',
                   'GCC': 'A',
                   'UCA': 'S',
                   'CCA': 'P',
                   'ACA': 'T',
                   'GCA': 'A',
                   'UCG': 'S',
                   'CCG': 'P',
                   'ACG': 'T',
                   'GCG': 'A',
                   'UAU': 'Y',
                   'CAU': 'H',
                   'AAU': 'N',
                   'GAU': 'D',
                   'UAC': 'Y',
                   'CAC': 'H',
                   'AAC': 'N',
                   'GAC': 'D',
                   'UAA': 'Stop',
                   'CAA': 'Q',
                   'AAA': 'K',
                   'GAA': 'E',
                   'UAG': 'Stop',
                   'CAG': 'Q',
                   'AAG': 'K',
                   'GAG': 'E',
                   'UGU': 'C',
                   'CGU': 'R',
                   'AGU': 'S',
                   'GGU': 'G',
                   'UGC': 'C',
                   'CGC': 'R',
                   'AGC': 'S',
                   'GGC': 'G',
                   'UGA': 'Stop',
                   'CGA': 'R',
                   'AGA': 'R',
                   'GGA': 'G',
                   'UGG': 'W',
                   'CGG': 'R',
                   'AGG': 'R',
                   'GGG': 'G'}


UPPER_BOUND = 1_000_000
originalProteinString = "MWNGPTEDLWRMHQNWAGTFYNSRQQPMNRIACHQLEKYTDFEDDTNCSCNCSLTCAVSRYAFGDIMGTWWDQGPRQIVSMGVVPGRASCGGRLEARGGYQRELCRYVGMKGDVMWRVMMWIATRFTKGGERTCHHRQTPDCADPRRRGEPDIFWIPPNTGQKNIHMVRWHSAFWLPYFKIETQFMDAVPFMAAYMSNSYFAVAFHHYQFDMNTKRLHCAMDLHHTICVTRSIMGFLHNSSNDDYAWQKQLGWWDCNCYAITNRPENTNFLGPVQWMDQSFPRCLNIEKFKQARIENCELEYFILWGEQWPFNVPYPMNTNGGNSYSRTKKADTMKFVFYQPMFAPWFYSQFVRTMIFSTLQAPPSMGQIIERFPHWAGCDMVDHIPNSEFYRWTMKTWVNLGFYQGTKDCWDYGTGHMVARKYDINQQEGGPYMDYSSQKLIELYFIWMMCKVPWKHREIVYHHIFFKTTAECNAFKAFHRAMGDYRDCLVCKFWLCQISLFRLCKEAVFIHHEHITTHDSPTSIWSDVRHFINFWWTCTYEKPFKKNHAKPAKLQNMIDFYERIWEMSMEMNMDVETICDIEFHVTSESSNSPCGLVVGWREDLAKEQQIQNKSPCGSAGQFYMPHISSAWEITNFMMDDTYVVGFKKDQQMVGKYVFVKWGGPWISHNPLDCICNGMEKGDSLCTWLSDNLWFYHGAFHLLCMASGSTEGVHLGLAEFRYRWNHQYVGQLFTICYKESHMDYTKGFAVFMAMMTSSVKRVARMLDWFQHRMMYSRIWYYEAHDTPQAIPSCADKMHIQTIMCLYTLYHEPMDPNHRSKICTWPHMYMTYYFTREMLEKQFYWFLGKATAPWTEQIIVYWHAWDMVPANCWDMQPCQFYEQDFKSKCYTFQGQYFHPCTLLYAPVQNKATSPCLDCQTIRCDNNVRRCSIRETEWEDIYCAHACCVIMNWSLYCMLIQDYRQPAWEQFWNPMIYGCSSFFTFHYGNVDRSHCPPAAH"
proteinToRnaCount = defaultdict(int)

for key, val in rnaCodonMapping.items():

    proteinToRnaCount[val] += 1


def computePossibleRna(proteinString, start, stop):

    ret = 1

    for protein in proteinString[start: stop]:

        ret = (ret * proteinToRnaCount[protein]) % UPPER_BOUND

    return ret


def computePossibleRnaParallel(proteinString):

    proccesses = multiprocessing.cpu_count()

    windowSize = len(proteinString) // proccesses
    remainder = len(proteinString) % proccesses

    ret = []

    for i in range(proccesses):

        shift = min(remainder, i)

        ret.append((proteinString, i * windowSize + shift, (i + 1) * windowSize +
                    shift + (1 if i < remainder else 0)))

    with multiprocessing.Pool(processes=proccesses) as pool:

        separateResults = pool.starmap(computePossibleRna, ret)

        preStopCodon = functools.reduce(lambda agg, curr: (
            agg * curr) % UPPER_BOUND, separateResults)

        print(preStopCodon * proteinToRnaCount['Stop'] % UPPER_BOUND)


if __name__ == '__main__':
    computePossibleRnaParallel(originalProteinString)
