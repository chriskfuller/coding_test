import os
from pyfaidx import Fasta as PyfaidxFasta
from coordinate import OneBasedCoordinate, ZeroBasedCoordinate

class InvalidGenomicCoordinateException(Exception):
    pass

class FastaQuerier:

    def __init__(self, fasta_file_path, name=None):
        """
        A querying class allowing sequences to be extracted from fasta file using
        Coordinates.

        Args:
            fasta_file_path (str): fasta_file_path
            name (str): name of the fasta_file for description purpose only.
                If None, the file name of the fasta file will be used.
        """
        if name is None:
            name = os.path.basename(fasta_file_path)
        self._name = name
        self._pyfaidx_fasta = PyfaidxFasta(fasta_file_path)

    def retrieve_sequence(self, coordinate, to_upper=True):
        """
        Given a Coordinate (OneBasedCoordinate or ZeroBasedCoordinate), return the
        sequence at the location represented by the coordinate.

        Args:
            coordinate (OneBasedCoordinate or ZeroBasedCoordinate): the coordinate
                representing the region of the genome to extract.

        Returns:
            sequence (str): the sequence at the location represented by the input
                coordinate.

        Raises:
            ValueError: if coordinate is not a OneBasedCoordinate or ZeroBasedCoordinate.
            InvalidGenomicCoordinateException: if the given coordinate represents a
                location not in the genome.
        """
        if isinstance(coordinate, OneBasedCoordinate):
            k = 1
        elif isinstance(coordinate, ZeroBasedCoordinate):
            k = 0
        else:
            raise ValueError(f'Coordinate must be OneBasedCoordinate or ZeroBasedCoordinate, not {type(coordinate)}')

        try:
            if coordinate.is_reverse_strand:
                sequence = (-self._pyfaidx_fasta[coordinate.chrom][coordinate.start - k:coordinate.stop]).seq
            else:
                sequence = self._pyfaidx_fasta[coordinate.chrom][coordinate.start - k:coordinate.stop].seq
            return sequence.upper() if to_upper else sequence
        except:
            raise InvalidGenomicCoordinateException(f'Invalid coordinate {coordinate} for genome {self._name}')

    def get_chromosome_names(self):
        """
        Retrieve all of the chromosome names from the genome fasta.
        """
        return self._pyfaidx_fasta.keys()

    def retrieve_chromosome_sequence(self, chrom_name):
        """
        Retrieve the full sequence associated with the given chromosome name.
        Args:
            chrom_name (str): the name of the chromosome to retrieve.
        Returns:
            (str): the sequence associated with the given chromosome.
        """
        return self._pyfaidx_fasta[chrom_name][:].seq.upper()
