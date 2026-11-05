# NYC Taxi Data Engineering Project

Project đồ án Data Engineering với dữ liệu chuyến taxi vàng của New York năm 2025. Repo hiện có script tải dữ liệu nguồn, notebook khám phá dữ liệu và cấu hình MinIO/PostgreSQL để phát triển pipeline.

## Cấu trúc

- `scripts/download_data.py`: tải 12 file Parquet theo tháng và bảng tra cứu taxi zone từ NYC TLC.
- `notebooks/eda.ipynb`: khám phá schema, chất lượng dữ liệu, giá cước và một số trường hợp bất thường.
- `data/raw/taxi_zone_lookup.csv`: bảng tra cứu taxi zone.
- `docker-compose.yml`: dịch vụ MinIO và PostgreSQL chạy cục bộ.

Các file Parquet được tải lại bằng script nên không được đưa lên GitHub.

## Chạy cục bộ

1. Tạo môi trường Python và cài thư viện: `python -m pip install -r requirements.txt`.
2. Sao chép `.env.example` thành `.env`, rồi đặt tên người dùng và mật khẩu riêng trong `.env`.
3. Nếu cần MinIO/PostgreSQL, chạy `docker compose up -d`.
4. Chạy `python scripts/download_data.py` để tải dữ liệu nguồn.
5. Mở `notebooks/eda.ipynb` bằng Jupyter/VS Code từ thư mục `notebooks`.

Nguồn dữ liệu: [NYC Taxi & Limousine Commission Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
