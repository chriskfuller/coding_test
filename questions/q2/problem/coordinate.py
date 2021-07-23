import re
from abc import ABCMeta, abstractmethod

class Coordinate(metaclass=ABCMeta):
    __slots__ = ['_chrom', '_start', '_stop', '_is_reverse_strand']

    # TO DO: fill in this pattern
    _pattern = re.compile(r'')

    def __init__(self, chrom, start=None, stop=None, is_reverse_strand=None):
        """
        Chromosome coordinate abstract class. OneBasedCoordinate and ZeroBasedCoordinate will
        extend this abstract class to 1- and 0- based chromosome coordinate.

        Input is flexible; a string representation can be passed as the first argument,
        or the chrom, start, stop, and is_reverse_strand can be passed individually.
        is_reverse_strand is optional; if not provided, assumed to be False.

        Valid input:
            Coordinate('chr1', 123, 456, False)
            Coordinate('chr1:123-456,+')
            Coordinate('chr1:123-456')
        Not valid:
            Coordinate('chr1', is_reverse_strand=False) : missing start_position
            Coordinate('chr1:123-456', is_reverse_strand=False) : using string and separate params
            to pass in coordinates simultaneously is not allowed.

        Args:
            chrom (str): chromosome or string representation of coordinate.
            start (int or None): start position, must be <= stop.
            stop (int or None): stop position, must be >= start.
            is_reverse_strand (bool or None): if bool, indicates whether coordinate is on reverse strand.

        Raises:
            ValueError:
                If string representation cannot be parsed; if start > stop; if start or stop < 0.
        """
        # TO DO: implement
        pass

    def __str__(self):
        return self.string_value

    @property
    def chrom(self):
        return self._chrom

    @property
    def start(self):
        return self._start

    @property
    def stop(self):
        return self._stop

    @property
    def is_reverse_strand(self):
        return self._is_reverse_strand

    @property
    @abstractmethod
    def string_value(self):
        pass

    @property
    @abstractmethod
    def string_value_unstranded(self):
        pass

    @classmethod
    def parse_string(cls, coordinate_str):
        """
        Process a string into OneBasedCoordinate/ZeroBasedCoordinate variables.
        The string format must match that produced by the corresponding
        cls.string_value/cls.string_value_unstranded properties.

        Args:
            coordinate_str (str): a string representing a Coordinate.
        Returns:
            (tuple): The extracted string value of chrom, start, stop, strand.

        Raises:
            ValueError: if the coordinate_str format does not match format
                in cls.string_value/cls.string_value_unstranded; if coordinate_str
                cannot be parsed.
        """
        # TO DO: implement
        pass

    def union(self, other_coord):
        """
        Combine self and other_coord into a coordinate (of the same type)
        representing the full range of the chromosome overlapping and between the
        two coordinates. If self and other_coord are on same strand, return
        union on that strand; otherwise, return union on positive strand.

        Example:
            self: Coordinate('chr1', 123, 456, True)
            other_coord: Coordinate('chr1', 234, 567, False)
            return: Coordinate('chr1', 123, 567, False)

        Args:
            other_coord (OneBasedCoordinate or ZeroBasedCoordinate): other coordinate to
                get union with.

        Raises:
            ValueError:
                If type of self and other_coord do not match.
                If other_coord is on a different chromosome than self.
        """
        # TO DO: implement
        pass


class OneBasedCoordinate(Coordinate):
    """
    Coordinate class where chromosome indices are 1-based and intervals are
    closed; e.g. OneBasedCoordinate('chr1', 1, 10, False) represents the first
    10 bases of chromosome 1 on the positive strand.
    """

    def to_zero_based(self):
        """
        Convert to ZeroBasedCoordinate.
        Returns:
            ZeroBasedCoordinate
        """
        return ZeroBasedCoordinate(self.chrom, self.start - 1, self.stop, self.is_reverse_strand)

    @property
    def string_value(self):
        """
        Returns: the string representation of a OneBasedCoordinate which will be:
        chr1:123-456,+
        chr1:456-789,-
        """
        if self.is_reverse_strand:
            return "{}:{}-{},-".format(self.chrom, self.start, self.stop)
        else:
            return "{}:{}-{},+".format(self.chrom, self.start, self.stop)

    @property
    def string_value_unstranded(self):
        """
        Returns: the string representation of a OneBasedCoordinate without the strand, which will be:
        chr1:123-456
        chr1:456-789
        """
        return "{}:{}-{}".format(self.chrom, self.start, self.stop)


class ZeroBasedCoordinate(Coordinate):
    """
    Coordinate class where chromosome indices are 0-based and intervals are
    half-open; e.g. OneBasedCoordinate('chr1', 0, 10, False) represents the first
    10 bases of chromosome 1 on the positive strand. The 11th base (0-based index 10)
    is not included.
    """

    def to_one_based(self):
        """
        Convert to OneBasedCoordinate.
        Returns:
            OneBasedCoordinate
        """
        return OneBasedCoordinate(self.chrom, self.start + 1, self.stop, self.is_reverse_strand)

    @property
    def string_value(self):
        """
        Returns: the string representation of a ZeroBasedCoordinate, which will be:
        chr1:123_456,+
        chr1:456_789,-
        """
        if self.is_reverse_strand:
            return "{}:{}_{},-".format(self.chrom, self.start, self.stop)
        else:
            return "{}:{}_{},+".format(self.chrom, self.start, self.stop)

    @property
    def string_value_unstranded(self):
        """
        Returns: the string representation of a ZeroBasedCoordinate without the strand, which will be:
        chr1:123_456
        chr1:456_789
        """
        return "{}:{}_{}".format(self.chrom, self.start, self.stop)
