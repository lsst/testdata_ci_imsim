==========
``testdata_ci_imsim``
==========

``testdata_ci_imsim`` provides a minimal amount of test data sufficient to run
the Rubin Observatory science pipelines from single frame processing through
to coaddition processing. This data is sourced from the
`DC2 simulations`_, run 2.2i. 

.. _DC2 simulations: https://lsstdesc.org/DC2-production/

Obtaining test data
===================

The data used by ``ci_imsim`` is stored using `Git LFS`_; refer to the
`relevant documentation`_ for details on how to check out this repository.

.. _Git LFS: https://git-lfs.github.com
.. _relevant documentation: https://developer.lsst.io/git/git-lfs.html

Running the tests
=================

This package only contains data; packages that use it must implement tests.

Set up the package
------------------

The package must be set up in the usual way before running::

$ cd testdata_ci_imsim
$ setup -j -r .

Reference catalog
-----------------

An appropriate reference catalog for both astrometry and photometry is
provided in the ``ref_cats`` directory. This reference catalog contains the 
input values, as well as a flag for whether each source is resolved.

Truth table
-----------

A parquet-formatted ``truth_summary`` table for the entire tract is included.
See `PREOPS-584 <https://jira.lsstcorp.org/browse/PREOPS-584>`_ for details.

Red Galaxy Table
----------------

A parquet-formatted ``cosmodc2_1_1_4_redmapper_v0_8_1_redgals`` red galaxy truth table is included.
See `DM-33957 <https://jira.lsstcorp.org/browse/DM-33957>`_ for details.

Visits
------

The visit/detectors contained in this dataset (taken from copy_data.log) are:

u:
(433038, 82), (277060, 82), (466756, 13),
(180001, 13), (180001, 14), (466756, 14)

g:
(419000, 48), (254379, 48), (419000, 51),
(254379, 51), (254358, 54), (183772, 54)

r:
(257768, 161), (212739, 161), (213545, 99),
(456716, 99), (212071, 54), (448317, 54)

i:
(256383, 26), (227976, 26), (227951, 54),
(280217, 54), (211545, 138), (496989, 138)

z:
(226983, 36), (209018, 36), (209018, 37),
(226983, 37), (8003, 76), (209063, 76)

y:
(189382, 130), (407919, 130), (37657, 141),
(12466, 141), (206039, 55), (5884, 55)

