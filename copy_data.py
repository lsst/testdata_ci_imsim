from lsst.daf.persistence import Butler
from modelling_research.repos import copy_repo_subset
import os

# See DM-26083
path_dc2 = '/datasets/DC2/repoRun2.2i'
butler_coadd = Butler(os.path.join(path_dc2, 'rerun/w_2020_48/DM-27780/coadd'))

copy_repo_subset(
    path_in=path_dc2, path_out='./', butler_coadd=butler_coadd,
    tract_patches={3828: ['3,3']}, filters='ugrizy', filter_flat_override='i',
)
