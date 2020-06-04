inputfile ="DNAFile.txt"
f = open(inputfile, "r")
sequence = f.read()

sequence = sequence.replace("\n", "")
sequence = sequence.replace("\r", "")

Amino_chart = {
    'I' : ['ATA', 'ATT', 'ATC'],
    'L' : ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
    'V' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'F' : ['TTT', 'TTC'],
    'M' : ['ATG']
}

def SLC(codon):
    for SLC in Amino_chart:
        if codon.upper() in Amino_chart[SLC]:
            return SLC
    else:
        return " "

def translate(sequence):
    SLC = ""
    error = ""

    if len(sequence)%3 == 0:
        print(error)
    else:
        for i in sequence[:]:
            if i.upper() is ['A', 'T', 'C', 'G']:
                print(error)
    pass
# the coding used for the error coding are as follows: 
    if not error:
        for i in range(len(sequence)// 3):
            codon = sequence[(i*3):(i*3)+3]
            SLC == SLC(codon)
        
        if SLC =='':
            print(error)
        else:
            print(SLC)

        return(False, SLC) if SLC != "" else (True, error)

def mutated():
    dnafile = open('DNAFile.txt', 'r')
    dna = dnafile.read()
    
    dna = sequence.replace("\n", "")
    dna = sequence.replace("\r", "")

    a = dna.find('a')

    mutated = dna.replace('a', 'A')
    normalD = dna.replace('a', 'T')

    write_to ('mutatedDNA.txt', mutated)
    write_to  ('normalDNA.txt', normalD)

def write_to(fname, text):
    f = open(fname, 'a') 
    f.write(text)
    f.close()

def read_only(fname):
    with open(fname, 'r') as f:
        sequence = f.read()
    return sequence

def txttranslation():
    mutated = translate(read_only('mutatedDNA.txt'))
    normal = translate(read_only('normalDNA.txt'))

    txttranslation = translate(mutated[20:935])
    txttranslation == mutated


      


     