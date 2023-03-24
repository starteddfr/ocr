from .image import TargetImage
from .result import ResultFactory, Result
import requests


class OCRExtractor:

    def __init__(self, image_url: str):
        self.image = TargetImage.from_url(img_url=image_url)

    def get_result(self) -> Result:
        kwargs = {
            "url": "https://api.api-ninjas.com/v1/imagetotext",
            "files": {"image": self.image.bytes},
            "headers": {"Origin": "https://api-ninjas.com", "Referer": "https://api-ninjas.com/"}
        }

        response = requests.post(**kwargs)
        return ResultFactory.create(response.json())
