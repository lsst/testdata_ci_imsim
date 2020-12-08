==========
``testdata_ci_imsim``
==========

``testdata_ci_imsim`` provides a minimal amount of test data sufficient to run
the Rubin Observatory science pipelines from single frame processing through
to coaddition processing. This data is sourced from the
[DC2 simulations](https://lsstdesc.org/DC2-production/), run 2.2i. 


Obtaining test data
===================

The data used by ``ci_imsim`` is stored using `Git LFS`_; refer to the
`relevant documentation`_ for details on how to check out this repository.

.. _Git LFS: https://git-lfs.github.com
.. _relevant LSST documentation: https://developer.lsst.io/git/git-lfs.html

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
input values with errors, as well as a flag for whether each source is 
extended or resolved.

