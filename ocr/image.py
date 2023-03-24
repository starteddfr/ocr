import urllib.request
import io

from PIL import Image
from dataclasses import dataclass


@dataclass
class TargetImage:
    image: Image

    @classmethod
    def from_url(cls, img_url: str):
        with urllib.request.urlopen(img_url) as url:
            img = Image.open(url)
            return cls(image=img)

    @property
    def bytes(self) -> bytes:
        img_bytes = io.BytesIO()
        self.image.save(img_bytes, format=self.image.format)
        img_bytes = img_bytes.getvalue()
        return img_bytes
