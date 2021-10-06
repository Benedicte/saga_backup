import h5py
import numpy

def LonRead(InFile,*DatKey):
    # InFile: name of file that data is stored on
    # DatKey: dictionary keys of data to read in
    
    # Dictionary to return key/data pairs
    Data = {}
    
    # Input file 
    Tape = h5py.File(InFile,'r')
    
    # NS = number of spinorbitals
    # NB = number of basis functions
    
    if 'MolOrbOccs' in DatKey:
        # List of spinorbital occupation numbers: 0 / 1
        # Integer array with dimension (NS)
        Data['MolOrbOccs'] = Tape['MolOrbOccs'][:]
    
    if 'SpinString' in DatKey:
        # Spin-ordering sequence of spinorbitals: 0 & 1
        # Integer array with dimension (NS)
        Data['SpinString'] = Tape['SpinString'][:]
    
    if 'MolOrbEigs' in DatKey:
        # Spinorbital energy levels / eigenvalues
        # Complex array with dimension (NS)
        Data['MolOrbEigs'] = Tape['MolOrbEigs'][:]
    
    if 'MolOrbVecs' in DatKey:
        # Spinorbital molecular orbital coefficients
        # Complex array with dimension (NB,NS)
        Data['MolOrbVecs'] = Tape['MolOrbVecs'][...]
    
    if 'KinEneInts' in DatKey:
        # Kinetic energy integrals in spinorbital basis 
        # Data[p,q] = <p|T|q>
        # Complex array with dimension (NS,NS)
        Data['KinEneInts'] = Tape['KinEneInts'][...]
    
    if 'NucAttInts' in DatKey:
        # Nuclear attraction integrals in spinorbital basis 
        # Data[p,q] = <p|Z/r|q>
        # Complex array with dimension (NS,NS)
        Data['NucAttInts'] = Tape['NucAttInts'][...]
    
    if 'DipMomInts' in DatKey:
        # Dipole moment integrals in spinorbital basis 
        # Data[p,q,i] = <p|D_i|q>
        # Complex array with dimension (NS,NS,3)
        Data['DipMomInts'] = Tape['DipMomInts'][...]
    
    if 'EleRepInts' in DatKey:
        # Antisymmetrised two-electron integrals in spinorbital basis
        # Data[p,q,r,s] = <pq||rs> = <pq|rs> - <pq|sr>
        # Complex array with dimension (NS,NS,NS,NS)
        Data['EleRepInts'] = Tape['EleRepInts'][...]

    if 'OviIntAO' in DatKey:
        #overlap_integrals dimensions(NB, NB)
        Data['OviIntAO'] = Tape['OviIntAO'][...]

    if 'KinEneIntAO' in DatKey:
        # dimensions (NB,NB)
        Data['KinEneIntAO'] = Tape['KinEneIntAO'][...]

    if 'NucAttIntAO' in DatKey:
        Data['NucAttIntAO'] = Tape['NucAttIntAO'][...]
    
    if 'EleRepIntAO' in DatKey:
        Data['EleRepIntAO'] = Tape['EleRepIntAO'][...]

    if 'DipMomIntAO' in DatKey:
        Data['DipMomIntAO'] = Tape['DipMomIntAO'][...]

    if 'CMO_0' in DatKey:
        Data['CMO_0'] = Tape['CMO_0'][...]
    
    if 'CMO_1' in DatKey:
        Data['CMO_1'] = Tape['CMO_1'][...]

    Tape.close()

    return Data
