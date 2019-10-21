## Given a dictionary with each symbol with its probability return the intervals for codification
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

## Test
#Probabilities of all symbols
symbols=['A','B','C','D','E','F','G']
vec_probabilites=[0.05,0.2,0.1,0.05,0.3,0.2,0.1]
prob_symbols=dict(zip(symbols,vec_probabilites))
#Probability intervals
prob_intv=probabilities_interval(prob_symbols)
print('Probability intervals:',prob_intv)

#Sequence to be send
emission=['B','B','F','F','G','A']

#Codification
value=arithmetic_coding(emission,prob_intv)
print('Codification value',value)

#Decode
decode_sequence=arithemtic_decode(value[0],prob_intv,len(emission))
print('Decode sequence:',decode_sequence)
