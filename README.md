# Light-weight wrapper repository for running omnidata inference

# License
The license for the model and the weights are entirely attributed to the original authors of the [omnidata repository](https://github.com/EPFL-VILAB/omnidata)

# Installation
```bash
pip install git://github.com/leejaeyong7/OmnidataModels
```

# Example Usage
```python
import torch
import torchvision.transforms as transforms
from omnidata import OmnidataDepthModel, OmnidataNormalModel
from PIL import Image

device = torch.device('cuda')

depth_model = OmnidataDepthModel().to(device)
normal_model = OmnidataNormalModel().to(device)

crop_size = 800
image_size = 384
image_file = 'test.png'

trans =  transforms.Compose([
    transforms.CenterCrop(crop_size),
    transforms.Resize(image_size, interpolation=Image.BILINEAR),
    transforms.ToTensor()
])

norm_trans = transforms.Normalize(mean=0.5, std=0.5)

image = Image.open(image_file)
cropped = trans(image)
normalized = norm_trans(cropped)

cropped = cropped[:3].unsqueeze(0).to(device)
normalized = normalized[:3].unsqueeze(0).to(device)

with torch.no_grad():
    depth = depth_model(normalized).clamp(0, 1)[0]
    normal = normal_model(cropped).clamp(0, 1)[0]

```