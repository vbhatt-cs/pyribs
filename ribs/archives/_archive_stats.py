"""Provides ArchiveStats."""
import dataclasses

import numpy as np


@dataclasses.dataclass
class ArchiveStats:
    """Holds statistics about an archive.

    Attributes of type :class:`~numpy.floating` will match the
    :attr:`~ArchiveBase.dtype` of their archive.
    """

    #: Number of elites in the archive.
    num_elites: int

    #: Proportion of cells in the archive that have an elite - always in the
    #: range :math:`[0,1]`.
    coverage: np.floating

    #: QD score, i.e. sum of objective values of all elites in the archive.
    #: **This score only makes sense if objective values are non-negative.**
    qd_score: np.floating

    #: Normalized QD score, i.e. the QD score divided by the number of cells in
    #: the archive.
    norm_qd_score: np.floating

    #: Maximum objective value of the elites in the archive. None if there are
    #: no elites in the archive.
    obj_max: np.floating

    #: Mean objective value of the elites in the archive. None if there are no
    #: elites in the archive.
    obj_mean: np.floating
