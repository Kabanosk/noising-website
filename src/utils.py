import shutil
from pathlib import Path
import zipfile

import librosa
import soundfile as sf
from tqdm import tqdm


class ZipDataset:
    def __init__(self, file: bytes, path: str = "data/dataset.zip"):
        self.file = file
        self.path = Path(path)
        self.prepare_dataset()

    def prepare_dataset(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, 'wb') as zip_file:
            zip_file.write(self.file)
        with zipfile.ZipFile(self.path, 'r') as zip_file:
            zip_file.extractall(str(self.path.parent))

    def save(self, output_filename):
        output_filename = (Path('data') / output_filename).with_suffix(".zip")
        with zipfile.ZipFile(str(output_filename), 'w', zipfile.ZIP_DEFLATED) as new_zip:
            p_dir = self.path.parent
            for file in tqdm(list(p_dir.rglob('*.wav')), desc="Saving zip file"):
                new_zip.write(file, arcname=file.name)

    def downsample(self, sr: int = 8000):
        p_dir = self.path.parent
        for file in tqdm(list(p_dir.rglob('*.wav')), desc="Downsampling"):
            y, _ = librosa.load(file, sr=sr)
            sf.write(file, y, sr)
