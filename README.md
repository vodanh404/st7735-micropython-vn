# SPI TFT với thư viện trình điều khiển ST7735 cho Raspberry Pi Pico Micropython (hỗ trợ tiếng Việt)

## Lòi cảm ơn
Dựa trên công trình từ

* [alastairhm]([https://github.com/alastairhm])

## Mô tả

* Thư viện này tương thích với dòng sản phẩm Raspberry pi pico ( sử dụng Micropython)
* Hỗ trợ hiển thị tiếng Việt
* sử dụng màn hình 1.8'128x160 RGB_TFT


### Thông tin sản phẩm

*Màu hiển thị: 16BIT RGB 65K màu
*Kích thước màn hình: 1,8 (inch)
* Loại: TFT
* IC điều khiển: ST7735S
* Độ phân giải: 128*160 (pixel)
* Giao diện mô-đun: Giao diện SPI 4 dây
* Đèn nền: 2 đèn LED trắng
* Diện tích hiệu dụng: 28,03x35,04 (mm)
* Kích thước PCB mô-đun: 38,30x62,48 (mm)
* Nhiệt độ làm việc: -20℃~60℃
* Nhiệt độ bảo quản: -30℃~70℃
* Điện áp làm việc: 5V/3.3V
* Trọng lượng: 16g

## Kết nối màn hình TFT với Raspberry Pi Pico

Đây là chân cắm được sử dụng trong mã ví dụ.

| TFT Board | Raspberry Pi Pin |
|:--------:|:-------------:|
| LED | 3v3(Out)|
| SCK | GP10 |
| SDA | GP11 |
| AO/DC | GP16 |
| Reset | GP17 |
| CS | GP18 |
| GND | GND |
| VCC | VBUS 5V |

## Cài đặt
Tải thư mục st7735 lên Raspberry Pi Pico của bạn.
Tải các tệp BMP lên thư mục gốc để tftbmp.py có thể truy cập ,
LƯU Ý: Tệp BMP cần phải ở định dạng 24 bit. 
