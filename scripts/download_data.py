from pathlib import Path
from urllib.request import urlopen
import shutil

# Thu muc goc cua project
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://d37ci6vzurychx.cloudfront.net"


def download_file(filename, url):
    destination = DATA_DIR / filename
    temporary = DATA_DIR / (filename + ".part")

    if destination.exists() and destination.stat().st_size > 0:
        print(f"Đã có: {filename}")
        return

    print(f"Đang tải: {filename}")

    try:
        with urlopen(url, timeout=120) as response:
            with temporary.open("wb") as output:
                shutil.copyfileobj(response, output)

        if temporary.stat().st_size == 0:
            raise ValueError("File rỗng")

        temporary.replace(destination)
        print(f"Thành công: {filename}")

    except Exception as e:
        print(f"Tải thất bại: {filename} - {e}")
        temporary.unlink(missing_ok=True)


for month in range(1, 13):
    filename = f"yellow_tripdata_2025-{month:02d}.parquet"
    url = f"{BASE_URL}/trip-data/{filename}"
    download_file(filename, url)

download_file(
    "taxi_zone_lookup.csv",
    f"{BASE_URL}/misc/taxi_zone_lookup.csv"
)

print("Hoàn thành!")
