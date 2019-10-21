import math
def probabilities_interval(prob_symbols):
    prob_symbols_interval={}
    prob_low=0
    symbols=list(prob_symbols.keys())
    for symbol in symbols:
        prob_high=prob_symbols.get(symbol)
        prob_symbols_interval[symbol]=(round(prob_low,2),round(prob_low+prob_high,2))
        prob_low+=prob_symbols.get(symbol)
    return prob_symbols_interval
## Return the value of the probability function
def return_CDF_symbol(symbol,probabilities_interval):
    cdf=probabilities_interval.get(symbol)[0]
    return cdf
## Codification algorithm
def arithmetic_coding(emission,probability_interval):
    ao=1
    co=0
    for symbol in emission:  
        cdf=return_CDF_symbol(symbol,probability_interval)
        co+=ao*cdf
        ao=ao*prob_symbols.get(symbol)
    
    return(co,co+ao)
## Decode algorithm
def arithemtic_decode(value,prob_symbols_interval,length_emission):
    # Inputs: Value of codification
    #          Probabilities interval
    #          Length emission = Length of codification block
    low=0
    high=1
    interval=high-low
    sequence=[]
    length=0
    while length<length_emission:
        for symbol in symbols:
            subinterval_low=prob_symbols_interval.get(symbol)[0]
            subinterval_high=prob_symbols_interval.get(symbol)[1]
            if((subinterval_low<=((value-low)/interval)) and (((value-low)/interval))<=subinterval_high):
                sequence.append(symbol)
                break
        high=low+interval*subinterval_high
        low=low+interval*subinterval_low
        interval=high-low
        length=length+1
    return sequence

def text_extraction_prob(file):
    f = open(file, "r")
    text=f.read()
    words=[]
    for i in range(len(text)):
        words.append(text[i])
    symbols=list(set(words))
    total_words=len(text)
    probabilities=[]
    for symbol in symbols:
        count=text.count(symbol)
        probabilities.append(count/total_words)
    prob_symbols=dict(zip(symbols,probabilities))
    prob_symbols_intv=probabilities_interval(prob_symbols)
    f.close()
    return prob_symbols,prob_symbols_intv,text,symbols

def create_coded_file(step,name_file):
    f=open(name_file,'w+')
    for i in range(math.ceil(len(raw_text)/step)):
        sequence=raw_text[i*step:i*step+min(len(raw_text)-step*i,step)]
        b=arithmetic_coding(sequence,prob_symbols_intv)
        f.write('{},'.format(b[0]+b[1]/2))
    f.close()

def create_decode_file(step,name_file_decoded,name_file_encoded):
    decoded=open(name_file_decoded,'w+')
    encoded=open(name_file_encoded,'r')
    numbers=encoded.read().split(',')[:-1]
    for number in numbers:
        sequence=arithemtic_decode(float(number),prob_symbols_intv,step)
        c=''.join(sequence)
        decoded.write(c)
    encoded.close()
    decoded.close()

#Test
prob_symbols,prob_symbols_intv,raw_text,symbols=text_extraction_prob('text_test.txt')
create_coded_file(4,'encoded.txt')
create_decode_file(4,'decoded.txt','encoded.txt')
