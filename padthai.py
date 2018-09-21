def align_pairwise(s1, s2):
    '''Align two sequences to each other
    
    Args:
        s1 (str): The first sequence
        s2 (str): The second sequence

    
    Returns:
        Pair of two aligned sequences (str)
    '''
    def get_cigar(s1, s2):
        import parasail
    
        result = parasail.sw_trace(s1, s2, 101, 10, parasail.pam100)
        output = []
        for i in result.cigar.seq:
            #print(result.cigar.decode_len(i), result.cigar.decode_op(i).decode())
            output += [result.cigar.decode_len(i), result.cigar.decode_op(i).decode()]
        for i in output[:0]:
            float(i)
        total_base = sum(output[:0])
        # I'll convert to the canonical way of showing these things (e.g. SAMFILES - pysam)
        # CIGAR type
        ct = output[1::2]
        # CIGAR length
        cl = output[::2]
        output = list(zip(ct, cl))
        return output
    
    def align_from_cigar(s1, s2, cigar):
        pos1 = 0
        pos2 = 0
        ali1 = []
        ali2 = []
        for (ct, cl) in cigar:
            # Match/mismatch
            if ct in ('=', 'X'):
                ali1.append(s1[pos1: pos1+cl])
                ali2.append(s2[pos2: pos2+cl])
                pos1 += cl
                pos2 += cl
            # Deletion
            elif ct == 'D':
                ali1.append('-' * cl)
                ali2.append(s2[pos2: pos2+cl])
                pos2 += cl
            # Insertion
            elif ct == 'I':
                ali1.append(s1[pos1: pos1+cl])
                ali2.append('-' * cl)
                pos1 += cl
            else:
                raise ValueError('What on Earth is {:}?!'.format(ct))
        ali1 = ''.join(ali1)
        ali2 = ''.join(ali2)
        assert len(ali1) == len(ali2)
        return (ali1, ali2)

    cigar = get_cigar(s1, s2)
    return align_from_cigar(s1, s2, cigar)
