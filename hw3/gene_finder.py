# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Elizabeth O'Callaghan
"""



# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random
from load import load_seq

def stopCodon(currentCodon):
    """returns true if the currentCodon is a stop Codon"""
    return (currentCodon in codons[10])
    
def startCodon(currentCodon):
    """return true if the currentCodon is the startCodon"""
    return (currentCodon in codons[3])
    
def find_Amino_Acid(currentCodon):
    """finds the Amino Acid given the currentCodon"""
    for i in range(len(codons)):
        if (currentCodon in codons[i]):
            return aa[i]
    

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    
    output = ""    
    for s in L:
        output = output + s
    return output
        


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
        
    proteinSequence = ""
    for i in range (len(dna)/3):
        nextCodon = ""
        nextCodon += dna[3*i:3*i+3]
        proteinSequence += find_Amino_Acid(nextCodon)
    return proteinSequence

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    codonList = []
    for i in range (len(codons)):
        codonList.append(collapse(codons[i]))
    codonString = collapse(codonList)
    print "Input: ", codonString
    print "Expected Output: FFLLLLLLIIIMVVVVSSSSSSPPPPTTTTAAAAYY|||HHQQNNKKDDEECCWRRRRRRGGGG"
    print "Actual Output:  ", coding_strand_to_AA(codonString)
    
    
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE
    
    newDna = ""
    for i in range (len(dna)):
        if (dna[i]=='A'):
            newDna += 'T'
            
        elif(dna[i]=='T'):
            newDna += 'A'

        elif(dna[i]=='C'):
            newDna +='G'

        elif(dna[i]=='G'):
            newDna +='C'
    return newDna
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    dna = "ATGCATGCGTAC"
    print "Input: ", dna
    print "Expected Output:  TACGTACGCATG"
    print "Actual Output:   ", get_reverse_complement(dna)
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    dnaSequence = ""
    for i in range (len(dna)):
        nextCodon = dna[3*i:3*i+3]
        if (stopCodon(nextCodon)):
            break
        dnaSequence = dnaSequence + nextCodon
        
    return dnaSequence

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    dnaNoStop = codons[3][0]+codons[0][1]+codons[1][5]+codons[11][1]+codons[14][1]+codons[1][1]
    dnaStop0 = codons[3][0]+codons[0][1]+codons[1][5]+codons[11][1]+codons[14][1]+codons[10][0]+codons[1][1]
    dnaStop1 = codons[3][0]+codons[0][1]+codons[1][5]+codons[11][1]+codons[14][1]+codons[10][1]+codons[1][1]
    dnaStop2 = codons[3][0]+codons[0][1]+codons[1][5]+codons[11][1]+codons[14][1]+codons[10][2]+codons[1][1]
    print "Input: ", dnaNoStop
    print "Expected Output:ATGTTCCTGCACAAGTTG"
    print "Actual Output: ", rest_of_ORF(dnaNoStop)
    print "Input: ", dnaStop0
    print "Expected Output:ATGTTCCTGCACAAG"
    print "Actual Output: ", rest_of_ORF(dnaStop0)
    print "Input: ", dnaStop1
    print "Expected Output:ATGTTCCTGCACAAG"
    print "Actual Output: ", rest_of_ORF(dnaStop1)
    print "Input: ", dnaStop2
    print "Expected Output:ATGTTCCTGCACAAG"
    print "Actual Output: ", rest_of_ORF(dnaStop2)
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORFs = []
    i = 0
    while (i < len(dna)):
        nextCodon = dna[3*i:3*i+3]
        if(startCodon(nextCodon)):
            currentDna = dna[3*i:len(dna)]
            dnaSequence = rest_of_ORF(currentDna)
            ORFs.append(dnaSequence)
            i = i+len(dnaSequence)/3
        else:
            i+=1
    return ORFs
            
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    """sC is the start Codon
    stC0, stC1, and stC2 are the stop codons
    and rc, rc1, rc2, rc3 are three random codons"""
    sC = codons[3][0]
    stC0 = codons[10][0]
    stC1 = codons[10][1]
    stC2 = codons[10][2]
    rc = codons[1][1]
    rc1 = codons[1][5] 
    rc2 = codons[12][0]
    rc3 = codons[14][1]
    
    randomLongSequence = rc + rc1 + rc2 + rc3
    randomLongSequence1 = rc1 + rc3 + rc2 + rc
    randomLongSequence2 = rc3 + rc2 + rc + rc1
    ORF0 = sC + randomLongSequence + stC0
    ORF1 = sC + randomLongSequence1 + stC1
    ORF2 = sC + randomLongSequence2 + stC2
    
    dna = randomLongSequence + stC0 + sC + ORF0 + sC + ORF1 + stC1 + ORF2 + stC2
    dna1 = dna + randomLongSequence + dna
    ExpectedOutput1 = [sC+sC + randomLongSequence, sC + sC + randomLongSequence1,sC + randomLongSequence2 ] 
    ExpectedOutput2 = [sC+sC + randomLongSequence, sC + sC + randomLongSequence1,sC + randomLongSequence2, sC+sC + randomLongSequence, sC + sC + randomLongSequence1,sC + randomLongSequence2 ]
    print "Input: ", dna
    print "Expected Output:", ExpectedOutput1
    print "Actual Output:  ", find_all_ORFs_oneframe(dna)
    print "Input: ", dna1
    print "Expected Output:", ExpectedOutput2
    print "Actual Output:  ", find_all_ORFs_oneframe(dna1)    
    
    
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    frame0Shift = dna
    frame1Shift = dna[1:len(dna)] 
    frame2Shift = dna[2:len(dna)]

    list0Shift = find_all_ORFs_oneframe(frame0Shift)
    list1Shift = find_all_ORFs_oneframe(frame1Shift)
    list2Shift = find_all_ORFs_oneframe(frame2Shift)
    all_ORFs = []
    for i in range(len(list0Shift)):
        all_ORFs.append(list0Shift[i])
        
    for i in range(len(list1Shift)):
        all_ORFs.append(list1Shift[i])

    for i in range(len(list2Shift)):
        all_ORFs.append(list2Shift[i])
        
    return all_ORFs 

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    
    dna = "ATGTTGATATAG"
    dna1 = "GATGTTCATATAGGC"
    dna2 = "CGATGTTAATATAGC"
    longDna = dna + dna1 + dna2
   
    print "Input: ", longDna
    print "Expected Output:",["ATGTTGATA", "ATGTTCATA", "ATGTTAATA"]
    print "Actual Output:  ", find_all_ORFs(longDna)

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dnaReverse = get_reverse_complement(dna)
    ORFsRegular = find_all_ORFs(dna)
    ORFsReverse = find_all_ORFs(dnaReverse)
    all_ORFs = []
    for i in range(len(ORFsRegular)):
        all_ORFs.append(ORFsRegular[i])    
    for i in range(len(ORFsReverse)):
        all_ORFs.append(ORFsReverse[i])
        
    return all_ORFs

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    dna = "ATGTTGATATAG"
    dna1 = "GATGTTCATATAGGC"
    dna2 = "CGATGTTAATATAGC"
    dnaC = get_reverse_complement(dna)
    dnaC1 = get_reverse_complement(dna1) 
    dnaC2 = get_reverse_complement(dna2)
    longDna = dna + dna1 + dna2 + dnaC + dnaC1 + dnaC2
    
    print "Input: ", longDna
    print "Expected Output:",["ATGTTGATA", "ATGTTCATA", "ATGTTAATA","ATGTTGATA", "ATGTTCATA", "ATGTTAATA"]
    print "Actual Output:  ", find_all_ORFs_both_strands(longDna)

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    allORFs = find_all_ORFs_both_strands(dna)
    currentLongest = ""
    for i in range(len(allORFs)):
        if (len(allORFs[i])>len(currentLongest)):
            currentLongest = allORFs[i]
            
    return currentLongest
    
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    dna = "ATGTTGATATAG"
    dnaLong = "ATGAAATTGATATAG"
    dna1 = "GATGTTCATATAGGC"
    dna2 = "CGATGTTAATATAGC"
    dnaC = get_reverse_complement(dna)
    dnaCLong = get_reverse_complement(dnaLong)
    dnaC1 = get_reverse_complement(dna1) 
    dnaC2 = get_reverse_complement(dna2)
    longDnaFoward = dnaLong + dna1 + dna2 + dnaC + dnaC1 + dnaC2
    longDnaReverse = dna + dna1 + dna2 + dnaC + dnaCLong + dnaC1 + dnaC2
    
    print "Input: ", longDnaFoward
    print "Expected Output:ATGAAATTGATA"
    print "Actual Output: ", longest_ORF(longDnaFoward)
    print "Input: ", longDnaReverse
    print "Expected Output:ATGAAATTGATA"
    print "Actual Output: ", longest_ORF(longDnaReverse)
    
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    maximumLength = 0
    dnaList = []
    for i in range(len(dna)):
        dnaList.append(dna[i])
    for i in range(num_trials):
        shuffledDnaList = list(dna)
        random.shuffle(shuffledDnaList)
        shuffledDna = collapse(shuffledDnaList)
        currentLongest = longest_ORF(shuffledDna)
        if( len(currentLongest) > maximumLength ):
            maximumLength = len(currentLongest)
            
    return maximumLength

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    list_Of_ORFs = find_all_ORFs_both_strands(dna)
    list_Of_Genes = []
    aminoAcidSequences = []
    for i in range(len(list_Of_ORFs)):
        currentLength = len(list_Of_ORFs[i])
        
        if(currentLength >= threshold):
            list_Of_Genes.append(list_Of_ORFs[i])
    
    for i in range (len(list_Of_Genes)):
        currentDna = list_Of_Genes[i]
        aminoAcid = coding_strand_to_AA(currentDna)
        aminoAcidSequences.append(aminoAcid)
        
    return aminoAcidSequences
        
            
if __name__ == '__main__':
    dna = load_seq("./data/X73525.fa")
    
    threshold = longest_ORF_noncoding(dna, 1500)
    print threshold
    aminoAcids = gene_finder(dna, threshold)
    for i in range(len(aminoAcids)):
        print aminoAcids[i]