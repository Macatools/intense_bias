import ants

import ants.core
import ants.core.ants_image

#from ants.core.ants_image import ANTsImage


print(ants.__version__)

image = "../sub-Randy_ses-01_space-stereo_T1w.nii.gz"

ants_image = ants.image_read(image)

res_image = ants.n3_bias_field_correction(ants_image)
print(res_image)

ants.image_write(res_image,
                 filename="../sub-Randy_ses-01_space-stereo_T1w_N3debias.nii.gz")
